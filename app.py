# import streamlit as st
# st.title("Simple Calculator")
# a = st.number_input("Enter first number")
# b = st.number_input("Enter second number")
# operation = st.selectbox("opetationa",["Add","Subtract","Multiply","Divide"])
# if operation == "Add":
#     result = a +b
# elif operation == "Subtract":
#     result = a -b
# elif operation == "Multiply":
#     result = a * b
# elif operation == "Divide":
#     result = a / b

# st.write("Result =",result)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Data Visualization / Chart")

data = {
    "Product": ["rafay","Umer","adil","huzaifa"],
    "Sales": [120,90,80,70]
}
df = pd.DataFrame(data)
st.subheader("Data")
st.dataframe(df)
st.subheader("Datax")

fig, ax = plt.subplots()
ax.bar(df["Product"],df["Sales"])
ax.set_ylabel("Sales")
ax.set_title("Sales of Fruits")
st.pyplot(fig)