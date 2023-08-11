from textgenerator import word_generator


def letter_a() -> str:
    return "a"


def test_should_generate_single_word_with_correct_length() -> None:
    characters = 5
    result: str = word_generator(characters, letter_a)
    assert result == "a" * characters
