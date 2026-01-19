from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class InteractionInput(BaseModel):
    hcp_id: int = Field(..., description="Unique HCP identifier")
    rep_id: int = Field(..., description="Sales representative ID")
    notes: str = Field(..., description="Conversation or structured interaction notes")
    interaction_type: str = Field(
        default="in-person",
        description="in-person | call | email | virtual"
    )
    edit_notes: Optional[str] = Field(
        None,
        description="Optional edits for existing interaction"
    )


class InteractionResponse(BaseModel):
    interaction_id: int
    summary: str
    sentiment: Optional[str]
    compliance_status: Optional[str]
    next_best_action: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
