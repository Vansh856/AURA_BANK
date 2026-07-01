import streamlit as st

#==========================================================================
#1. CHECKING THE USER'S AUTHENTICATION STATE WHEN THE APP LOADS
#===========================================================================

is_logged_in="authenticated_user" in st.session_state

#=============================================
# 2. DEFINING THE PAGES
#=============================================

landing_page = st.Page("views/landing.py", title="Home", icon="🏠", default=True)
#changing the visibility according to the session state
auth_page = st.Page("views/auth.py", title="Login / Register", icon="🔐",visibility="hidden" if is_logged_in else "visible")
dashboard_page = st.Page("views/dashboard.py", title="Dashboard", icon="🏦", visibility="visible"if is_logged_in else "hidden")

contact_page=st.Page("views/contact.py",title="contact",visibility="hidden")
about_page=st.Page("views/about.py",title="About us",visibility="hidden")

#=================================
# 3. SETUP THE NAVIGATION
#=================================

pg = st.navigation([landing_page, auth_page, dashboard_page,contact_page,about_page])

#========================
# 4. run the app
#========================

pg.run()