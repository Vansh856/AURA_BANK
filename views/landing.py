import streamlit as st
import requests
st.image("assets/banner.png", link="https://github.com")
st.title(" :green[AURA BANK 🏦]")
st.markdown("*The Financialization of Engagement Data*")
st.markdown("---")
col1,col2=st.columns(2)
with col1:
    if st.button("Go to Login"):
        st.session_state["Auth_mode"]="Login"
        st.switch_page("views/auth.py")
with col2:
    if st.button("Go to Register"):
        st.session_state["Auth_mode"]="Register"
        st.switch_page("views/auth.py")

st.text("")
col3,col4=st.columns(2)
with col3:
    st.page_link("views/contact.py",label="contact",icon="🔗")
    st.text("""
    
    
    """)
with col4:
    st.page_link("views/about.py",label="ABOUT US",icon="🔗")

    