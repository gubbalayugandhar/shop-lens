import re

def sum_and_last_divisible_by_3(string):
    numbers = [int(num) for num in re.findall(r'\d+', string)]
    total_sum = 0
    last_divisible = None

    for num in numbers:
        if num % 3 == 0:
            total_sum += num
            last_divisible = num
    
    return total_sum, last_divisible

input_string = "The best 6 of 8 will get 9 points"
result_sum, last_divisible = sum_and_last_divisible_by_3(input_string)
print("Total sum of numbers divisible by 3:", result_sum)
print("Last number divisible by 3:", last_divisible)
