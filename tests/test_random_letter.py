from textgenerator import random_letter


def test_should_only_return_letters() -> None:
    for _ in range(10):
        letter = random_letter()
        assert len(letter) == 1
        assert letter.isalpha()
