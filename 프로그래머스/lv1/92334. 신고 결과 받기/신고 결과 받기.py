def solution(id_list, report, k):
    report = list(set(report))
    answer = []
    dic = dict()
    bad_users_arr = []
    answer_dic = dict()
#####
    # for i in id_list:  # id_list dic key로 만들기
    #     dic[i] = 0
    # for bad_users in report:
    #     bad_users = bad_users.split()
    #     if bad_users[0] not in answer_dic:
    #         answer_dic[bad_users[0]] = [bad_users[1]]
    #     else:
    #         answer_dic[bad_users[0]].append(bad_users[1])
    #     dic[bad_users[1]] += 1
####    
    for v in report :
        report_user, bad_user = v.split()
        dic[bad_user] = dic.get(bad_user,0)+1 #dic
        answer_dic[report_user] = answer_dic.get(report_user,[]) + [bad_user]
        # print("ansdic = ", answer_dic)
        
    for key in dic:
        if dic[key] >= k:
            bad_users_arr.append(key)

    for key in id_list:
        cnt = 0
        if key not in answer_dic:
            answer.append(0)
            continue
        for v in answer_dic[key]:
            if v in bad_users_arr:
                cnt += 1
        answer.append(cnt)

    return answer