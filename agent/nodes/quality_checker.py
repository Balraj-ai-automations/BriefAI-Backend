import json
import logging

from agent.state import BriefAIState
from prompts.quality_checker import build_quality_checker_prompt
from services.mistral import mistral_service

logger = logging.getLogger(__name__)


def quality_checker_node(state: BriefAIState) -> BriefAIState:
    """
    Review the generated marketing copy.

    This node validates the generated WhatsApp message and
    Instagram caption against the business profile and
    marketing strategy.
    """

    try:
        logger.info("Starting Quality Checker node.")

        # --------------------------------------------------
        # Step 1: Read state
        # --------------------------------------------------

        business_profile = state["business_profile"]
        strategy = state["strategy"]

        whatsapp_copy = state["whatsapp_copy"]
        instagram_caption = state["instagram_caption"]

        wa_language = state.get("wa_language", "English")
        ig_language = state.get("ig_language", "English")

        # --------------------------------------------------
        # Step 2: Build prompt
        # --------------------------------------------------

        prompt = build_quality_checker_prompt(
            business_profile=business_profile,
            strategy=strategy,
            whatsapp_copy=whatsapp_copy,
            instagram_caption=instagram_caption,
            wa_language=wa_language,
            ig_language=ig_language,
        )

        # --------------------------------------------------
        # Step 3: Call Mistral
        # --------------------------------------------------

        response = mistral_service.generate(prompt)

        # --------------------------------------------------
        # Step 4: Parse JSON
        # --------------------------------------------------

        review = json.loads(response)

        # --------------------------------------------------
        # Step 5: Update state
        # --------------------------------------------------

        state["quality_passed"] = review["passed"]
        state["quality_feedback"] = review["feedback"]

        # Optional (recommended)
        state["quality_score"] = review["score"]

        logger.info("Quality Checker node completed successfully.")

        return state

    except Exception as e:
        logger.exception("Quality Checker node failed.")

        state["error"] = str(e)

        return state