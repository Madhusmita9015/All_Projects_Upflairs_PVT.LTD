🔑 Get Your OpenAI API Key
To use this app, you must have your own OpenAI API key.

👉 Steps to Generate Your Key:
Go to https://platform.openai.com/account/api-keys

Click "Create new secret key"

Copy the key (starts with sk-...)

In your project folder, create a file named .env

Inside .env, paste this line:

env
Copy code
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
⚠️ Keep this file private. Never upload your .env or API key to GitHub.



# 📄 Resume & Job Match Analyzer (GPT-Powered)

A Streamlit web app that analyzes how well a resume matches a job description using OpenAI's GPT-3.5. It gives:
- A match score out of 100
- Matching & missing skills
- Suggestions to improve resume
- A custom cover letter

## 🔧 Tech Stack
- Python 3.10
- Streamlit
- OpenAI GPT-3.5
- PyMuPDF (`fitz`)

## 🚀 How to Run

```bash
pip install streamlit openai pymupdf
streamlit run resume_match_streamlit_app.py
