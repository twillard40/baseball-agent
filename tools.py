
from pybaseball import batting_stats_bref
import requests

# ============================================================
# UTILITIES
# Helper functions used by multiple tools
# ============================================================

#  get_player_id()

def get_player_id(player_name: str) -> int | None:
    """
    Looks up a player's mlbID from the Baseball Reference batting stats.
    Returns the mlbID as an integer, or None if the player is not found.
    """
    stats = batting_stats_bref(2025)
    match = stats[stats['Name'].str.contains(player_name, case=False, na=False)]
    
    if match.empty:
        return None
    
    if len(match) > 1:
        # Multiple players matched -- return the list of names for disambiguation
        return match['Name'].tolist()
    
    return int(match.iloc[0]['mlbID'])

# call_mlb_api()

def call_mlb_api(url: str) -> dict | None:
    """
    Makes a GET request to the MLB Stats API.
    Returns the JSON response as a dictionary, or None if the request fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None
    except requests.exceptions.ConnectionError:
        print("Connection error -- check your internet connection")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# ============================================================
# BATTING TOOLS
# ============================================================


# ============================================================
# PITCHING TOOLS
# ============================================================


# ============================================================
# MATCHUP TOOLS
# ============================================================