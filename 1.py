L = []
k = int(input("Введите размер массива: "))
L = [int(input("Введите число: ")) for i in range(k)]
print(L)

delta = int(input("Введите DELTA: "))


for i in L:
	if i < delta:
		count = 0
		count += 1

print(len(list(filter(lambda x: x - delta == min(L), L))))