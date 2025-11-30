# 🏀 NBA GPT Assistant – 
AWS Serverless Chatbot (OpenAI + API Gateway + Lambda + Streamlit)

This project builds a **real NBA Q&A chatbot** using a fully serverless AWS backend and a Streamlit front-end.
You can ask natural questions about NBA players, teams, seasons, and history — and the assistant responds conversationally using OpenAI GPT.

This README documents ONLY the **AWS NBA Project**.

------------------------------------------------------------
## 🔧 Architecture Overview (AWS + OpenAI + Streamlit)
------------------------------------------------------------

User → Streamlit Web App (src/app/app.py)
      → POST /ask
      → API Gateway (HTTP API)
      → Lambda (nba_gpt_lambda)
      → OpenAI GPT (gpt-4o-mini)
      ← Response JSON
      ← Streamlit renders chat

Services Used:
- AWS Lambda → Chatbot backend
- AWS API Gateway (HTTP API) → /ask endpoint
- AWS CloudShell → Testing + debugging
- Amazon S3 → Curated NBA datasets
- OpenAI API → GPT inference
- Streamlit → Chat UI
- AWS- S3 - Save raw and clean data
- IAM-  for role in AWS
- Amazon Bedrock - access clud LLM and Embedding
- Athena - to check RDBM relations in dara
- CloudShell - to find out the error in the pyhton code and check API access port
- 

------------------------------------------------------------
## 📁 Final Project Structure (NBA Project Only)
------------------------------------------------------------

NBA_project/
├─ data/
│  └─ curated/
│     ├─ players_cleaned

│     └─ teams_cleaned

│        └─ date=2025-11-10
├─ src/
│  ├─ app/
│  │  └─ app.py                
│  │
│  ├─ lambda/
│  │  └─ nba_gpt_lambda/
│  │     └─ lambda_function.py 
│  │
│  ├─ etl/                    
│  ├─ features/                
│  ├─ models/                  
│  └─ dashboard/                
│
├─ .env                        
└─ README.md

------------------------------------------------------------
## 🧠 AWS Lambda – nba_gpt_lambda
------------------------------------------------------------

Handler:
lambda_function.lambda_handler

Lambda Responsibilities:
- Parse incoming question from:
    event["body"] (API Gateway)
    OR direct test {"question": "..."}
- Send request to OpenAI Chat Completions (gpt-4o-mini)
- Return JSON response:

{
  "statusCode": 200,
  "body": "{\"question\": \"...\", \"answer\": \"...\"}"
}

Environment Variables Required:
OPENAI_API_KEY=<your-key>

------------------------------------------------------------
## 🌐 AWS API Gateway – /ask Endpoint
------------------------------------------------------------

Type: HTTP API  
Method: POST  
Route: /ask  
Stage: prod  
Integration: Lambda Proxy → nba_gpt_lambda  

Example Endpoint:
https://<your-api-id>.execute-api.us-east-1.amazonaws.com/prod/ask

Test using CloudShell:

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"question": "Tell me about Stephen Curry"}' \
  "https://<your-api-id>.execute-api.us-east-1.amazonaws.com/prod/ask"

Expected response:
{"question":"...","answer":"..."}

------------------------------------------------------------
## 🎨 Streamlit App – src/app/app.py
------------------------------------------------------------

Features:
- Dark UI
- Title: "NBA GPT Assistant"
- Chat bubbles for Q&A
- Input text box
- Sends POST to API Gateway
- Session-state chat history

.env file:

API_URL=https://<your-api-id>.execute-api.us-east-1.amazonaws.com/prod/ask

Run locally:

cd NBA_project/src/app
streamlit run app.py

Open browser:
http://localhost:8501

Example Question:
who won the nba champion in 2014

GPT Example Response:
The San Antonio Spurs won the NBA Championship in 2014…

------------------------------------------------------------
## 🧪 Testing Checklist
------------------------------------------------------------

✔ Lambda Test  
Use {"question": "Who is LeBron James?"}

✔ API Gateway Test  
POST /ask ↓  
{"question": "Tell me about Kobe Bryant"}

✔ End-to-End  
Run Streamlit → Chat end-to-end

------------------------------------------------------------
## 🔐 Required Secrets
------------------------------------------------------------

Lambda:
OPENAI_API_KEY=<your-key>

Local .env:
API_URL=<your-gateway-url>

------------------------------------------------------------
## 📌 AWS Services Used (NBA Project Only)
------------------------------------------------------------

- AWS Lambda  
- API Gateway  
- CloudShell  
- Amazon S3  
- OpenAI (GPT)  
- Streamlit  

------------------------------------------------------------
## 🚀 Future Improvements
------------------------------------------------------------


- Add Cognito authentication
- Deploy Streamlit on EC2 or Streamlit Cloud
