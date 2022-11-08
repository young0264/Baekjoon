n = int(input())
dic = dict()
dic[0],dic[2] = 2,2
dic[1] = 1
dic[3], dic[7] = 3,3
dic[6],dic[4] = 4,4
dic[5] = 5
print(dic[n%8])