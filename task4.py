a = int(input())
max_digit = 0
while a != 0:
    if a % 10 > max_digit:
        max_digit = a % 10
    a //= 10
print(max_digit)