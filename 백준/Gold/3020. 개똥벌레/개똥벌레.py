import sys
n, h = map(int,input().split())
down_up = [0]*(h+1)
up_down = [0]*(h+1)
result = []
min_val = sys.maxsize
cnt = 0

for i in range(n):
    j = int(input())
    if i%2 == 0 :
        down_up[j] += 1
        # down_up.append(j)
    else :
        up_down[h-j+1] += 1
        # up_down.append(j)
# print(up_down)

h_arr = [0]*(h+1)

for i in range(h-1, -1, -1):
    down_up[i] += down_up[i+1]

for i in range(1,h+1):
    up_down[i] += up_down[i-1]

for i in range(1, h+1):
    res = (down_up[i] + up_down[i])
    result.append(res)
    if res < min_val:
        min_val = res
        cnt = 1
    elif res == min_val:
        cnt += 1

# print(down_up)
# print(up_down)
print(min_val, cnt)


