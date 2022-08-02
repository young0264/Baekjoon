def solution(record):
        
    answer = []
    dic = dict()
    for i in record:
        arr = i.split(" ")
        lang = ""
        
        if arr[1] not in dic:
            dic[arr[1]] = arr[2]
        ex_name = dic[arr[1]]
        
        if arr[0] == "Enter":   #now_name 찾아 다 바꾸고 append
            dic[arr[1]] = arr[2]
            lang = arr[1] +" 님이 들어왔습니다."
            answer.append(lang)
            
        elif arr[0] == "Leave": #append
            lang = arr[1] + " 님이 나갔습니다."
            answer.append(lang)
            "님이 나갔습니다."
        else:#arr[0] == "Change"
            dic[arr[1]] = arr[2]
            
    for i in range(len(answer)):
        l = answer[i].split(" ")
        answer[i] = answer[i].replace(l[0]+" ",dic[l[0]])

    return answer