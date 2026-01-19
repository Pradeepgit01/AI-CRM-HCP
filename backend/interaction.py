from fastapi import APIRouter
from schemas.interaction_schema import InteractionInput
from langgraph_agent.agent import run_agent

router = APIRouter()

@router.post("/log")
async def log_interaction(data: InteractionInput):
    result = run_agent(data)
    return {"message": "Interaction logged", "data": result}
