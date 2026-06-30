import json
import logging

from agent.state import BriefAIState
from prompts.strategy_planner import build_strategy_prompt
from services.mistral import mis/tral_service

logger = logging.getLogger(__name__)


def strategy_planner_node(state: BriefAIState) -> BriefAIState:
    """
    Generate a marketing strategy based on the structured
    business profile.
    """

    try:
        logger.info("Starting Strategy Planner node.")

        # Step 1: Read business profile from state
        business_profile = state["business_profile"]

        # Step 2: Build prompt
        prompt = build_strategy_prompt(
            business_profile=business_profile,
        )

        # Step 3: Generate response
        response = mistral_service.generate(prompt)

        # Step 4: Parse JSON response
        strategy = json.loads(response)

        # Step 5: Update state
        state["strategy"] = strategy

        logger.info("Strategy Planner node completed successfully.")

        return state

    except Exception as e:
        logger.exception("Strategy Planner node failed.")

        state["error"] = str(e)

        return state