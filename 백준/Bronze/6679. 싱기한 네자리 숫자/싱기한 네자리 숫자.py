
def find(num, a):
    res = 0
    while num > 0:
        n, m = divmod(num, a)
        # res.append(m)
        res += m
        num = n
    # print("res",res)
    return res

answer = 0
for num in range(1000, 10000):
    z = find(num,10)
    a = find(num,12)
    b = find(num,16)
    if a == b and b==z:
        print(num)


