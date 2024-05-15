# Forca Bruta que nao funcionou... Deu time limit exceeded. 2 segundos de runtime

value = float(input())
note_of_hundred = 0
note_of_fifty = 0
note_of_twenty = 0
note_of_ten = 0
note_of_five = 0
note_of_two = 0
coin_of_one_dollar = 0
coin_of_half_dollar = 0
coin_of_twenty_five_cents = 0
coin_of_ten_cents = 0
coin_of_five_cents = 0
coin_of_one_cent = 0

epsilon = 0.00001  # Pequena margem de erro

while abs(value) > epsilon:
    if value >= 100:
        note_of_hundred += 1
        value -= 100

    elif value >= 50:
        note_of_fifty += 1
        value -= 50

    elif value >= 20:
        note_of_twenty += 1
        value -= 20

    elif value >= 10:
        note_of_ten += 1
        value -= 10

    elif value >= 5:
        note_of_five += 1
        value -= 5

    elif value >= 2:
        note_of_two += 1
        value -= 2

    elif value >= 1:
        coin_of_one_dollar += 1
        value -= 1

    elif value >= 0.5:
        coin_of_half_dollar += 1
        value -= 0.5

    elif value >= 0.25:
        coin_of_twenty_five_cents += 1
        value -= 0.25

    elif value >= 0.10:
        coin_of_ten_cents += 1
        value -= 0.1

    elif value >= 0.05:
        coin_of_five_cents += 1
        value -= 0.05

    elif value >= 0.01:
        coin_of_one_cent += 1
        value -= 0.01


list_of_notes = [
    (100, note_of_hundred),
    (50, note_of_fifty),
    (20, note_of_twenty),
    (10, note_of_ten),
    (5, note_of_five),
    (2, note_of_two)
]

list_of_coins = [
    (1, coin_of_one_dollar),
    (0.50, coin_of_half_dollar),
    (0.25, coin_of_twenty_five_cents),
    (0.10, coin_of_ten_cents),
    (0.05, coin_of_five_cents),
    (0.01, coin_of_one_cent)
]


print('NOTAS:')
for current_note_value, number_of_notes in list_of_notes:
    print(f'{number_of_notes} nota(s) de R$ {current_note_value}.00')

print('MOEDAS:')
for current_coin_value, number_of_coins in list_of_coins:
    if current_coin_value >= 1:
        print(f'{number_of_coins} moeda(s) de R$ {current_coin_value},00')
    else:
        print(f'{number_of_coins} moeda(s) de R$ {current_coin_value:.2f}')
