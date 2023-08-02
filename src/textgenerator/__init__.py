from collections.abc import Sequence
from typing import Callable


def text_generator(word_lengths: Sequence[int], word_generator: Callable[[int], str]) -> str:
    return ' '.join(map(word_generator, word_lengths))


def word_generator(characters: int) -> str:
    return "a"*characters


def numeric_generator(number_length: int) -> str:
    return "1"*number_length
