import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# Import our static game bundles from our new helper module!
from views.games_bundle import GAMES

# =========================================================
# 1. ROUTE PROTECTION (Security First)
# =========================================================
if "authenticated_user" not in st.session_state:
    st.warning("Unauthorized Access. Please login first.")
    st.switch_page("views/landing.py")

current_user = st.session_state["authenticated_user"]

#=========================================
#SESSION STATE INITIALIZER
#=========================================

#on off switch for gameplay sandbox
if "test_started" not in st.session_state:
    st.session_state["test_started"]=False

#on off button for post game feedback form
if "show_feedback_form" not in st.session_state:
    st.session_state["show_feedback_form"]=False

#check which built the user is actively testing
if "select_game" not in st.session_state:
st.session_state[]
