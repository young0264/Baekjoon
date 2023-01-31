from math import *

arr = [0]*(1000001)
arr[0] = 1

for i in range(1,1000001):
    arr[i] = arr[floor(i-sqrt(i))] + arr[floor(log(i))] + arr[floor(i*sin(i)*sin(i))]

while True:
    n = int(input())
    if n== -1:
        break
    print(arr[n]%1000000)