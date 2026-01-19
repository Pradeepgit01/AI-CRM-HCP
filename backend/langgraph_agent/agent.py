from langgraph.graph import StateGraph
from langgraph_agent.tools import log_interaction_tool, edit_interaction_tool

def run_agent(input_data):
    graph = StateGraph(dict)

    graph.add_node("log", log_interaction_tool)
    graph.add_node("edit", edit_interaction_tool)

    graph.set_entry_point("log")
    graph.add_edge("log", "edit")

    app = graph.compile()
    return app.invoke({"input": input_data})
