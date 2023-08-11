from textgenerator import word_generator


def letter_a() -> str:
    return "a"


def test_should_generate_single_word_based_on_letter_generator() -> None:
    length = 5
    result: str = word_generator(length, letter_a)
    assert result == "a" * length
