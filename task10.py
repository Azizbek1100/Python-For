print("7 ta son kiriting:")
a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))
d = int(input("4-son: "))
e = int(input("5-son: "))
f = int(input("6-son: "))
g = int(input("7-son: "))

max_son = a
if b > max_son:
    max_son = b
if c > max_son:
    max_son = c
if d > max_son:
    max_son = d
if e > max_son:
    max_son = e
if f > max_son:
    max_son = f
if g > max_son:
    max_son = g

print("Eng katta son:", max_son)
