from fastapi import FastAPI
from routers import auth
app = FastAPI(title="Aura Bank API")
app.include_router(auth.router)