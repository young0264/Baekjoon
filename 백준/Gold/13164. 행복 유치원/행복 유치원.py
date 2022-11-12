n,k = map(int,input().split())
arr = list(map(int,input().split()))

brr = []

for i in range(n-1):
    brr.append(abs(arr[i] - arr[i+1]))
num = sum(brr)

brr.sort(reverse=True)


for i in range(k-1):
    num -= brr[i]

print(num)