from tools import get_player_id, call_mlb_api, get_player_splits, get_batter_stats, get_pitcher_id, get_pitcher_stats

# get_player_id tests
def test_single_match():
    assert get_player_id("Ohtani") == 660271

def test_no_match():
    assert get_player_id("zzzzz") is None

def test_multiple_match():
    assert isinstance(get_player_id("Williams"), list)

# call_mlb_api tests
def test_call_mlb_api_success():
    url = "https://statsapi.mlb.com/api/v1/people/660271"
    result = call_mlb_api(url)
    assert result is not None

def test_call_mlb_api_bad_url():
    url = "https://statsapi.mlb.com/api/v1/people/000000000"
    result = call_mlb_api(url)
    assert result is None

# get_player_splits tests
def test_get_player_splits_vs_left():
    result = get_player_splits("Ohtani", "vl")
    assert "AVG" in result
    assert "OPS" in result

def test_get_player_splits_player_not_found():
    result = get_player_splits("zzzzz", "vl")
    assert "No player found" in result

def test_get_player_splits_ambiguous_name():
    result = get_player_splits("Williams", "vl")
    assert "Multiple players found" in result

# get_batter_stats tests
def test_get_batter_stats_success():
    result = get_batter_stats("Ohtani")
    assert "AVG" in result
    assert "OPS" in result

def test_get_batter_stats_not_found():
    result = get_batter_stats("zzzzz")
    assert "No player found" in result

def test_get_batter_stats_ambiguous():
    result = get_batter_stats("Williams")
    assert "Multiple players found" in result

# get_pitcher_id tests
def test_get_pitcher_id_success():
    result = get_pitcher_id("deGrom")
    assert result == 594798

def test_get_pitcher_id_not_found():
    result = get_pitcher_id("zzzzz")
    assert result is None

def test_get_pitcher_id_ambiguous():
    result = get_pitcher_id("Cole")
    assert isinstance(result, list)

def test_get_pitcher_stats_success():
    result = get_pitcher_stats("deGrom")
    assert "ERA" in result
    assert "WHIP" in result

def test_get_pitcher_stats_not_found():
    result = get_pitcher_stats("zzzzz")
    assert "No pitcher found" in result

def test_get_pitcher_stats_ambiguous():
    result = get_pitcher_stats("Cole")
    assert "Multiple pitchers found" in result