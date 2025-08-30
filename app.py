import streamlit as st
import requests

st.title("💊 AI Prescription Verification System")

drug = st.text_input("Enter Drug Name")

if st.button("Check Drug"):
    response = requests.post("http://127.0.0.1:8000/check_drug", params={"drug": drug})
    result = response.json()

    if "error" in result:
        st.error("Drug not found in database")
    else:
        st.success(f"Drug: {drug}")
        st.write(f"Max Dose: {result['info']['max_dose']}")
        st.write(f"Age Limit: {result['info']['age_limit']}")
        st.write(f"Alternatives: {', '.join(result['info']['alternatives'])}")
