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
#2. SESSION STATE INITIALIZER
#=========================================

#on off switch for gameplay sandbox
if "test_started" not in st.session_state:
    st.session_state["test_started"]=False

#on off button for post game feedback form
if "show_feedback_form" not in st.session_state:
    st.session_state["show_feedback_form"]=False

# Check which build the user is actively testing
if "selected_game" not in st.session_state:
    st.session_state["selected_game"] = "2048"

# High-precision timer start timestamp (None until play is clicked)
if "start_time" not in st.session_state:
    st.session_state["start_time"] = None

# Stores calculated playtime duration in minutes
if "playtime_minutes" not in st.session_state:
    st.session_state["playtime_minutes"] = 0.0

# =========================================================
# 2. STATE A: THE LOBBY BUILD SELECTOR
# =========================================================
if not st.session_state["test_started"]:
    st.title("🎮 B2B Game Testing Engine")
    st.session_state["selected_game"] = st.selectbox(
    "Choose Game Sandbox:",
    options=["2048", "Snake", "Tic-Tac-Toe"]
)
    
    if st.button("▶️ Start Beta Test Session", type="primary", use_container_width=True):
        st.session_state["test_started"] = True
        st.session_state["start_time"] = datetime.now()
        st.switch_page("views/play_game.py")  # Target the View, not the data bundle

# OUTSIDE the lobby block: This is evaluated if lobby is skipped
elif st.session_state["test_started"]:
    st.switch_page("views/play_game.py") 

