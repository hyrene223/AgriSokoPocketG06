# AgriSoko Pocket G06 — Technical Report

## 1. Project Overview
AgriSoko Pocket is a group project designed to help users discover team members and their verified skills through a mobile interface and an AI-powered text-matching service.

Group: G06  
Application: AgriSoko Pocket  
Version: 1.0.0

## 2. Objectives
- Provide a mobile interface for searching team-member information.
- Match search queries against approved member records.
- Return a suitable member when the similarity is sufficient.
- Avoid inventing member information when no suitable match is found.
- Validate the AI service using automated tests.

## 3. System Architecture
The system consists of a React Native application built with Expo and a Python FastAPI backend. The mobile application sends search requests to the backend, which performs text matching and returns a response containing match information.

The backend provides:
- GET /health
- GET /model-info
- POST /search

The mobile interface displays the result, available member details, similarity score, or an error message.

## 4. AI Matching Approach
The project uses TF-IDF text representation and cosine similarity to compare a user's query with available team-member information. A similarity threshold is used to determine whether a result is suitable.

The system's reliability depends on the quality and completeness of the approved member records. A similarity score is not proof that information is correct.

## 5. Mobile Application
The current mobile screen provides a search input, a search button, loading feedback, result details, error handling, and project information. The app is configured for Android builds through Expo Application Services (EAS).

## 6. Testing
The backend automated test suite was run using pytest. The latest recorded result was:

7 passed, 1 warning, 0 failed.

The warning concerned Starlette's test-client integration with httpx. This result confirms the tests passed in that run; it does not establish that every mobile or deployment requirement has been verified.

## 7. Limitations and Responsible Use
- Member information must be verified before being added to the approved records.
- Text similarity can return incorrect or incomplete matches.
- The mobile application's API address must be configured for the deployment environment.
- The system should not invent missing member facts.
- Search results should be checked against approved information.
- Testing the backend alone does not verify the complete Android application.

## 8. Conclusion
AgriSoko Pocket G06 combines a mobile search interface with an AI text-matching backend. Further verification should cover Android installation, mobile-to-backend connectivity, all required assignment features, and the final submission evidence.

## 9. Evidence to Attach
- Android APK and installation evidence.
- Backend test log.
- Screenshots of successful and unsuccessful searches.
- Feedback evidence.
- Group contribution record.
- AI-use declaration.
- Continuous demonstration video of no more than three minutes.
