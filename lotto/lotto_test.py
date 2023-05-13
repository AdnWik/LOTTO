from lotto import draw_numbers, check_win


def test_len_draw_numbers():
    score = draw_numbers()
    assert len(score) == 6

def test_equal_values_check_win():
    user_numbers = {1, 2, 3, 4, 5, 6}
    lottery_numbers = {1, 2, 3, 4, 5, 6}
    score = check_win(user_numbers, lottery_numbers)
    assert score == True

def test_different_values_check_win():
    user_numbers = {1, 2, 3, 4, 5, 6}
    lottery_numbers = {7, 2, 3, 4, 5, 6}
    score = check_win(user_numbers, lottery_numbers)
    assert score == False

def test_different_len_check_win():
    user_numbers = {1, 2, 3, 4, 5, 6}
    lottery_numbers = {1, 2, 3, 4, 5}
    score = check_win(user_numbers, lottery_numbers)
    assert score == False