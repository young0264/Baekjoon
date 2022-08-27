import sys
def input():
    return sys.stdin.readline().rstrip()
s = list(input())
length = len(s)
arr = []
for i in range(length):
    for j in range(i+1,length+1):    #0,1,2,3,4
        res=(s[i:j])
        arr.append(''.join(res))
print(len(list(set(arr))))