import streamlit as st
import numpy as np
import pickle
import os
st.set_page_config(layout="wide")

st.markdown("""
    <style>
        .block-container {
            padding-left: 2rem;
            padding-right: 2rem;
            max-width: 100%;
        }
    </style>
""", unsafe_allow_html=True)
# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))

st.title("🚬 Smoking Prediction App")

# =========================
# 👨‍💻 ADD YOUR DETAILS HERE
# =========================
st.info("""
👨‍💻 Developer: Amrutha P 
🎓 Role: Data Science / ML Engineer  
📊 Project: Smoking Prediction using Machine Learning  
""")

# =========================
# 👤 GROUP 1: BASIC INFO
# =========================
st.header("👤 Basic Information")

age = st.number_input("Age", min_value=1, max_value=100, step=1)

weight = st.number_input("Weight (kg)", min_value=20, max_value=150, step=1)

waist = st.number_input("Waist (cm)", min_value=20, max_value=150, step=1)

# =========================
# 🩸 GROUP 2: BLOOD TEST
# =========================
st.header("🩸 Blood Test Results")

ast = st.number_input(
    "AST",
    value=20.0,
    step=0.1,
    help="Liver enzyme level (normal range ~10–40 U/L)"
)

alt = st.number_input(
    "ALT",
    value=20.0,
    step=0.1,
    help="Liver enzyme level (normal range ~7–56 U/L)"
)

gtp = st.number_input(
    "GTP",
    value=20.0,
    step=0.1,
    help="Gamma-GTP enzyme (high values may indicate alcohol/smoking impact)"
)

hemoglobin = st.number_input("Hemoglobin", value=14.0, step=0.1)

# =========================
# 🦷 GROUP 3: ORAL HEALTH
# =========================
st.header("🦷 Oral Health")

tartar = st.selectbox("Tartar", ["No", "Yes"])
tartar = 1 if tartar == "Yes" else 0

caries = st.selectbox("Dental Caries", ["No", "Yes"])
caries = 1 if caries == "Yes" else 0

oral = st.selectbox("Oral Condition", ["Normal", "Bad"])
oral = 1 if oral == "Bad" else 0

# =========================
# 📦 INPUT ARRAY
# =========================
input_data = np.array([[
    age,
    weight,
    waist,
    gtp,
    alt,
    ast,
    hemoglobin,
    tartar,
    caries,
    oral
]])

# =========================
# 🚀 PREDICTION
# =========================
if st.button("Predict"):

    proba = model.predict_proba(input_data)[0][1]

    if proba >= 0.4:
        st.error(f"🚬 Smoker Detected (Risk Score: {proba:.2f})")

        st.warning("""
        ⚠️ Health Advice:
        - Smoking increases risk of lung disease
        - It affects liver (GTP, ALT, AST)
        - It reduces oxygen levels in blood

        💡 Suggestion:
        Consider reducing or quitting smoking for better health.
        """)

    else:
        st.success(f"✅ Non-Smoker (Risk Score: {proba:.2f})")

        st.info("""
        🎉 Great Job!

        💪 Keep maintaining your healthy lifestyle
        - Continue regular exercise
        - Maintain good diet
        - Stay away from smoking habits
        """)
