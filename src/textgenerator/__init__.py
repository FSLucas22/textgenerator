from collections.abc import Sequence
from typing import Callable, Optional
from functools import partial
import string
import random
import argparse


def argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generates random strings separated by spaces")
    parser.add_argument("string_lengths", type=int, nargs='+', help='length of the string to be generated')
    return parser


def main(args: Optional[Sequence[str]] = None) -> int:
    parser = argument_parser()
    parsed_args = parser.parse_args(args)

    if 0 in parsed_args.string_lengths or -1 in parsed_args.string_lengths:
        return 1
    
    print(text_generator(parsed_args.string_lengths, string_generator))
    return 0


StringGenerator = Callable[[int], str]  # Used to return strings with specified length
CharGenerator = Callable[[], str]  # Used to return strings with length = 1


def text_generator(word_lengths: Sequence[int], string_generator: StringGenerator) -> str:
    return ' '.join(map(string_generator, word_lengths))


def random_letter() -> str:
    return random.choice(string.ascii_letters)


def string_generator(characters: int, char_generator: CharGenerator = random_letter) -> str:
    return ''.join([char_generator() for _ in range(characters)])


def random_digit() -> str:
    return str(random.randint(0, 9))


numeric_generator = partial(string_generator, char_generator=random_digit)


if __name__ == "__main__":
    exit(main())
