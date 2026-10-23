
import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Locate the member data file relative to this Python file.
DATA_FILE = Path(__file__).parent / "data" / "members.json"

# Minimum similarity required to return a result.
# This threshold must be evaluated during testing.
MATCH_THRESHOLD = 0.25


class MemberMatcher:
    """Finds member profiles that best match a user's question."""

    def __init__(self, data_file=DATA_FILE):
        """Load member data and prepare the TF-IDF search index."""

        with open(data_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.group_code = data["groupCode"]
        self.members = data["members"]

        # Build one searchable text document for each member.
        documents = []

        for member in self.members:
            searchable_fields = [
                member.get("fullName", ""),
                " ".join(member.get("aliases", [])),
                " ".join(member.get("skills", [])),
                member.get("role", ""),
                member.get("problem", ""),
                member.get("contribution", ""),
                member.get("feature", ""),
                member.get("targetUser", ""),
                member.get("introductionDraft", ""),
            ]

            # Ignore empty fields and placeholder values.
            searchable_fields = [
                value
                for value in searchable_fields
                if value
                and isinstance(value, str)
                and "PENDING_" not in value
            ]

            documents.append(" ".join(searchable_fields))

        # Convert member documents into TF-IDF vectors.
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            strip_accents="unicode",
        )

        self.member_vectors = self.vectorizer.fit_transform(documents)

    def search(self, query):
        """Return the best matching member or a no-match response."""

        # Validate the query.
        if not isinstance(query, str) or not query.strip():
            return {
                "matched": False,
                "message": "Please enter a question or search term.",
                "member": None,
                "similarity": 0.0,
            }

        # Convert the query into the same TF-IDF representation.
        query_vector = self.vectorizer.transform([query.strip()])

        # Calculate cosine similarity between the query and each member.
        scores = cosine_similarity(
            query_vector,
            self.member_vectors,
        ).flatten()

        # Find the member with the highest similarity score.
        best_index = int(scores.argmax())
        best_score = float(scores[best_index])
        best_member = self.members[best_index]

        # Check whether the query explicitly contains a member's
        # full name or approved alias.
        normalized_query = query.casefold()

        full_name = best_member.get("fullName", "").strip()
        exact_identity = bool(
            full_name
            and full_name.casefold() in normalized_query
        )

        if not exact_identity:
            for alias in best_member.get("aliases", []):
                alias = alias.strip()

                if alias and alias.casefold() in normalized_query:
                    exact_identity = True
                    break

        # Reject weak matches unless the query identifies the member.
        if best_score < MATCH_THRESHOLD and not exact_identity:
            return {
                "matched": False,
                "message": (
                    "No suitable member match was found. "
                    "Try a member's name or a verified skill."
                ),
                "member": None,
                "similarity": round(best_score, 4),
            }

        # Return only public fields and confirmed profile details.
        public_profile = {
            "id": best_member["id"],
            "fullName": best_member["fullName"],
            "aliases": best_member.get("aliases", []),
            "skills": best_member.get("skills", []),
        }

        # Add optional fields only when they contain confirmed details.
        optional_fields = [
            "role",
            "contribution",
            "feature",
            "introductionDraft",
        ]

        for field in optional_fields:
            value = best_member.get(field, "")

            if (
                isinstance(value, str)
                and value.strip()
                and "PENDING_" not in value
                and not value.lower().startswith(
                    "profile awaiting confirmation"
                )
            ):
                public_profile[field] = value

        return {
            "matched": True,
            "message": "A possible member match was found.",
            "member": public_profile,
            "similarity": round(best_score, 4),
        }
