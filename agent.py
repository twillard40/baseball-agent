from smolagents import LiteLLMModel, CodeAgent
from tools import get_player_splits, get_batter_stats, get_pitcher_stats

# ============================================================
# MODEL CONFIGURATION
# ============================================================

model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",
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
)

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    response = agent.run("How does Ohtani hit against left handed pitchers?")
    print(response)