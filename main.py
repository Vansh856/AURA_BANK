import streamlit as st

# 1. Define the pages
landing_page = st.Page("views/landing.py", title="Home", icon="🏠", default=True)
auth_page = st.Page("views/auth.py", title="Login / Register", icon="🔐")

# The 1% Trick: Hide the dashboard from the sidebar using visibility=False [2]
dashboard_page = st.Page("views/dashboard.py", title="Dashboard", icon="🏦", visibility="hidden")

contact_page=st.Page("views/contact.py",title="contact",visibility="hidden")
about_page=st.Page("views/about.py",title="About us",visibility="hidden")
# 2. Setup the Navigation
pg = st.navigation([landing_page, auth_page, dashboard_page,contact_page,about_page])

# 3. Run the App
pg.run()