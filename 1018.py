value = int(input())
print(value)

note_of_hundred = 0
note_of_fifty = 0
note_of_twenty = 0
note_of_ten = 0
note_of_five = 0
note_of_two = 0
note_of_one = 0

while value > 0:
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
        note_of_one += 1
        value -= 1

list_of_notes = [
    (100, note_of_hundred),
    (50, note_of_fifty),
    (20, note_of_twenty),
    (10, note_of_ten),
    (5, note_of_five),
    (2, note_of_two),
    (1, note_of_one)
]

for current_note_value, number_of_notes in list_of_notes:
    print(f'{number_of_notes} nota(s) de R$ {current_note_value},00')
