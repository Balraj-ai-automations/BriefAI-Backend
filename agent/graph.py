from langgraph.graph import StateGraph, END

from agent.state import BriefAIState

from agent.nodes.input_parser import input_parser
from agent.nodes.strategy_planner import strategy_planner
from agent.nodes.copy_writer import copy_writer
from agent.nodes.image_prompt_builder import image_prompt_builder
from agent.nodes.quality_checker import quality_checker
from agent.nodes.response_compiler import response_compiler


def quality_router(state: BriefAIState):
    """
    Retry logic for Node 5.
    """

    if (
        state.get("quality_passed") is False
        and state.get("retry_count", 0) < 2
    ):
        return "retry"

    return "pass"


graph_builder = StateGraph(BriefAIState)

# Nodes
graph_builder.add_node("input_parser", input_parser)
graph_builder.add_node("strategy_planner", strategy_planner)
graph_builder.add_node("copy_writer", copy_writer)
graph_builder.add_node("image_prompt_builder", image_prompt_builder)
graph_builder.add_node("quality_checker", quality_checker)
graph_builder.add_node("response_compiler", response_compiler)

# Entry point
graph_builder.set_entry_point("input_parser")

# Main flow
graph_builder.add_edge(
    "input_parser",
    "strategy_planner"
)

graph_builder.add_edge(
    "strategy_planner",
    "copy_writer"
)

graph_builder.add_edge(
    "copy_writer",
    "image_prompt_builder"
)

graph_builder.add_edge(
    "image_prompt_builder",
    "quality_checker"
)

# Conditional routing
graph_builder.add_conditional_edges(
    "quality_checker",
    quality_router,
    {
        "retry": "copy_writer",
        "pass": "response_compiler",
    },
)

graph_builder.add_edge(
    "response_compiler",
    END
)

graph = graph_builder.compile()