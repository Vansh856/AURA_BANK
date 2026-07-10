import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Aura Bank",
    page_icon="🏦",
    layout="centered"
)

# ==========================================
# 2. NATIVE HERO HEADER (No HTML/CSS!)
# ==========================================
st.title("🏦 :green[AURA BANK]")
st.subheader("Build. Compete. Master Your Finances.")
st.caption("THE FINANCIALISATION OF ENGAGEMENT DATA")
st.write("---")

# ==========================================
# 3. NATIVE MULTI-COLUMN FEATURE GRID
# ==========================================
# Create two equal responsive columns
col_gamers, col_partners = st.columns(2)

# Column 1: B2C Gamer Pillar
with col_gamers:
    with st.container(border=True):
        st.markdown("### 🎮 :green[For Gamers]")
        st.write(
            "Stop testing games for virtual pennies. Build your **Aura Score** "
            "(virtual credit rating) by providing high-quality gameplay telemetry. "
            "Accumulate **Aura Points** and unlock high-tier simulated credit assets."
        )

# Column 2: B2B Partner Pillar
with col_partners:
    with st.container(border=True):
        st.markdown("### 💼 :green[For B2B Partners]")
        st.write(
            "Connect directly to our **B2B Game Testing Engine**. Our proprietary "
            "**Anti-Data Degradation Engine** validates user telemetry at source, "
            "ensuring high-quality, zero-noise reviews for your development pipelines."
        )

# ==========================================
# 4. NATIVE ACTION TRIGGERS (No HTML/CSS!)
# ==========================================
col_login, col_register = st.columns(2)

with col_login:
    # We use type="primary" to highlight the main portal access point
    if st.button("🔓 Access Portal", use_container_width=True, type="primary"):
        st.session_state["Auth_mode"] = "Login"
        st.switch_page("views/auth.py")

with col_register:
    if st.button("📝 Register Account", use_container_width=True):
        st.session_state["Auth_mode"] = "Register"
        st.switch_page("views/auth.py")

st.write("---")

# ==========================================
# 5. NATIVE MINIMALIST FOOTER
# ==========================================
col_foot1, col_foot2 = st.columns(2)

with col_foot1:
    st.page_link("views/contact.py", label="Contact Support", icon="📧")

with col_foot2:
    st.page_link("views/about.py", label="About Us", icon="ℹ️")