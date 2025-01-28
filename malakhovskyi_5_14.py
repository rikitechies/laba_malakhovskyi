"""
task 5_14: read intenger list
"""
n, k = [int(d) for d in input().split()]
a = list(map(int, input().split()))
b = sorted(a)
print(b[k-1])
