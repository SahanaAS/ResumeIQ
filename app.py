import streamlit as st

st.title("ResumeIQ")
st.subheader("AI Resume Reviewer")

resume = st.text_area(
    "Paste your Resume",
    height=250
)

job = st.text_area(
    "Paste the Job Description",
    height=250
)

if st.button("🚀 Analyze Resume"):

    if resume.strip() == "" or job.strip() == "":
        st.warning("⚠️ Please paste both your resume and the job description.")

    else:

        st.success("Resume received successfully!")

        st.divider()

        st.header("📊 Analysis Results")

        st.metric(
            label="Resume Match Score",
            value="Coming Soon..."
        )

        st.subheader("💪 Strengths")
        st.info("Claude will identify your strengths here.")

        st.subheader("📚 Missing Skills")
        st.info("Claude will list missing skills here.")

        st.subheader("📈 Suggested Improvements")
        st.info("Claude will suggest improvements here.")

        st.subheader("🎤 Interview Questions")
        st.info("Claude will generate interview questions here.")