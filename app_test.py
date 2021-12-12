from app import sum_numbers


def test_sum():
    result = sum_numbers(1, 2)
    assert result == 3
