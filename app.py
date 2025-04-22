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
    "Sales": [120,90,80,70],
    "Players":["Babar","Rizwan","F.Zaman","Ahmed"],
    "Scores":[3000,8000,6000,5000]
}
df = pd.DataFrame(data)
st.subheader("Data")
st.dataframe(df)
st.subheader("Datax")

# fig, ax = plt.subplots() #figure ax variables
# ax.bar(df["Product"],df["Sales"])
# ax.set_ylabel("Sales")
# ax.set_title("Sales of Fruits")
# st.pyplot(fig) 
fig, ax = plt.subplots()
ax.bar(df["Players"],df["Scores"])
ax.set_ylabel("Runs")
ax.set_title("Players Performance")
st.pyplot(fig)

st.title("Excel file uploader")

uf = st.file_uploader("Upload File", type=["xlsx"])
if uf is not None:
    df = pd.read_excel(uf)

    st.subheader("Excel Data")
    st.dataframe(df.head(5))
else:
    st.info("please upload excel file .xlsx")

fig, ax = plt.subplots()
ax.bar(df["Products"],df["UnitPrice"])
ax.set_ylabel("Devices")
ax.set_xlabel("Product Prices")
ax.set_title("Devices")
st.pyplot(fig)