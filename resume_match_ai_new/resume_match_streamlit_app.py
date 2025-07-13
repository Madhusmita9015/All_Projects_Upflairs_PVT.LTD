import streamlit as st
import fitz 
import openai
openai.api_key = "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"  

# Function to extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"


def analyze_resume(resume_text, job_text):
    prompt = f"""
Here is a resume:
---
{resume_text}
---

Here is a job description:
---
{job_text}
---

Based on the job description, provide:
1. Match score out of 100
2. List of matching skills
3. List of missing or weak areas
4. Suggestions to improve the resume
5. A custom cover letter tailored for the job
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error from OpenAI: {e}"

# --- Streamlit UI ---
st.set_page_config(page_title="Resume Match Bot", layout="centered")
st.title("📄 Resume & Job Match Analyzer (Powered by GPT-3.5)")

resume_file = st.file_uploader("📎 Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("📝 Paste the Job Description")

if resume_file and job_description:
    with st.spinner("Analyzing... please wait ⏳"):
        resume_text = extract_text_from_pdf(resume_file)
        if resume_text.startswith("Error"):
            st.error(resume_text)
        else:
            result = analyze_resume(resume_text, job_description)
            st.success("✅ Analysis Complete!")
            st.markdown(result)
