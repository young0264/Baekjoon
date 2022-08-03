import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
arr = list(sorted(map(int,input().split())))
pos = [0,0]
answer = 0
for i in range(n):
    new_pos=[pos[0]+arr[i],pos[1]+arr[i]]
    if i==0 and arr[i]==1:
        pos[1] = 1
    elif i==0 and arr[i] != 1:
        print(1)
        exit(0)
    elif new_pos[0] <= pos[1]+1<= new_pos[1]:
        pos[1] = new_pos[1]
    else:
        break
answer = pos[1]+1
print(answer)