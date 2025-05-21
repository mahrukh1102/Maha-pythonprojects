import streamlit as st
import re
import random

#password strength check func

blacklist = ['password', '123456', 'qwerty', 'pakistan123', 'karachi123', 'admin', 'password123', 'abc123']

def check_password_strength(password):
    score = 0
    suggestions = []

    if password.lower() in blacklist:
        return 0, ["🚫 This one's way too common. Try something unique."]

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("🔹 At least 8 characters")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("🔹 Include both UPPERCASE and lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("🔹 Add at least one digit (0-9)")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("🔹 Include one special character (!@#$%^&*)")

    return score, suggestions




def generate_strong_password(length=12):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*"
    all_chars = upper + lower + digits + special

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

#page config

st.set_page_config("🔐 Password Strength Meter", layout="centered")

custom_css = """
<style>
    .main { background-color: #F6F8FA; padding-top: 2rem; }
    h1, h3, .stButton>button {
        font-family: 'Segoe UI', sans-serif;
    }
    .strength-bar {
        height: 10px;
        border-radius: 10px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

#UI sec

st.title("🔐 Password Strength Meter")
st.write("###### Enter a password below to see how secure it is — or generate a strong one instantly.")

password = st.text_input("🔑 Enter your password", type="password")
check_clicked = st.button("✅ Check Password")

if check_clicked and password:
    score, tips = check_password_strength(password)

    st.subheader("🧪 Strength Analysis")

    strength_labels = {
        0: ("Very Weak", "❌", "#e74c3c"),
        1: ("Weak", "⚠️", "#e67e22"),
        2: ("Moderate", "🟠", "#f1c40f"),
        3: ("Good", "🟢", "#2ecc71"),
        4: ("Strong", "✅", "#27ae60")
    }

    label, emoji, color = strength_labels.get(score, ("Unknown", "", "#bdc3c7"))
    st.markdown(f"**{emoji} Strength: {label}**")

#Strength bar
    st.markdown(f"""
    <div class="strength-bar" style="width: 100%; background-color: #eee;">
        <div style="width: {score * 25}%; background-color: {color};" class="strength-bar"></div>
    </div>
    """, unsafe_allow_html=True)

    if score < 4:
        st.markdown("### 🔧 Suggestions:")
        for tip in tips:
            st.markdown(f"- {tip}")
    else:
        st.success("Your password is strong! 🔐")

elif check_clicked and not password:
    st.warning("Please enter a password before checking.")

st.markdown("---")

#Generator

st.subheader("🛠️ Need Help Creating One?")

with st.expander("Customize Password Generator"):
    length = st.slider("Password Length", 8, 20, 12)

if st.button("🎲 Generate Password"):
    strong_pass = generate_strong_password(length)
    st.code(strong_pass, language="text")
    st.success("Here’s a strong password you can use!")
st.markdown("---")

