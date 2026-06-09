from agent.state import BriefAIState


def input_parser(state: BriefAIState) -> BriefAIState:
    print("Running Node 1: Input Parser")

    state["business_profile"] = {
        "product": "handmade kurti",
        "business_type": "clothing",
        "price_level": "budget",
    }

    return state