from textgenerator import main
import pytest
import pyperclip


def test_main_can_generate_correct_length_word(capsys: pytest.CaptureFixture[str]) -> None:
    main(["3", "5"])
    captured_words = capsys.readouterr()
    assert captured_words.err == ""
    word_lengths = [len(word) for word in captured_words.out.split()]
    assert word_lengths == [3, 5]


def test_main_returns_zero_with_valid_inputs() -> None:
    return_code = main(["3", "5"])
    assert return_code == 0


def test_main_returns_one_with_input_zero() -> None:
    return_code = main(["5", "0"])
    assert return_code == 1


def test_main_returns_one_with_input_negative_input() -> None:
    return_code = main(["5", "-1"])
    assert return_code == 1


def test_main_can_copy_to_clipboard(monkeypatch: pytest.MonkeyPatch) -> None:
    class MockPyperclip:
        def __init__(self) -> None:
            self.copied = ''
        
        def copy(self, string: str) -> None:
            self.copied = string
    
    mock = MockPyperclip()
    monkeypatch.setattr(pyperclip, 'copy', mock.copy)

    main(["3", "5", "-c"])

    word_lengths = [len(word) for word in mock.copied.split()]
    assert word_lengths == [3, 5]
