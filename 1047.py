input_of_problem = input()
initial_hour, initial_minute, final_hour, final_minute = map(int, input_of_problem.split())

hour = 0
minutes = 0

if initial_hour == final_hour and initial_minute == final_minute:
    hour = 24
    minutes = 0
else:
    hour = final_hour - initial_hour
    minutes = final_minute - initial_minute

if minutes < 0:
    minutes = 60 - abs(minutes)
    hour -= 1

if hour < 0:
    hour = 24 - abs(hour)

print(f'O JOGO DUROU {hour} HORA(S) E {minutes} MINUTO(S)')
