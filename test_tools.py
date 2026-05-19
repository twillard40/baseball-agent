from tools import get_player_id

def test_single_match():
    assert get_player_id("Ohtani") == 660271

def test_no_match():
    assert get_player_id("zzzzz") is None

def test_multiple_match():
    assert isinstance(get_player_id("Williams"), list)