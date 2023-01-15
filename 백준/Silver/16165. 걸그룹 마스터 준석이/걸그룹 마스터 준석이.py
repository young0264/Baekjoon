n, m = map(int, input().split())
team_dic = dict()
member_dic = dict()

for i in range(n):
    team_name = input()
    team_num = int(input())

    for j in range(team_num):
        member = input()
        # team_dic[team_name] = team_dic.get(team_name,member).append(member)
        if team_name in team_dic:
            team_dic[team_name].append(member)
        # team_dic[team_name].append(member)
        else:
            team_dic[team_name] = [member]
        member_dic[member] = team_name

for i in range(m):
    s = input()
    k = int(input())
    if k == 1:
        print(member_dic[s])
    else:
        team_dic[s].sort()
        for j in team_dic[s]:
            print(j)
