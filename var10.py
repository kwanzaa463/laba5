n = int(input("Введите количество целых чисел N:"))
print(f"Введите {n} целых чисел через пробел:")
numbers = list(map(int, input().split()))
first_abs = abs(numbers[0])

count = sum(1 for x in numbers if abs(x) == first_abs)

print(count)
    
