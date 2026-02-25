import streamlit as st

st.title("💰 Simple Tip Calculator")

bill = st.number_input("How much was the bill?", min_value=0.00)
tip_percentage = st.slider("Select tip percentage", 0, 30, 15)

tip_amount = bill * (tip_percentage / 100)
total = bill + tip_amount

if bill > 0:
    st.write(f"Tip amount: ${tip_amount:.2f}")
    st.success(f"Total to pay: ${total:.2f}")