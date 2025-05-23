import streamlit as st


st.set_page_config(page_title="BMI Calculator", page_icon="💪")
st.title("💪 BMI Calculator")
st.write("Enter your height and weight to calculate your Body Mass Index (BMI).")

# Inputs
user_height_cm = st.number_input("Height (in centimeters):", min_value=30.0, format="%.1f")
user_weight_kg = st.number_input("Weight (in kilograms):", min_value=1.0, format="%.2f")

# BMI Calculation
if st.button("Calculate BMI"):
    if user_height_cm > 0 and user_weight_kg > 0:
        height_m = user_height_cm / 100  # Convert cm to meters
        bmi_result = user_weight_kg / (height_m ** 2)
        st.success(f"Your BMI is: {bmi_result:.2f}")

         # Category
        if bmi_result < 18.5:
            st.warning("You are considered underweight.")
        elif 18.5 <= bmi_result < 24.9:
            st.success("Your weight is within the normal range.")
        elif 25 <= bmi_result < 29.9:
            st.info("You fall into the overweight category.")
        else:
            st.error("You are classified as obese. ⚠️ Please consider consulting a healthcare professional.")
    else:
        st.error("Make sure to input valid height and weight values.")