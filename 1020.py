raw_days = int(input())
year = int(raw_days / 365)
current_days = raw_days - (year * 365)
month = int(current_days / 30)
day = current_days % 30

print(f'{year} ano(s)')
print(f'{month} mes(es)')
print(f'{day} dia(s)')
