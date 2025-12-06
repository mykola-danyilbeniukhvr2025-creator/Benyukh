B = [ -4, 0, 3, -4, -1, -2, 1, 5, 7]

pos = []

for i in range(len(B)):
    if B[i] > 0:
        pos.append(i)

print(pos)

if len(pos) >= 2:
    p = 1
    for x in B[pos[0]+1 : pos[1]]:
        p *= x
    print(p)
else:
    print("Потрібно мінімум два додатних елементи")
