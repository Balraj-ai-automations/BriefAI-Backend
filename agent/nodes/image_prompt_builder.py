from agent.state import BriefAIState


def image_prompt_builder_node(
    state: BriefAIState,
) -> BriefAIState:
    """
    Build the image prompt for the image generation service.

    This is currently a placeholder implementation.
    It will be replaced with the Replicate/Flux integration
    in Phase 4.
    """

    print("Running Node 4: Image Prompt Builder")

    state["image_prompt"] = (
        "beautiful kurti product photo"
    )

    state["negative_prompt"] = (
        "blurry, watermark, low quality"
    )

    state["image_url"] = (
        "https://placeholder.com/image.jpg"
    )

    state["replicate_url"] = (
        "https://replicate.com/test"
    )

    state["aspect_ratio"] = "1:1"

    return state