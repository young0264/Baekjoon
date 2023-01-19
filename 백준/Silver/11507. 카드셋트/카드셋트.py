s = input()
dic= dict()
dic['P'], dic['K'], dic['H'], dic['T'] = 13,13,13,13
length = len(s)
card_cnt = length//3
se = set()
for i in range(card_cnt):
    res = s[i*3:i*3+3]
    dic[res[0]] -= 1
    se.add(res)
if len(se) == card_cnt:
    print(dic['P'], dic['K'], dic['H'], dic['T'] )
else:
    print("GRESKA")
