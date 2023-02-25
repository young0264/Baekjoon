arr = []
brr = []

for _ in range(10):
    n = int(input())
    arr.append(n)

for _ in range(10):
    n = int(input())
    brr.append(n)

arr.sort()
brr.sort()
print(arr[-1]+arr[-2]+arr[-3], brr[-1]+brr[-2]+brr[-3])
