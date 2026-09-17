# HIGHER ORDER FUNCTIONS

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_one(first_values,second_values,f_sum):
    return f_sum(first_values + second_values)

print(sum_two_values_and_add_one(5,4,sum_one))
print(sum_two_values_and_add_one(5,4,sum_five))

# CLOSURES

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(5)
print(add_closure(5))
print(sum_ten(5)(5))

# Built-in Higher Order Functions
numbers = [2,5,10,21,2,11]
# Map
def multiply_two(number):
    return number * 2

print(multiply_two(numbers))
print(list(map(multiply_two,numbers)))
print(list(map(lambda number: number * 2,numbers)))

# FILTER

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# REDUCE

def sum_two_value(first_value,second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_value,numbers))