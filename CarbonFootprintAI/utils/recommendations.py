import os
from dotenv import load_dotenv
from google.genai import Client
import streamlit as st

# Load local .env file (works locally)
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI API KEY")

# If running on Streamlit Cloud, use Secrets
if not api_key:
    try:
        api_key = st.secrets["GEMINI API KEY"]
    except:
        api_key = None


def ai_recommendation(score, transport, electricity, meat):

    if not api_key:
        return "⚠️ Gemini API key not configured."

    client = Client(api_key=api_key)

    prompt = f"""
    Carbon Score: {score}

    Transport: {transport}
    Electricity Usage: {electricity} kWh
    Meat Consumption: {meat}

    Provide 5 practical and easy eco-friendly recommendations
    to help reduce the user's carbon footprint.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"⚠️ AI Recommendation Error: {e}"
