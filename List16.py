numbers = list(range(1, 40))
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(f"That are the even numbers: {evens}")
print(f"That are the odd numbers: {odds}")
