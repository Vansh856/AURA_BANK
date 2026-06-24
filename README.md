# 🏦 Aura Bank
**The Financialization of Engagement Data.**

## 🚀 Overview
Aura Bank is a B2B user-testing engine wrapped inside a highly addictive, gamified virtual neobank [1, 2]. 

Traditional reward apps feel like a chore and suffer from massive user churn because the payouts feel cheap [2, 3]. Aura Bank completely flips this model by replacing low-affinity cash rewards with high-affinity social and financial gamification [4]. Instead of earning pennies, users build a simulated financial identity—including an "Aura Score" (a virtual credit score) and an "Aura Points" balance—by delivering high-quality UI/UX feedback on beta games [4]. 

## ✨ Core Features
* **The Virtual Neobank Dashboard:** A fully simulated B2C financial layer that displays the user's Aura Score, Aura Points, and AuraCard Tier using dynamic UI metrics [5].
* **B2B Game Testing Engine:** An embedded platform where users can play open-source web games and provide detailed UI/UX feedback to earn virtual rewards [6].
* **Anti-Data Degradation Engine:** To ensure B2B game studios receive valuable insights, the platform ties the user's Aura Score directly to feedback quality [7]. High-quality reviews boost credit scores, while spammy or mindless feedback tanks the score and locks the account [7].
* **Macroeconomic "Sinks":** Built-in point-burning systems (like transaction fees or digital items) prevent the hyperinflation of the "Aura Points" supply [8].

## 💻 Tech Stack & Architecture
This application is built with a highly modular, high-performance architecture split across multiple files [9].

**Frontend: Streamlit**
* Streamlit is an open-source Python framework used to build and deploy the dynamic frontend interface [10].
* Utilizes Streamlit's new `st.Page()` routing with the `visibility` parameter to dynamically hide and reveal the authentication and dashboard portals based on the user's login state [11].
* Employs session-state route protection to prevent unauthorized access.

**Backend: FastAPI**
* Built on FastAPI, a modern, fast web framework for building APIs with Python that offers performance on par with NodeJS and Go [12].
* Uses Pydantic models for strict schema validation to restrict password lengths and prevent brute-force memory overloads [13, 14].
* The backend will scale using the `APIRouter` class to separate authentication pipelines from the virtual economy calculations [9].

**Database: SQL**
* A relational SQL database utilizing B-Tree indexing and primary keys to ensure lightning-fast user authentication and secure data retrieval.

## 📂 Project Structure
```text
aura_bank/
│
├── main.py                  # The Streamlit frontend entrypoint and page router
├── backend/
│   └── backend.py           # The FastAPI application and core API endpoints
│
├── views/                   # Modular Streamlit UI pages
│   ├── landing.py           # VC-ready home page
│   ├── auth.py              # Login and Registration Gateway
│   ├── dashboard.py         # The Virtual Neobank financial dashboard
│   ├── beta_testing.py      # Embedded HTML5 game and feedback form
│   ├── about.py             # Hidden about page
│   └── contact.py           # Hidden contact page
│
├── .gitignore               # Ensures virtual environments and DBs are not committed
└── README.md                # Project documentation
🛠️ How to Run Locally
1. Clone the repository and set up your environment Make sure you have Python installed, then create and activate a virtual environment
:
git clone https://github.com/yourusername/aura-bank.git
cd "aura bank"
python -m venv venv
source venv/Scripts/activate  # On Windows
2. Install the required dependencies
pip install "fastapi[standard]" streamlit requests
3. Start the FastAPI Backend The fastapi dev command automatically detects the FastAPI app and starts a local server with auto-reload enabled
.
cd backend
fastapi dev backend.py
The backend API will run on http://127.0.0.1:8000. You can view the interactive API documentation by navigating to http://127.0.0.1:8000/docs
.
4. Start the Streamlit Frontend Open a second terminal window, ensure your virtual environment is activated, and run the Streamlit app:
streamlit run main.py
The gamified neobank will open in your browser at http://localhost:8501.
