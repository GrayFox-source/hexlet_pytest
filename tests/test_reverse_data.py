from pathlib import Path
import pytest

from hexlet_pytest.example import reverse


@pytest.fixture
def test_data_dir():
    return Path(__file__).parent / "test_data"


def read_test_file(test_data_dir: Path, filename: str) -> str:
    return (test_data_dir / filename).read_text(encoding="utf-8")


def test_reverse_long_text(test_data_dir):
    input_text = read_test_file(test_data_dir, "long_text.txt")
    expected = read_test_file(test_data_dir, "reversed_text.txt")
    actual = reverse(input_text)
    assert actual == expected
