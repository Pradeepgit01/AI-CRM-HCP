from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import interaction
from db import database

app = FastAPI(
    title="AI-First CRM HCP Module",
    description="Log Interaction Screen using LangGraph + LLM",
    version="1.0.0"
)

# CORS (React Frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB init
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Routers
app.include_router(interaction.router, prefix="/api/interactions", tags=["HCP Interactions"])

@app.get("/")
def root():
    return {
        "status": "running",
        "service": "AI-First CRM HCP Log Interaction"
    }
