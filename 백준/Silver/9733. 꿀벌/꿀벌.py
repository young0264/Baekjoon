crr = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
arr = []
while True:
    try:
        brr = list(map(str, input().split()))
        if not brr:
            break
    except EOFError:
        break
    arr = arr+brr
    # print(arr)

length = len(arr)
dic = dict()

for a in arr:
    dic[a] = dic.get(a, 0) + 1

for c in crr:
    if c in dic:
        res = (dic[c] / length)
        print(c, dic[c],'{:.2f}'.format(res) )
    else:
        print(c, 0, '0.00')
print('Total', length, '1.00')
