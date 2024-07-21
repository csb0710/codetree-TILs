from functools import cmp_to_key

def compare(x, y):
    templ = x + y
    tempr = y + x
    if templ > tempr:
        return -1
    if templ < tempr:
        return 1
    if templ == tempr:
        return 0

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

arr.sort(key=cmp_to_key(compare))

result = ""
for i in range(n):
    result += arr[i]

print(result)