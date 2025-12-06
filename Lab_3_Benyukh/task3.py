import matplotlib.pyplot as plt


with open("text", "r") as f:
    text = f.read().lower()


vowels = "aeiou"
freq = {v: 0 for v in vowels}

for ch in text:
    if ch in vowels:
        freq[ch] += 1

plt.bar(freq.keys(), freq.values())
plt.xlabel("Голосні")
plt.ylabel("Частота")
plt.title("Частота появи голосних у тексті")

plt.savefig("histogram.png")
plt.close()

print("Гістограму збережено у файл histogram.png")
