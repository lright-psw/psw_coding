N = int(input())

year = 2024
month = 8

months_to_add = (N - 1) * 7
month += months_to_add

year += (month - 1) // 12
month = (month - 1) % 12 + 1

print(year, month)
