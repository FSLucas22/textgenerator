from textgenerator import string_generator


def letter_a() -> str:
    return "a"


def test_should_generate_single_string_based_on_letter_generator() -> None:
    length = 5
    result: str = string_generator(length, letter_a)
    assert result == "a" * length
