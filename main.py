import streamlit as st

#==========================================================================
#1. CHECKING THE USER'S AUTHENTICATION STATE WHEN THE APP LOADS
#===========================================================================

is_logged_in="authenticated_user" in st.session_state

#=============================================
# 2. DEFINING THE PAGES
#=============================================

landing_page = st.Page(
    "views/landing.py", 
    title="Home", 
    icon="🏠", 
    default=not is_logged_in,  # True only if the user is NOT logged in
    visibility="hidden" if is_logged_in else "visible"
)

dashboard_page = st.Page(
    "views/dashboard.py", 
    title="Dashboard", 
    icon="🏦", 
    default=is_logged_in,      # True only if the user IS logged in
    visibility="visible" if is_logged_in else "hidden"
)
#changing the visibility according to the session state
auth_page = st.Page("views/auth.py", title="Login / Register", icon="🔐",visibility="hidden" if is_logged_in else "visible")


contact_page=st.Page("views/contact.py",title="contact",visibility="hidden")
about_page=st.Page("views/about.py",title="About us",visibility="hidden")
testing_engine=st.Page("views/game_testing.py",title="Testing engine",icon="🎮",visibility="visible" if is_logged_in else "hidden")
game_play=st.Page("views/play_game.py", title="play game", icon="🎮",visibility="hidden")
feedback_form=st.Page("views/feedback.py",title="feedback_form",visibility="hidden")

#=================================
# 3. SETUP THE NAVIGATION
#=================================

pg = st.navigation([landing_page, auth_page, dashboard_page,contact_page,about_page,testing_engine,game_play,feedback_form])

#========================
# 4. run the app
#=======================

pg.run()