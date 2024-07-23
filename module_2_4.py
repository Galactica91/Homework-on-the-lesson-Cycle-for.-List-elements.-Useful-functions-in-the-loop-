def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def split_numbers(numbers):
    prime_numbers = []
    composite_numbers = []

    for num in numbers:
        if is_prime(num):
            prime_numbers.append((num))
        else:
            composite_numbers.append(num)
    return prime_numbers, composite_numbers

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers, composite_numbers=split_numbers(numbers)
print("Even numbers: ", prime_numbers)
print("Odd numbers: ", composite_numbers)