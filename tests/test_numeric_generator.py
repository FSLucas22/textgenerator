from textgenerator import numeric_generator


def test_should_generate_number_with_exact_length() -> None:
    number_length = 5
    result: str = numeric_generator(number_length)
    assert len(result) == number_length


def test_should_generate_generic_numeric_string() -> None:
    number_length = 5
    result: str = numeric_generator(number_length)
    assert result.isnumeric()
