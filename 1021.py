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

# Convertendo o valor para centavos para evitar problemas de precisão com ponto flutuante
value = int(round(value * 100))

note_of_hundred = value // 10000
value %= 10000

note_of_fifty = value // 5000
value %= 5000

note_of_twenty = value // 2000
value %= 2000

note_of_ten = value // 1000
value %= 1000

note_of_five = value // 500
value %= 500

note_of_two = value // 200
value %= 200

coin_of_one_dollar = value // 100
value %= 100

coin_of_half_dollar = value // 50
value %= 50

coin_of_twenty_five_cents = value // 25
value %= 25

coin_of_ten_cents = value // 10
value %= 10

coin_of_five_cents = value // 5
value %= 5

coin_of_one_cent = value // 1
value %= 1

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
        print(f'{number_of_coins} moeda(s) de R$ {current_coin_value:.2f}')
    else:
        print(f'{number_of_coins} moeda(s) de R$ {current_coin_value:.2f}')
