import streamlit as st

# =========================================================
# 1. ROUTE PROTECTION (Security First)
# =========================================================

# login bypass protection
if "authenticated_user" not in st.session_state:
    st.warning("Unauthorized Access. Please login first.")
    st.switch_page("views/landing.py")
if not st.session_state["show_feedback_form"]:
    st.warning("Firstly play the game")
    st.switch_page("views/game_testing.py")

#=============================================================
#2. PLAYED GAME DATA
#=============================================================

played_game=st.session_state["selected_game"]
play_time=st.session_state["playtime_minutes"]


#==============================================================
#3. HEADER
#==============================================================

st.title("B2B Telemetry Portal.")
st.info("As of now you have played the game and now its time for the Aura Farming ")
with st.container(border=True):
    st.subheader("Your Gameplay Data")
    st.markdown(f"GAME PLAYED:- {played_game}")
    st.markdown(f"PLAY TIME:- {play_time:.2f} minutes")

with st.form("my_form_key"):
    gameplay_feedback,graphics_feedback=st.columns(2)
    performance_feedback,audio_feedback=st.columns(2)
    with gameplay_feedback:
        gameplay_rating = st.slider("Rate the gameplay", 1, 5,key="gameplay")
    with graphics_feedback:
        graphics_rating = st.slider("Rate the graphics", 1, 5,key="graphics")
    with performance_feedback:
        performance_rating = st.slider("Rate the game", 1, 5,key="performance")
    with audio_feedback:
        audio_rating = st.slider("Rate the game", 1, 5,key="audio")
    submitted = st.form_submit_button("🚀 Submit Telemetry")