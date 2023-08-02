from textgenerator import word_generator


def test_should_generate_single_word() -> None:
    characters = 5
    result: str = word_generator(characters)
    assert len(result.split()) == 1


def test_should_generate_word_with_exact_character_length() -> None:
    characters = 5
    result: str = word_generator(characters)
    assert len(result) == characters


def test_actions() -> None:
    assert True
