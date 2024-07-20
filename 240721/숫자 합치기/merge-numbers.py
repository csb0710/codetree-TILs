import heapq

n = int(input())
uinput = input()
arr = list(map(int, uinput.split()))

heapq.heapify(arr)
result = 0

while len(arr) > 1:
    f = heapq.heappop(arr)
    s = heapq.heappop(arr)
    temp = f + s
    result += temp
    heapq.heappush(arr, temp)


print(result)