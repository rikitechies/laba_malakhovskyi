import string

n = input() 

a = ""
for i in n:
    if i in string.ascii_letters:
        a = a + i + i
    else:
        a = a + i
print(a)