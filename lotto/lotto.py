from random import choice


def draw_numbers(num_of_numbers=6) -> set:
    """Draw n numbers from 1 to 49

    Args:
        num_of_numbers (int, optional): Number of numbers to draw.
                                        Defaults = 6.

    Returns:
        set: set with n draw numbers
    """
    numbers = [number for number in range(1, 50)]
    result = set()
    while len(result) != num_of_numbers:
        result.add(choice(numbers))

    return result


def check_win(numbers_to_check, function) -> bool:
    """ Compare drawn_numbers with user_numbers
        if True user win

    Args:
        user_numbers (set): set with user numbers
        function (set): set with drawn numbers

    Returns:
        bool: If True user win
    """
    if __name__ == "__main__":
        drawn_numbers = function()
    else:
        drawn_numbers = function
    
    if len(numbers_to_check) == len(drawn_numbers):
        return numbers_to_check == drawn_numbers
    else:
        return False


def collect_user_numbers() -> set:
    """Collect six unique numbers from 1 to 49 from user

    Returns:
        set: set of user numbers
    """
    user_numbers = set()
    print('Give your 6 unique numbers from 1 to 49')
    while len(user_numbers) != 6:
        number = int(input('Give your number: '))
        if number in range(1, 50):
            user_numbers.add(number)
    return user_numbers

if __name__ == "__main__":
    user_numbers = collect_user_numbers()
    number_of_samples = 0

    print('\nLottery in progress, please wait...')
    while True:
        number_of_samples += 1
        if check_win(user_numbers, draw_numbers):
            break
    lottery_ticket_cost = 3
    total_cost = number_of_samples * lottery_ticket_cost
    weeks = number_of_samples / 3
    months = weeks / 4
    years = months / 12

    print('\n')
    print('YOU WIN!')
    print(f'Total cost: {total_cost:,} PLN.')
    print(f'Weeks: {weeks:,.1f}')
    print(f'Months: {months:,.1f}')
    print(f'Years: {years:,.1f}')
