
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

# get_player_splits()

from smolagents import tool

@tool
def get_player_splits(player_name: str, split_code: str) -> str:
    """
    Retrieves batting split stats for a player against a specific situation.
    Use this when the user asks how a batter performs against left or right handed pitchers,
    at home or away, during day or night games, or any other split situation.

    Args:
        player_name: The full or partial name of the batter. Example: 'Ohtani' or 'Shohei Ohtani'.
        split_code: The situation code for the split. Common codes:
            vl = vs Left handed pitchers
            vr = vs Right handed pitchers
            h = Home games
            a = Away games
            d = Day games
            n = Night games

    Returns:
        A formatted string with the player's stats for that split situation,
        or a message explaining why data is not available.
    """
    # Step 1 -- look up player ID
    player_id = get_player_id(player_name)

    if player_id is None:
        return f"No player found matching '{player_name}'. Check the spelling and try again."

    if isinstance(player_id, list):
        names = ", ".join(player_id)
        return f"Multiple players found matching '{player_name}': {names}. Please be more specific."

    # Step 2 -- call MLB Stats API
    url = f"https://statsapi.mlb.com/api/v1/people/{player_id}/stats?stats=statSplits&season=2024&group=hitting&sitCodes={split_code}"
    data = call_mlb_api(url)

    if data is None:
        return f"Could not retrieve data for {player_name}. The MLB Stats API may be unavailable."

    # Step 3 -- parse response
    splits = data['stats'][0]['splits']

    if not splits:
        return f"No split data found for '{player_name}' with split code '{split_code}'."

    # Step 4 -- format output
    split = splits[0]
    stat = split['stat']
    description = split['split']['description']

    return (
        f"{player_name} | {description}\n"
        f"AVG: {stat['avg']} | OBP: {stat['obp']} | SLG: {stat['slg']} | OPS: {stat['ops']}\n"
        f"HR: {stat['homeRuns']} | RBI: {stat['rbi']} | BB: {stat['baseOnBalls']} | SO: {stat['strikeOuts']}\n"
        f"AB: {stat['atBats']} | Hits: {stat['hits']} | Games: {stat['gamesPlayed']}"
    )

# get_batter_stats

@tool
def get_batter_stats(player_name: str) -> str:
    """
    Retrieves current season batting stats for a player.
    Use this when the user asks about a batter's overall season performance,
    stats, or how a player is doing this year.

    Args:
        player_name: The full or partial name of the batter. Example: 'Ohtani' or 'Shohei Ohtani'.

    Returns:
        A formatted string with the player's current season stats,
        or a message explaining why data is not available.
    """
    # Step 1 -- check player exists
    player_id = get_player_id(player_name)

    if player_id is None:
        return f"No player found matching '{player_name}'. Check the spelling and try again."

    if isinstance(player_id, list):
        names = ", ".join(player_id)
        return f"Multiple players found matching '{player_name}': {names}. Please be more specific."

    # Step 2 -- get batting stats
    stats = batting_stats_bref(2025)
    match = stats[stats['Name'].str.contains(player_name, case=False, na=False)]
    row = match.iloc[0]

    # Step 3 -- format output
    return (
        f"{row['Name']} | {row['Tm']} | Age: {row['Age']}\n"
        f"AVG: {row['BA']} | OBP: {row['OBP']} | SLG: {row['SLG']} | OPS: {row['OPS']}\n"
        f"HR: {row['HR']} | RBI: {row['RBI']} | SB: {row['SB']}\n"
        f"BB: {row['BB']} | SO: {row['SO']} | G: {row['G']} | PA: {row['PA']}"
    )

# ============================================================
# PITCHING TOOLS
# ============================================================


# ============================================================
# MATCHUP TOOLS
# ============================================================