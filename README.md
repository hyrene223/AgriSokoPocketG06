\# AgriSoko Pocket — Group G06



\## Project Overview

AgriSoko Pocket is a React Native mobile application connected to a Python FastAPI backend. It uses TF-IDF text representation and cosine similarity to match user queries against approved team-member information.



\## Group Members



| Name | Registration Number |

|---|---|

| Nsabimana Irene | 25/27790 |

| Uwimbabazi Aimerance | 25/28028 |

| Ishimwe Alphaxad | 25/27565 |

| Muram Yaser | 25/28164 |

| Umutoniwase Alice | 25/28026 |

| Doris Kelly | 24/23813 |



Actual contributions must be confirmed by each group member.



\## Repository

https://github.com/hyrene223/AgriSokoPocketG06



\## Project Structure

\- `mobile/` — React Native and Expo application.

\- `ai-api/` — FastAPI backend, matching logic, member data, and tests.

\- `build/` — Final Android APK.

\- `docs/` — Project documentation and report.

\- `evidence/` — Test logs, contributions, feedback, AI-use declaration, and demo evidence.



\## Run the Backend

From the project root, open PowerShell and run:



```powershell

cd ai-api

.\\.venv\\Scripts\\python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000

```



The backend listens on port 8000. A mobile device must be able to reach the computer's network address, and the mobile app must use the correct API URL.



\## Backend Endpoints

\- `GET /health`

\- `GET /model-info`

\- `POST /search`



\## Run Backend Tests

From the project root:



```powershell

cd ai-api

.\\.venv\\Scripts\\python.exe -m pytest -q

```



Latest recorded result: \*\*7 passed, 1 warning\*\*. Run the tests again before submission and preserve evidence of the actual output.



\## Build the Android Application

From the project root:



```powershell

cd mobile

npx.cmd eas-cli build --platform android --profile preview

```



After the cloud build finishes successfully, download the APK and place it at:



`build/AgriSokoPocket\_G06.apk`



\## Documentation and Evidence

The final submission must include the required project report, actual group contributions, test log, tester feedback, AI-use declaration, and demonstration video in the required formats and locations.



\## Limitations

\- Text similarity does not guarantee a correct match.

\- Member information must be checked against approved records.

\- The API URL must be reachable from the mobile device.

\- Backend tests alone do not prove that every mobile feature works correctly.

\- Contributions, signatures, feedback, and device test results must reflect genuine evidence.



\## Last Known Commit

`cf6b3a0` — Fix mobile AI backend connection.



Verify the latest commit and final APK before creating the submission ZIP.

