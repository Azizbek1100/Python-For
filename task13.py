print("5 ta telefon narxini kiriting:")
a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))
d = int(input("4: "))
e = int(input("5: "))

max_narx = a
min_narx = a

if b > max_narx:
    max_narx = b
if c > max_narx:
    max_narx = c
if d > max_narx:
    max_narx = d
if e > max_narx:
    max_narx = e

if b < min_narx:
    min_narx = b
if c < min_narx:
    min_narx = c
if d < min_narx:
    min_narx = d
if e < min_narx:
    min_narx = e

print("Eng arzon:", min_narx)
print("Eng qimmat:", max_narx)
