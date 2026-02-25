import streamlit as st

# 1. Title stays in the main area
st.title("💰 Professional Tip Calculator")

# 2. Add a header to the sidebar
st.sidebar.header("⚙️ Settings")

# 3. Move inputs to the sidebar by adding '.sidebar'
bill = st.sidebar.number_input("How much was the bill?", min_value=0.00)
tip_percentage = st.sidebar.slider("Tip Percentage", 0, 30, 15)

# 4. Logic (Math) stays the same
tip_amount = bill * (tip_percentage / 100)
total = bill + tip_amount

# 5. Display results in the main area (Clean & Big)
st.write("### 🧾 Your Receipt")  # '###' makes it a sub-header

if bill > 0:
    # Use columns to show results side-by-side
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"Tip Amount:")
        st.info(f"${tip_amount:.2f}") # .info makes it blue

    with col2:
        st.write(f"Total to Pay:")
        st.success(f"${total:.2f}") # .success makes it green
else:
    st.write("👈 *Enter the bill amount in the sidebar to start.*")
