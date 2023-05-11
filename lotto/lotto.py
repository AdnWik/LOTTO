from random import choice


def draw_numbers(num_of_numbers=4):
    numbers = [number for number in range(1, 50)]
    result = set()
    while len(result) != num_of_numbers:
        result.add(choice(numbers))

    return result

def check_win(user_numbers, function) -> bool:
    x = user_numbers
    y = function()
    print(f'{x} --- {y}')
    #return user_numbers == function()
    return x == y

my_numbers = {8, 11, 1, 17}
number_of_samples = 0

while True:
    number_of_samples += 1
    if check_win(my_numbers, draw_numbers):
        break
lottery_ticket_cost = 3
total_cost = number_of_samples * lottery_ticket_cost
weeks = number_of_samples /3
months = weeks / 4
years = months / 12

print('\n')
print('YOU WIN!')
print(f'Total cost: {total_cost:,} PLN.')
print(f'Weeks: {weeks:,.1f}')
print(f'Months: {months:,.1f}')
print(f'Years: {years:,.1f}')



# liczby od 1 do 49
# w karzdym losowaniu 6 liczb
# 3 losowania w tygodniu
# 3 zł za jeden zakład

#Dodatkowo
# - sprawdzaj tez 5,4,3 zanim wylosowałeś 6
# - sprawdz ile dni, tygodni, miesięcy, lat zajeło trafienie 6ki
# - sprawdź ile lat bedziesz miał gdy trafisz
#


