n = int(input())
uinput = input()
arr = list(map(int, uinput.split()))

result = 0

while len(arr) > 1:
    arr.sort()
    f = arr.pop(0)
    s = arr.pop(0)
    temp = f + s
    result += temp
    arr.append(temp)

print(result)