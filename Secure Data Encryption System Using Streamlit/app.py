import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import uuid

# Initialize Fernet key and cipher (one-time for app lifetime)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Initialize in-memory storage and state variables in session_state for persistence
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}  # {id: {"encrypted_text": ..., "passkey": ...}}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

if 'locked_out' not in st.session_state:
    st.session_state.locked_out = False

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to encrypt data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    # Find data entry with matching encrypted text and passkey hash
    for key, value in st.session_state.stored_data.items():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            # Reset failed attempts on success
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    # Increment failed attempts on failure
    st.session_state.failed_attempts += 1
    if st.session_state.failed_attempts >= 3:
        st.session_state.locked_out = True
    return None

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")
    st.write("- Store new encrypted data")
    st.write("- Retrieve your data by providing the correct passkey")
    st.write("- After 3 failed attempts, reauthorization is required")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            # Use a unique ID as key to avoid collision
            data_id = str(uuid.uuid4())
            st.session_state.stored_data[data_id] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success("✅ Data stored securely!")
            st.info(f"🔑 Your Encrypted Data (save this to retrieve later):\n\n```\n{encrypted_text}\n```")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")

    if st.session_state.locked_out:
        st.warning("🔒 Too many failed attempts! Please reauthorize through the Login page.")
    else:
        encrypted_text = st.text_area("Enter Encrypted Data:")
        passkey = st.text_input("Enter Passkey:", type="password")

        if st.button("Decrypt"):
            if encrypted_text and passkey:
                decrypted_text = decrypt_data(encrypted_text.strip(), passkey)
                if decrypted_text:
                    st.success(f"✅ Decrypted Data:\n\n{decrypted_text}")
                else:
                    attempts_left = 3 - st.session_state.failed_attempts
                    if attempts_left > 0:
                        st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")
                    else:
                        st.error("❌ Incorrect passkey! You have been locked out. Please go to Login page to reauthorize.")
            else:
                st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")

    login_pass = st.text_input("Enter Master Password:", type="password")
    if st.button("Login"):
        if login_pass == "admin123":  # Simple hardcoded password for demo
            st.session_state.failed_attempts = 0
            st.session_state.locked_out = False
            st.success("✅ Reauthorized successfully! You may now retry data retrieval.")
            # Redirect to Retrieve Data page automatically
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")

