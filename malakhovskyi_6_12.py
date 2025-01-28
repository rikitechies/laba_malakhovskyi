n = input()
k = int(input())
a = ""

for i in n:
    b = ord(i)-k
    if b < 65:
        b = 91+(ord(i)-k-65)
        a = a + chr(b)
    else:
        a = a + chr(b)
print(a)