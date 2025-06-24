print("5 ta son kiriting:")
a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))
d = int(input("4-son: "))
e = int(input("5-son: "))

max_son = a
min_son = a

if b > max_son:
    max_son = b
if c > max_son:
    max_son = c
if d > max_son:
    max_son = d
if e > max_son:
    max_son = e

if b < min_son:
    min_son = b
if c < min_son:
    min_son = c
if d < min_son:
    min_son = d
if e < min_son:
    min_son = e

urtacha = (max_son + min_son) / 2
print("O‘rtacha:", urtacha)
