def add(a, b):
    return a - b  # bug: subtraction instead of addition

def is_even(n):
    return n % 2 == 1  # bug: this actually checks for odd

def get_max(numbers):
    if len(numbers) == 0:
        return None
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest  # this one is actually correct — a control case

def average(numbers):
    return sum(numbers) / len(numbers)  # bug: no check for empty list (ZeroDivisionError)