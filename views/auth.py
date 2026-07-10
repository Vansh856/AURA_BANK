import streamlit as st
import requests
st.title("🔐 Authentication Gateway")

#=========================================================
#1. Fetch User's Intention from the Landing page
#=========================================================

initial_mode=st.session_state.get("Auth_mode","Login")
Auth_index=0 if initial_mode=="Login" else 1

#==============================================================================
#2. using radio button instead of tabs to use indexing
#==============================================================================

auth_mode = st.radio("Select Mode", ["Login", "Register"], index=Auth_index, horizontal=True, label_visibility="collapsed")

# ==========================================
# 3: LOGIN PIPELINE
# ==========================================

if auth_mode=="Login":
    st.subheader("Welcome Back!")
    login_Username=st.text_input("Enter your username",key="log_user")
    login_Password=st.text_input("Enter your password",type="password",key="log_pass")
    if st.button("Login"):
        if login_Username and login_Password:
            try:
                payload={"username":login_Username,"password":login_Password}
                response = requests.post("http://127.0.0.1:8000/login", json=payload)
                if response.status_code==200:
                    st.success("Login Successful.Welcome to Aura Bank")
                    st.session_state["authenticated_user"] = login_Username
                    st.switch_page("views/dashboard.py")

                else:
                    error_data=response.json()
                    error_message=error_data.get("detail","Invalid username or password")
                    st.error(error_message)

            except Exception as e:
                # 5. Handle cases where the FastAPI server is not running
                st.error("Backend server is offline. Please start FastAPI.")
        else:
            st.warning("Please fill in both the username and password fields.")

# ==========================================
#4. registration pipeline
# ==========================================
elif auth_mode=="Register":
    st.subheader("Create an Aura Bank Account")
    reg_Username=st.text_input("Choose an UserName",key="reg_user")
    reg_Password=st.text_input("Choose a Password",type="password",key="reg_pass")
    if st.button("Register"):
        if reg_Username and reg_Password:
            try:
                payload={"username":reg_Username,"password":reg_Password}
                response=requests.post("http://127.0.0.1:8000/register", json=payload)

                if response.status_code==200:
                    st.success("Registration successful! You can now log in")

                else:
                    error_data=response.json()
                    error_message=error_data.get("detail","REGISTRATION FAILED DUE TO AN UNKNOWN ERROR")
                    st.error(   error_message)
            except Exception as e:
                st.error("Backend server is offline. Please start FastAPI.")
        else:
            st.warning("Please fill in all feilds.")