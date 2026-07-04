import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

#==========================================
#1. ROUTE PROTECTION
#==========================================

#If the user is not in the session memory kick them back to the landing page
if "authenticated_user" not in st.session_state:
    st.warning("Unauthorized Access.Please login first")
    st.switch_page("views/landing.py")

# =========================================================
# 2. PAGE HEADER
# =========================================================

st.title("🎮 B2B Game Testing Engine")
st.markdown("*Play the game, test the mechanics, and provide high-quality feedback to boost your Aura Score!* [3, 4]")
st.markdown("---")