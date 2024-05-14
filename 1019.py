# first mode
# raw_time = int(input())
#
# second = raw_time % 60
# minute = int(int(raw_time / 60) % 60)
# hour = int(int(raw_time / 60) / 60)
#
# print(f'{hour}:{minute}:{second}')

# second mode
raw_time = int(input())
hour = int(raw_time / 3600)
current_time = raw_time - (hour * 3600)
minute = int(current_time / 60)
second = current_time % 60
print(f'{hour}:{minute}:{second}')
