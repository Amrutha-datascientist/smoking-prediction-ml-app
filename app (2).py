import streamlit as st
import numpy as np
import pickle

# Load model
import os
import pickle

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

age = st.number_input("Age")
weight = st.number_input("Weight (kg)")
waist = st.number_input("Waist (cm)")

# =========================
# 🩸 GROUP 2: BLOOD TEST
# =========================
st.header("🩸 Blood Test Results")

gtp = st.number_input("GTP Level")
alt = st.number_input("ALT Level")
ast = st.number_input("AST Level")
hemoglobin = st.number_input("Hemoglobin")

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
# 📦 INPUT ARRAY (IMPORTANT ORDER)
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
