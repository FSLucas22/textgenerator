from collections.abc import Sequence
from typing import Callable
from functools import partial

import random


StringGenerator = Callable[[int], str]  # Used to return strings with specified length
CharGenerator = Callable[[], str]  # Used to return strings with length = 1


def text_generator(word_lengths: Sequence[int], string_generator: StringGenerator) -> str:
    return ' '.join(map(string_generator, word_lengths))


def random_letter() -> str:
    letter_codes = list(range(65, 91)) + list(range(97, 122))
    return chr(random.choice(letter_codes))


def string_generator(characters: int, char_generator: CharGenerator = random_letter) -> str:
    return ''.join([char_generator() for _ in range(characters)])


def random_digit() -> str:
    return str(random.randint(0, 9))


numeric_generator = partial(string_generator, char_generator=random_digit)
