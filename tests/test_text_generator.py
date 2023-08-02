from textgenerator import text_generator


def test_should_return_text_based_on_word_lengths_and_word_generator() -> None:
    word_lengths = [2, 3]
    word_generator = lambda characters: "x"*characters
    result: str = text_generator(word_lengths, word_generator)
    assert result == "xx xxx"
