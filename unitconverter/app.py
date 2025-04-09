import streamlit as st

#page setting
st.set_page_config(page_title="Unit Converter", layout="centered")

# Title
st.title("Unit Converter")
st.write("#### Convert between Length, Weight and Temperature")

st.divider()

#conversion type choose
conversion_type = st.selectbox("Choose conversion category:", ["Length", "Temperature", "Weight"])

col1, col2 = st.columns(2)


# Length 
if conversion_type == "Length":
    st.subheader("Length Converter")

    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Inches": 0.0254,
        "Feet": 0.3048,
        "Yards": 0.9144,
        "Miles": 1609.34
    }

    with col1:
        from_unit = st.selectbox("From", units.keys())
    with col2:
        to_unit = st.selectbox("To", units.keys())

    value = st.number_input("Enter length:", value=0.0, min_value=0.0, step=0.1)


    if st.button("Convert"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        st.caption(f"Formula: {value} × ({units[from_unit]} / {units[to_unit]})")



# Weigth
elif conversion_type == "Weight":
    st.subheader("Weight Converter")

    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    with col1:
        from_unit = st.selectbox("From", units.keys())
    with col2:
        to_unit = st.selectbox("To", units.keys())

    value = st.number_input("Enter weight:", value=0.0, min_value=0.0, step=0.1)


    if st.button("Convert"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        st.caption(f"Formula: {value} × ({units[from_unit]} / {units[to_unit]})")



#Temperature
elif conversion_type == "Temperature":
    st.subheader("Temperature Converter")

    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

    value = st.number_input("Enter temperature:", value=0.0, step=0.1)

    def convert_temp(v, f, t):
        if f == t:
            return v
        if f == "Celsius":
            return v + 273.15 if t == "Kelvin" else v * 9/5 + 32
        if f == "Fahrenheit":
            return (v - 32) * 5/9 if t == "Celsius" else (v - 32) * 5/9 + 273.15
        if f == "Kelvin":
            return v - 273.15 if t == "Celsius" else (v - 273.15) * 9/5 + 32

    if st.button("Convert"):
        result = convert_temp(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

    #Formula
        if from_unit == to_unit:
            st.caption("Formula: No conversion needed.")
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            st.caption("Formula: (°C × 9/5) + 32")
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            st.caption("Formula: (°F - 32) × 5/9")
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            st.caption("Formula: °C + 273.15")
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            st.caption("Formula: K - 273.15")
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            st.caption("Formula: ((°F - 32) × 5/9) + 273.15")
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            st.caption("Formula: ((K - 273.15) × 9/5) + 32")
