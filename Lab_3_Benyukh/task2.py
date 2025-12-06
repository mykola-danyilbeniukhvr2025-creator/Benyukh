f = open("letters.txt", "w")
for i in range(1, 10):
    f.write("a" * i + "\n")
f.close()
