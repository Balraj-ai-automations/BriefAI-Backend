from agent.state import BriefAIState


def strategy_planner(state: BriefAIState) -> BriefAIState:
    print("Running Node 2: Strategy Planner")

    state["strategy"] = {
        "tone": "warm",
        "campaign_angle": "Desi style, modern comfort",
    }

    return state