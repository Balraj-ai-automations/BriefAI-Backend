from agent.state import BriefAIState


def quality_checker(state: BriefAIState) -> BriefAIState:
    print("Running Node 5: Quality Checker")

    retry_count = state.get("retry_count", 0)

    # Force pass after 2 retries
    if retry_count >= 2:
        state["quality_passed"] = True
        state["quality_feedback"] = (
            "Force passed after max retries"
        )

    else:
        state["quality_passed"] = True
        state["quality_feedback"] = None

    state["retry_count"] = retry_count

    # Dummy score for Phase 2
    

    return state