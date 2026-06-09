from smolagents import LiteLLMModel, ToolCallingAgent
from tools import get_player_splits, get_batter_stats, get_pitcher_stats
from config import SYSTEM_PROMPT

# ============================================================
# MODEL CONFIGURATION
# ============================================================

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
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