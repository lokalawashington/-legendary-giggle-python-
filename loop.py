a = ["banana", "apple","microsoft"]

for element in a :
	print(element)


b = [1,3,4,5,6,6,7,7,8]
total = 0
for e in b:
	print(e)
	total = total + e
	print(total)

#range(1, 5)
c = list(range(1, 5))
print(c)

total2 = 0
for d in range(1, 5):
	total2 += d
	print(total2)

print(list(range(1, 8)))
total3 = 0
for i in range(1, 8):
	if i % 3 == 0 :
		total3 += i
		print(total3)


