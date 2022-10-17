n = int(input())
arr = []
for _ in range(n):
    s = input()
    arr.append(s)
tmp = arr[:]
tmp.sort()
if arr == tmp:
    print('INCREASING')
    exit(0)
tmp = arr[:]
tmp.sort(reverse=True)
if arr == tmp:
    print('DECREASING')
    exit(0)
else:
    print("NEITHER")