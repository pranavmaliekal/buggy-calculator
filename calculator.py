def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def get_max(numbers):
    if len(numbers) == 0:
        return None
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)