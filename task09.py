print("7 ta son kiriting:")
a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))
d = int(input("4-son: "))
e = int(input("5-son: "))
f = int(input("6-son: "))
g = int(input("7-son: "))

min_son = a
if b < min_son:
    min_son = b
if c < min_son:
    min_son = c
if d < min_son:
    min_son = d
if e < min_son:
    min_son = e
if f < min_son:
    min_son = f
if g < min_son:
    min_son = g

print("Eng kichik son:", min_son)
