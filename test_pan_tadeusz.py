import pytest
from pan_tadeusz import play


def test_play_display_help(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "x")
    play()
    captured = capsys.readouterr()
    assert 'Hit x to finish, c to continue.' in captured.out
