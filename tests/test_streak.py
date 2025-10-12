from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_and_negatives():
    assert longest_positive_streak([-1, -2, 0, -4]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_element_positive():
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    assert longest_positive_streak([-5]) == 0

def test_mixed_streaks():
    assert longest_positive_streak([1, 0, 2, 2, 0, 3, 3, 3]) == 3

def test_long_streak():
    assert longest_positive_streak([1] * 1000) == 1000

def test_large_list_with_no_streak():
    assert longest_positive_streak([-1, 0] * 500) == 0

def test_interspersed_positives_and_negatives():
    assert longest_positive_streak([1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
