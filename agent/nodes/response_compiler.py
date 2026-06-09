from uuid import uuid4

from agent.state import BriefAIState


def response_compiler(state: BriefAIState) -> BriefAIState:
    print("Running Node 6: Response Compiler")

    campaign_id = str(uuid4())

    state["campaign_id"] = campaign_id

    state["final_response"] = {
        "campaign_id": campaign_id,
        "whatsapp_copy": state.get("whatsapp_copy"),
        "instagram_caption": state.get("instagram_caption"),
        "image_url": state.get("image_url"),
        "strategy": state.get("strategy"),
        "quality_passed": state.get("quality_passed"),
    }

    return state