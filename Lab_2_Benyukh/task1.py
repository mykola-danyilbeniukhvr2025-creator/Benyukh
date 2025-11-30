h = float(input("Введіть висоту жердини h: "))
a = float(input("Введіть скільки равлик піднімається за день a: "))
b = float(input("Введіть скільки равлик спускається за ніч b: "))

if a >= h:
    print("Равлик доповзе до вершини за 1 день")
else:
    day = 1
    height = a
    while height < h:
        height += a - b
        day += 1
    print(f"Равлик доповзе до вершини на {day} день")
