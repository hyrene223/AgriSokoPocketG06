
import React, { useState } from "react";
import {
  SafeAreaView,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
  ActivityIndicator,
} from "react-native";

type Member = {
  id: string;
  fullName: string;
  aliases: string[];
  skills: string[];
  role?: string;
  contribution?: string;
  feature?: string;
};

type SearchResponse = {
  matched: boolean;
  message: string;
  member: Member | null;
  similarity: number;
};

const API_URL = "http://10.100.192.3:8000";

export default function App() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<SearchResponse | null>(null);
  const [error, setError] = useState("");

  async function handleSearch() {
    const trimmedQuery = query.trim();

    if (!trimmedQuery) {
      setError("Please enter a name or search question.");
      setResult(null);
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/search`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: trimmedQuery }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          typeof data.detail === "string"
            ? data.detail
            : "The search request failed."
        );
      }

      setResult(data as SearchResponse);
    } catch {
      setError(
        "Could not contact the AI service. Check that the backend is running on port 8000."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.header}>
          <Text style={styles.logo}>AS</Text>
          <Text style={styles.appName}>AgriSoko Pocket</Text>
          <Text style={styles.groupLabel}>GROUP G06</Text>
          <Text style={styles.tagline}>
            Meet our team. Discover our skills.
          </Text>
        </View>

        <View style={styles.card}>
          <Text style={styles.sectionTitle}>Find a team member</Text>
          <Text style={styles.description}>
            Search by a member's name or ask about verified team skills.
          </Text>

          <TextInput
            style={styles.input}
            value={query}
            onChangeText={setQuery}
            placeholder="e.g. Who is Nsabimana?"
            placeholderTextColor="#7B8585"
            returnKeyType="search"
            onSubmitEditing={handleSearch}
            accessibilityLabel="Search team members"
          />

          <TouchableOpacity
            style={styles.searchButton}
            onPress={handleSearch}
            disabled={loading}
            accessibilityRole="button"
          >
            {loading ? (
              <ActivityIndicator color="#FFFFFF" />
            ) : (
              <Text style={styles.searchButtonText}>Search members</Text>
            )}
          </TouchableOpacity>

          {loading && (
            <Text style={styles.statusText}>Searching the AI service...</Text>
          )}

          {!!error && (
            <View style={styles.errorBox}>
              <Text style={styles.errorText}>{error}</Text>
            </View>
          )}

          {result && (
            <View style={styles.resultBox}>
              <Text style={styles.resultTitle}>
                {result.matched && result.member
                  ? result.member.fullName
                  : "No suitable match"}
              </Text>

              <Text style={styles.resultText}>{result.message}</Text>

              {result.matched && result.member && (
                <>
                  {result.member.aliases.length > 0 && (
                    <Text style={styles.detailText}>
                      Also known as: {result.member.aliases.join(", ")}
                    </Text>
                  )}

                  {result.member.role && (
                    <Text style={styles.detailText}>
                      Role: {result.member.role}
                    </Text>
                  )}

                  {result.member.skills.length > 0 && (
                    <Text style={styles.detailText}>
                      Skills: {result.member.skills.join(", ")}
                    </Text>
                  )}

                  {result.member.contribution && (
                    <Text style={styles.detailText}>
                      Contribution: {result.member.contribution}
                    </Text>
                  )}

                  {result.member.feature && (
                    <Text style={styles.detailText}>
                      Feature: {result.member.feature}
                    </Text>
                  )}

                  <Text style={styles.similarityText}>
                    Similarity score: {result.similarity}
                  </Text>
                </>
              )}
            </View>
          )}
        </View>

        <View style={styles.infoCard}>
          <Text style={styles.infoTitle}>About this project</Text>
          <Text style={styles.infoText}>
            AgriSoko Pocket G06 helps visitors find group member profiles
            through a text-matching AI service using TF-IDF and cosine
            similarity. Results depend on the verified information available.
          </Text>
        </View>

        <Text style={styles.footer}>
          AgriSoko Pocket Â· G06 Â· Version 1.0.0
        </Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "#F2F7F6",
  },
  container: {
    flexGrow: 1,
    padding: 20,
    paddingTop: 32,
    width: "100%",
    maxWidth: 720,
    alignSelf: "center",
  },
  header: {
    alignItems: "center",
    marginBottom: 28,
  },
  logo: {
    width: 72,
    height: 72,
    lineHeight: 72,
    borderRadius: 22,
    overflow: "hidden",
    textAlign: "center",
    backgroundColor: "#008577",
    color: "#FFFFFF",
    fontSize: 27,
    fontWeight: "800",
    marginBottom: 14,
  },
  appName: {
    fontSize: 27,
    fontWeight: "800",
    color: "#173C37",
    textAlign: "center",
  },
  groupLabel: {
    marginTop: 9,
    color: "#008577",
    fontSize: 12,
    fontWeight: "800",
    letterSpacing: 2,
  },
  tagline: {
    marginTop: 10,
    fontSize: 15,
    color: "#5E706D",
    textAlign: "center",
  },
  card: {
    backgroundColor: "#FFFFFF",
    borderRadius: 20,
    padding: 20,
    marginBottom: 18,
    borderWidth: 1,
    borderColor: "#DFEAE7",
  },
  sectionTitle: {
    fontSize: 21,
    fontWeight: "800",
    color: "#173C37",
  },
  description: {
    marginTop: 8,
    marginBottom: 18,
    fontSize: 14,
    lineHeight: 21,
    color: "#61716E",
  },
  input: {
    borderWidth: 1,
    borderColor: "#C9D8D4",
    borderRadius: 12,
    paddingHorizontal: 14,
    paddingVertical: 14,
    fontSize: 15,
    color: "#173C37",
    backgroundColor: "#FBFDFC",
  },
  searchButton: {
    minHeight: 50,
    marginTop: 12,
    backgroundColor: "#008577",
    borderRadius: 12,
    alignItems: "center",
    justifyContent: "center",
    padding: 14,
  },
  searchButtonText: {
    color: "#FFFFFF",
    fontSize: 16,
    fontWeight: "700",
  },
  statusText: {
    marginTop: 12,
    color: "#61716E",
    textAlign: "center",
  },
  resultBox: {
    marginTop: 18,
    borderRadius: 12,
    padding: 14,
    backgroundColor: "#EAF5F2",
    borderWidth: 1,
    borderColor: "#CDE5DE",
  },
  resultTitle: {
    fontSize: 17,
    fontWeight: "800",
    color: "#17594E",
    marginBottom: 6,
  },
  resultText: {
    fontSize: 14,
    lineHeight: 21,
    color: "#315D55",
  },
  detailText: {
    marginTop: 8,
    fontSize: 14,
    lineHeight: 21,
    color: "#315D55",
  },
  similarityText: {
    marginTop: 12,
    fontSize: 12,
    color: "#61716E",
  },
  errorBox: {
    marginTop: 16,
    padding: 12,
    borderRadius: 10,
    backgroundColor: "#FCEDEC",
  },
  errorText: {
    color: "#9C302B",
    fontSize: 14,
    lineHeight: 20,
  },
  infoCard: {
    backgroundColor: "#E3EFEB",
    padding: 18,
    borderRadius: 18,
  },
  infoTitle: {
    color: "#173C37",
    fontSize: 17,
    fontWeight: "800",
    marginBottom: 8,
  },
  infoText: {
    color: "#4E6862",
    fontSize: 14,
    lineHeight: 22,
  },
  footer: {
    marginTop: 24,
    marginBottom: 16,
    textAlign: "center",
    color: "#758681",
    fontSize: 12,
  },
});


