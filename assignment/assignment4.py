number = 1234567
sum_digit = 0
while number > 0:
    sum_digit += number%10
    number //=10
    print(sum_digit)