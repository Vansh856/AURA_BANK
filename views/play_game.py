import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# Import our static game bundles from our new helper module!
from views.games_bundle import GAMES

# =========================================================
# 1. ROUTE PROTECTION (Security First)
# =========================================================

# login bypass protection
if "authenticated_user" not in st.session_state:
    st.warning("Unauthorized Access. Please login first.")
    st.switch_page("views/landing.py")

current_user = st.session_state["authenticated_user"]

#timer bypass protection 
if not st.session_state["test_started"]:
    st.warning("Please select the game first")
    st.switch_page("views/game_testing.py")

# =========================================================
#2.  RENDER RETRO GAME CONTAINER (SANDBOXED)
# =========================================================
# 2.1. Fetch the raw HTML string of the chosen game from our bundle
game_html = GAMES[st.session_state["selected_game"]]

# 2.2. Render the sandboxed iframe component
components.html(game_html, height=600, scrolling=False)

#================================================================
#2. GAME TERMINATION AND GAMETIME CALCULATION LOGIC
#================================================================

if st.button("⏹️ End Test & Submit Feedback"):
    #stores the endtime
    end_datetime = datetime.now()
        
    #gives the difference between two 
    duration = end_datetime - st.session_state["start_time"]
        
    #calculates the total seconds 
    total_seconds = duration.total_seconds()

    #save the playtime
    st.session_state["playtime_minutes"]=total_seconds/60
    st.session_state["test_started"]=False
    st.session_state["show_feedback_form"]=True
    st.switch_page("views/feedback.py")