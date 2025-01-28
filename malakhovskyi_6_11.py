import string

n = input()
a = 0

for i in n:
    if i in n and i in string.digits:
        a += 1
        break

for i in n:
    if i in n and i in string.ascii_lowercase:
        a += 1
        break

for i in n:
    if i in n and i in string.ascii_uppercase:
        a += 1
        break

for i in n:
    if i in n and i in string.punctuation:
        a += 1
        break

if len(n) >= 8:
        a += 1

print(a)