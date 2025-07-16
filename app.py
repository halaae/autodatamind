import streamlit as st
import pandas as pd
from modules.eda_engine import run_eda
from modules.ml_engine import run_ml
from modules.report_generator import generate_pdf_report
from modules.email_sender import send_email

st.set_page_config(page_title="AutoDataMind", layout="wide")
st.title("🤖 AutoDataMind - Your Autonomous AI Data Scientist")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your CSV data", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Preview of Dataset")
    st.dataframe(df)

    with st.expander("🔍 Run Exploratory Data Analysis"):
        run_eda(df)

    with st.expander("🧠 Run Machine Learning"):
        run_ml(df)

    # PDF Report
    if st.button("📄 Generate PDF Report"):
        try:
            generate_pdf_report(df, "Model has been trained and evaluated.")
            st.success("✅ Report generated and saved to outputs/report.pdf")
        except Exception as e:
            st.error(f"❌ Failed to generate report: {e}")

    # Email automation
    email = st.text_input("✉️ Enter your email to receive the report")
    if st.button("📬 Send Report via Email"):
        if email:
            try:
                send_email(
                    receiver_email=email,
                    subject="Your AutoDataMind Report",
                    body="Hi! Here's your automated data analysis report from AutoDataMind.",
                    attachment_path="outputs/report.pdf"
                )
                st.success(f"📨 Report sent to {email}")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
        else:
            st.warning("⚠️ Please enter a valid email.")

