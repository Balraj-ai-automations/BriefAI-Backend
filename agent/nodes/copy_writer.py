from agent.state import BriefAIState


def copy_writer(state: BriefAIState) -> BriefAIState:
    print("Running Node 3: Copy Writer")

    state["whatsapp_copy"] = "Test WA message"

    state["instagram_caption"] = (
        "Test IG caption #test"
    )

    return state