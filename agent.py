from smolagents import LiteLLMModel, ToolCallingAgent
from dotenv import load_dotenv
from tools import get_player_splits, get_batter_stats, get_pitcher_stats
from config import SYSTEM_PROMPT

load_dotenv()

# ============================================================
# MODEL CONFIGURATION
# ============================================================

model = LiteLLMModel(
    model_id="anthropic/claude-haiku-4-5",
    temperature=0.3,
)

# ============================================================
# TOOLS
# ============================================================

tools = [
    get_player_splits,
    get_batter_stats,
    get_pitcher_stats,
]

# ============================================================
# AGENT
# ============================================================

agent = ToolCallingAgent(
    model=model,
    tools=tools,
    instructions=SYSTEM_PROMPT,
    max_steps=10,
)

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    response = agent.run("How does Roman Anthony perform in away games?")
    print(response)