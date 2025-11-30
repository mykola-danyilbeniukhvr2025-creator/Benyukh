n = int(input("Введіть число n: "))

for num in range(1, n + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    print(num, "+" * count)
