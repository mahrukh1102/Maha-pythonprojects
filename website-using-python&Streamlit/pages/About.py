import streamlit as st
from components.navbar import navbar
from components.footer import footer

navbar()

st.title(" About Me")
st.write("""
## Hi! I'm Mahrukh, a Python developer.  
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
""")

footer()
