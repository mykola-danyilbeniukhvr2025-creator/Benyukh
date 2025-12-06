B = [ -4, 0, 3, -4, -1, -2, 1, 5, 7]

pos = [i for i, v in enumerate(B) if v > 0]

if len(pos) >= 2:
    p = 1
    for x in B[pos[0]+1 : pos[1]]:
        p *= x
    print(p)
else:
    print("Потрібно мінімум два додатних елементи")
