import math

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    flag = 0
    length = int(math.sqrt(n))+1
    for x in range(1,length):
        if x ** 2  == n:
            cnt += 1
            continue
        elif x ** 2 > n:
            break
        for y in range(x,length):
            if x ** 2 + y ** 2 == n:
                cnt += 1
                continue
            elif x ** 2 + y ** 2 > n:
                break
            for z in range(y,length):
                if x ** 2 + y ** 2 + z ** 2 == n:
                    cnt += 1
                    continue
                elif x ** 2 + y ** 2 + z ** 2 > n:
                    break
                for w in range(z,length):
                    if x**2 + y**2 + z**2 + w**2 == n:
                        cnt += 1
                        continue
                    elif x**2 + y**2 + z**2 + w**2 > n:
                        break
    print(cnt)