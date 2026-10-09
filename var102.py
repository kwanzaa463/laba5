n = int(input("Введите количество чисел N:"))
print(f"Введите {n} чисел через пробел:")
numbers = list(map(int, input().split()))
count = 0
total_sum = 0
for num in numbers:
    if num % 5 == 0 and num % 10 != 0:
        count += 1
        total_sum += num

print(f"Количество элементов: {count}")
print(f"Суммф таких элементов: {total_sum}")
