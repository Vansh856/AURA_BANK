import streamlit as st
import streamlit.components.v1 as components
#=================================================
#1. ROUTE PROTECTION AND STATE RETRIVAL
#==============================================

#If the user is not in the session memory kick them back to the landing page
if "authenticated_user" not in st.session_state:
    st.warning("Unauthorized Access.Please login first")
    st.switch_page("views/landing.py")

#If they are login fetch their username from memory
current_user=st.session_state["authenticated_user"]

#==========================================================
#2. SLIDEBAR PROFILE AND LOGOUT
#==========================================================

st.sidebar.markdown(f"👤 **Logged in as:** {current_user}")
if st.sidebar.button("Logout",type="primary"):
    #delete the session
    del st.session_state["authenticated_user"]
    #route back to the landing page
    st.switch_page("views\landing.py")



#======================================================
#2. NEOBANK DASHBORD HEADER
#======================================================

st.title(f"Welcome to your Neobank, {current_user}! 🏦")
st.markdown("*Your engagement data is your ultimate financial asset.*")
st.markdown("---")

#==================================================
#3. CREATING USER DESCIPTION CHART
#==================================================
aura_Score,aura_points,auraCard=st.columns(3)

#dashboard for user to see their progress
with aura_Score:
    st.metric(label="Aura Score", value="750", delta="+15", delta_description="High Quality Feedback Bonus")

with aura_points:
    st.metric(label="Aura points", value="750", delta="+15", delta_description="Your earning")
with auraCard:
    st.metric(label="Aura credit card", value="750", delta="+15", delta_description="SILVER")

#==============================================================
#4. GAMING AND FEEDBACK ENGINE
#==============================================================

st.markdown("---")
st.subheader("🎮Beta Testing Engine")
st.info("Test this open source web game to earn aura points and to gain aura score")


#Embed the web game using the streamlit iframe component
components.iframe("https://play2048.co/", width=700, height=500)


#Feedback engine
