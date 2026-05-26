from tools import get_player_id

def test_single_match():
    assert get_player_id("Ohtani") == 660271

def test_no_match():
    assert get_player_id("zzzzz") is None

def test_multiple_match():
    assert isinstance(get_player_id("Williams"), list)

    # Test 2

from tools import get_player_id, call_mlb_api

def test_call_mlb_api_success():
    url = "https://statsapi.mlb.com/api/v1/people/660271"
    result = call_mlb_api(url)
    assert result is not None

def test_call_mlb_api_bad_url():
    url = "https://statsapi.mlb.com/api/v1/people/000000000"
    result = call_mlb_api(url)
    assert result is None