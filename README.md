# 🏦 Aura Bank

> **The Financialization of Engagement Data.**  
> Aura Bank is a revolutionary B2B user-testing engine disguised as an immersive, gamified virtual neobank. It bridges the gap between game developers needing high-fidelity feedback and players seeking engaging, status-driven mechanics [1, 2].

---

## 🚀 Overview

Traditional play-to-test and reward models suffer from high user churn because micro-payments feel cheap, transactional, and tedious [2, 3]. Aura Bank completely reimagines this economy by replacing low-affinity cash rewards with status-driven financial gamification [4, 5]. 

Instead of earning fractional pennies, testers build a simulated financial identity—anchored by an **Aura Score** (a virtual credit score) and **Aura Points** balance—by playing indie games and providing structured telemetry and written feedback [5, 6].

To ensure game developers receive premium, actionable data, Aura Bank features an **Anti-Data Degradation Engine** [7]. If users submit low-quality, rushed, or spammy feedback to speedrun points, their Aura Score tanks, locking their simulated financial tier and restricting access to elite virtual cards [7].

---

## 🛠️ Repository Architecture

The project is structured with a clean, high-performance modular layout separation [47]:

```directory
.
├── assets/                  # Static design files, UI templates, and logos
├── backend/                 # High-performance FastAPI endpoints & Database connections
│   ├── auth/                # Security handlers, JWT token generation, and password hashing
│   ├── database/            # Relational MSSQL schema scripts, T-SQL migration procedures
│   └── main.py              # FastAPI microservices entrance
├── views/                   # Dynamic Streamlit frontend modules & Page routing
│   ├── about.py             # App vision, B2B partner info, and company bio
│   ├── auth.py              # Multi-state User registration and credential gatekeeping
│   ├── contact.py           # B2B client ticket inquiries and customer service portal
│   ├── dashboard.py         # Financial ledger, simulated credit cards, and balance statements
│   ├── feedback.py          # Detailed B2B telemetry collection and feedback validation form
│   ├── game_testing.py      # Gamers arcade lobby & active beta build selection
│   ├── games_bundle.py      # Hardcoded lightweight HTML5 game modules (2048, Snake, etc.)
│   ├── landing.py           # Conversational B2C/B2B landing hub page
│   └── play_game.py         # Isolated sandboxed iframe container for lag-free gameplay
├── .gitignore               # Excludes python virtual environments and databases
├── LICENSE                  # Open-source MIT Licensing
├── main.py                  # Entrypoint orchestrating modern page navigation routing
└── README.md                # Project documentation and architectural manifest
```

---

## ✨ Core Pillars & Features

### 1. The Virtual Neobank Dashboard
* **Dynamic Credit Scoring:** Players check their real-time **Aura Score** (credit score) and **Aura Points** balance [5].
* **Simulated Tiered Cards:** High scores unlock prestigious card tiers (Silver, Gold, Obsidian), unlocking premium game sandboxes and marketplace privileges [6].

### 2. B2B Game Testing Arena
* **Sandboxed Components:** Leverages isolated client-side iframe sandboxes to render retro HTML5 games (e.g., 2048, Snake) directly inside the Streamlit client [6, 137].
* **Lag-Free Interaction:** Heavy gameplay mechanics and input listeners execute strictly inside the iframe context, keeping the Python server completely light and reactive.

### 3. High-Precision Telemetry & Anti-Data Degradation
* **Precision Timers:** Automatically calculates precise active session playtime durations behind the scenes when a player launches a beta build.
* **Smart Validation Forms:** Uses input buffering techniques (`st.form`) to guarantee a smooth, lag-free writing experience.
* **T-SQL Telemetry Logging:** Records structured quantitative ratings (Gameplay, Graphics, Audio, Performance) and verified qualitative reviews inside relational schemas [125].

### 4. Robust MSSQL Backend Database
* Built on a relational **Microsoft SQL Server (MSSQL)** schema utilizing clustered and non-clustered indexing for lightning-fast user authentication and integrity [125, 528].
* Restricts brute-force memory leaks with strict input character constraints and structured schemas linking game reviews cleanly back to unique user tables via foreign key relations [127, 331].

---

## 🔌 Technical Handshakes

### Dynamic State Routing (`main.py`)
Rather than relying on outdated sidebar navigations, the app implements Streamlit’s modern `st.Page` structure [11, 47]. It dynamically controls user navigation based on state variables [11]:
```python
landing_page = st.Page(
    "views/landing.py", 
    title="Home", 
    icon="🏠", 
    default=not is_logged_in,
    visibility="hidden" if is_logged_in else "visible"
)
```
This ensures hidden panels (like the gameplay renderer or the feedback portal) remain completely routable programmatically via state-guards while preventing sidebar clutter for clean aesthetics [11, 574].

---

## 🚀 Setting Up Locally

### Prerequisites
* **Python 3.12+**
* **Microsoft SQL Server (MSSQL)** [114]

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Vansh856/AURA_BANK.git
   cd AURA_BANK
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the Database:
   Set up your MSSQL server connection string inside `backend/database/` and run the structural T-SQL schemas to initialize the `UserLogin`, `UserEconomy`, and `GameTelemetry` tables [125, 127].
4. Launch the Application:
   ```bash
   streamlit run main.py
   ```


