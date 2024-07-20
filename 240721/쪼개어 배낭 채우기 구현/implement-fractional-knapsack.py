n, m = map(int, input().split())

arr = []

for _ in range(n):
    w, v = map(int, input().split())
    arr.append([w, v, v / w])

arr = sorted(arr, key=lambda x: x[2])
result = 0

for i in range(n):
    tempw, tempv, temp = arr[n-1-i]
    if m < tempw:
        result += temp * m
        m = 0
    else:
        result += tempv
        m -= tempw
    if m == 0:
        break

print(f'{result:.3f}')