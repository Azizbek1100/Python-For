n = int(input("n sonini kiriting: "))
juft = 0
toq = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        juft += i
    else:
        toq += i

print("Juft yig‘indisi:", juft)
print("Toq yig‘indisi:", toq)
