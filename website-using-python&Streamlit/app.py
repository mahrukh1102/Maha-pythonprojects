import streamlit as st
from components.navbar import navbar
from components.footer import footer

st.set_page_config(page_title="My Website", layout="wide")

navbar()

st.title("Welcome to My Website")

col1, = st.columns(1)

with col1:
    st.header(" Hello There!")
    st.write("""
        I Made this Responsive, interactive , Clean website with following features.
    """)



st.markdown("### Features")
st.markdown("- Custom navigation bar\n- Responsive layout\n- Contact form with validation\n- Multipage support\n- Reusable components")

footer()
