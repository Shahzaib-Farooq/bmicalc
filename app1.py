import streamlit as st
import pandas as pd

st.title("BMI Calculator")
weight = st.number_input("Enter your weight in (kg)")
height = st.number_input("Enter your height in (m)")

if height > 0:
    bmi = weight/(height**2)
    st.write(f"Your BMI is {bmi}")
