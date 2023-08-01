from src.textgenerator import text_generator


def test_should_generate_text_with_exact_character_count() -> None:
    characters = 2
    result: str = text_generator(characters)
    assert len(result) == characters
