from collections.abc import Sequence
from typing import Callable
from functools import partial

import random


WordGenerator = Callable[[int], str]
LetterGenerator = Callable[[], str]


def text_generator(word_lengths: Sequence[int], word_generator: WordGenerator) -> str:
    return ' '.join(map(word_generator, word_lengths))


def random_letter() -> str:
    letter_codes = list(range(65, 91)) + list(range(97, 122))
    return chr(random.choice(letter_codes))


def word_generator(characters: int, letter_generator: LetterGenerator = lambda: "a") -> str:
    return ''.join([letter_generator() for _ in range(characters)])


def random_digit() -> str:
    return str(random.randint(0, 9))


numeric_generator = partial(word_generator, letter_generator=random_digit)
