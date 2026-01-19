from datetime import datetime
from typing import Dict, Any
from langchain_groq import ChatGroq

# Initialize LLM (Groq – Gemma2)
llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0.3,
    api_key="YOUR_GROQ_API_KEY"
)

# ---------------- TOOL 1: Log Interaction ----------------
def log_interaction_tool(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Captures HCP interaction via structured or conversational input.
    Uses LLM for summarization & entity extraction.
    """

    interaction_text = state["input"].notes

    prompt = f"""
    You are an AI CRM assistant.
    Summarize the interaction and extract key entities.

    Text:
    {interaction_text}

    Return:
    - Summary
    - HCP Name
    - Product Discussed
    - Intent (Positive / Neutral / Negative)
    """

    response = llm.invoke(prompt)

    state["logged_interaction"] = {
        "summary": response.content,
        "created_at": datetime.utcnow().isoformat()
    }

    return state


# ---------------- TOOL 2: Edit Interaction ----------------
def edit_interaction_tool(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Allows editing of an existing logged interaction.
    """

    if "edit_notes" in state["input"] and state.get("logged_interaction"):
        state["logged_interaction"]["summary"] += (
            "\n[EDITED]: " + state["input"].edit_notes
        )

    state["logged_interaction"]["updated_at"] = datetime.utcnow().isoformat()
    return state


# ---------------- TOOL 3: Sentiment Analysis ----------------
def sentiment_analysis_tool(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Determines HCP sentiment from conversation.
    """

    prompt = f"""
    Classify the sentiment of the following interaction
    as Positive, Neutral, or Negative:

    {state["input"].notes}
    """

    response = llm.invoke(prompt)
    state["sentiment"] = response.content.strip()
    return state


# ---------------- TOOL 4: Compliance Check ----------------
def compliance_check_tool(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ensures no off-label or compliance violations occurred.
    """

    prompt = f"""
    Check the following interaction for compliance issues.
    Flag if off-label promotion or violations exist.

    {state["input"].notes}
    """

    response = llm.invoke(prompt)
    state["compliance_status"] = response.content.strip()
    return state


# ---------------- TOOL 5: Next Best Action ----------------
def next_best_action_tool(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Suggests next best sales action for the field representative.
    """

    prompt = f"""
    Based on this interaction summary, suggest the next best action
    for a pharma sales representative:

    {state.get("logged_interaction")}
    """

    response = llm.invoke(prompt)
    state["next_best_action"] = response.content.strip()
    return state
