import streamlit as st
import os
from dotenv import load_dotenv
import anthropic

# Load API key
load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

st.title("🤖 AI Resume Reviewer")

resume = st.text_area("Paste your Resume", height=250)

job = st.text_area("Paste the Job Description", height=250)

if st.button("Analyze Resume"):

    if resume.strip() == "" or job.strip() == "":
        st.warning("Please enter both the Resume and Job Description.")
    else:

        with st.spinner("Claude is analyzing your resume..."):

            prompt = f"""
You are an expert technical recruiter.

Analyze this resume against the job description.

Resume:
{resume}

Job Description:
{job}

Provide:

1. Match Score (0-100)
2. Top Strengths
3. Missing Skills
4. Resume Improvements
5. Final Verdict
"""

            response = client.messages.create(
              model="claude-haiku-4-5-20251001",
                max_tokens=2000,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.success("Analysis Complete!")

            st.write(response.content[0].text)