from textgenerator import main


import pytest


def test_main_can_generate_correct_length_word(capsys: pytest.CaptureFixture[str]) -> None:
    main(["3", "5"])
    captured_words = capsys.readouterr()
    assert captured_words.err == ""
    word_lengths = [len(word) for word in captured_words.out.split()]
    assert word_lengths == [3, 5]
