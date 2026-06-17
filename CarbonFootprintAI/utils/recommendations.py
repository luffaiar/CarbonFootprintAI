import os
from dotenv import load_dotenv
from google.genai import Client

load_dotenv()

client = Client(
    api_key=os.getenv("AQ.Ab8RN6I_iMo0DD5b8ObOSEBNAr5emHIY-8it9qOYri96dgZvtw")
)

def ai_recommendation(score, transport, electricity, meat):

    prompt = f"""
    Carbon Score: {score}
    Transport: {transport}
    Electricity Usage: {electricity}
    Meat Consumption: {meat}

    Give 5 simple eco-friendly suggestions.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text