import streamlit as st
import pandas as pd
import os
from datetime import date
import plotly.express as px

# ===============================
# PAGE CONFIG (MUST BE FIRST)
# ===============================
st.set_page_config(
    page_title="Carbon Footprint Awareness Platform",
    page_icon="🌍",
    layout="wide"
)

# ===============================
# LOAD CSS
# ===============================
def load_css():
    if os.path.exists("style.css"):
        with open("style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ===============================
# IMPORT MODULES
# ===============================
from utils.calculator import calculate_carbon
from utils.goals import get_goal_status
from utils.pdf_report import create_pdf
from utils.recommendations import ai_recommendation

# Optional badge file
try:
    from utils.badges import get_badge
except:
    def get_badge(score):
        if score < 15:
            return "🌿 Green Hero"
        elif score < 30:
            return "🌱 Eco Warrior"
        else:
            return "♻ Carbon Fighter"

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("🌿 Eco Dashboard")

st.sidebar.markdown("""
### Features

- 🌍 Carbon Calculator
- 📈 Trend Analysis
- 🤖 AI Suggestions
- 📄 PDF Report
- 🌳 Tree Counter
- 🏆 Eco Badge
""")

# ===============================
# HERO SECTION
# ===============================
st.markdown("""
<div style="
background: linear-gradient(90deg,#14532d,#22c55e);
padding:25px;
border-radius:20px;
text-align:center;
margin-bottom:20px;
">

<h1 style="color:white;">
🌍 Carbon Footprint Awareness Platform
</h1>

<p style="color:white;font-size:18px;">
Track • Analyze • Reduce • Save the Planet
</p>

</div>
""", unsafe_allow_html=True)

# ===============================
# INPUTS
# ===============================
col1, col2 = st.columns(2)

with col1:
    transport = st.selectbox(
        "🚗 Mode of Transport",
        ["Walking", "Bicycle", "Bus", "Train", "Car"]
    )

    distance = st.number_input(
        "📍 Distance Travelled (km)",
        min_value=0.0,
        value=10.0
    )

with col2:
    electricity = st.number_input(
        "⚡ Electricity Usage (kWh)",
        min_value=0.0,
        value=5.0
    )

    meat = st.selectbox(
        "🍖 Meat Consumption",
        ["Never", "Sometimes", "Frequently"]
    )

# ===============================
# CALCULATE
# ===============================
if st.button("🌱 Calculate Carbon Footprint"):

    score = calculate_carbon(
        transport,
        distance,
        electricity,
        meat
    )

    # Sidebar score
    st.sidebar.metric("Current Score", score)

    # Carbon score
    st.success(f"🌱 Carbon Score: {score}")

    # Goal
    st.subheader("🎯 CO₂ Goal")
    st.info(get_goal_status(score))

    # Badge
    st.subheader("🏆 Eco Badge")
    st.success(get_badge(score))

    # Tree Counter
    trees_saved = max(0, int(50 - score))

    st.metric(
        "🌳 Trees Equivalent Saved",
        trees_saved
    )

    # ===============================
    # HISTORY
    # ===============================
    new_entry = pd.DataFrame({
        "Date": [str(date.today())],
        "Score": [score]
    })

    file_name = "carbon_history.csv"

    if os.path.exists(file_name):

        if os.path.getsize(file_name) > 0:

            try:
                old_data = pd.read_csv(file_name)

                history = pd.concat(
                    [old_data, new_entry],
                    ignore_index=True
                )

            except:
                history = new_entry

        else:
            history = new_entry

    else:
        history = new_entry

    history.to_csv(file_name, index=False)

    # Table
    st.subheader("📋 History")
    st.dataframe(history)

    # ===============================
    # CHART
    # ===============================
    st.subheader("📈 Carbon Trend")

    fig = px.line(
        history,
        x="Date",
        y="Score",
        markers=True,
        title="Carbon Footprint Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ===============================
    # AI RECOMMENDATIONS
    # ===============================
    st.subheader("🤖 AI Recommendations")

    try:
        response = ai_recommendation(
            score,
            transport,
            electricity,
            meat
        )

        st.write(response)

    except Exception as e:
        st.warning(f"AI unavailable: {e}")

    # ===============================
    # PDF REPORT
    # ===============================
    st.subheader("📄 Download Report")

    create_pdf(score)

    if os.path.exists("carbon_report.pdf"):

        with open("carbon_report.pdf", "rb") as file:

            st.download_button(
                label="📄 Download PDF Report",
                data=file,
                file_name="carbon_report.pdf",
                mime="application/pdf"
            )