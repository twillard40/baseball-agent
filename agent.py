from smolagents import LiteLLMModel, CodeAgent
from tools import get_player_splits, get_batter_stats, get_pitcher_stats
from config import SYSTEM_PROMPT

# ============================================================
# MODEL CONFIGURATION
# ============================================================

model = LiteLLMModel(
    model_id="ollama_chat/llama3.2",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
    temperature=0.7,
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

agent = CodeAgent(
    model=model,
    tools=tools,
    instructions=SYSTEM_PROMPT,
    max_steps=7,
)

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    response = agent.run("Is Roman Anthony a good start on the road?")
    print(response)