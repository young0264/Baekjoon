def solution(fees, records):
    answer = []
    car_number = []
    time_dic = dict()   #자동차 in시간 적고 out이면 0으로 초기화
    timesave_dic = dict()   #자동차 out-in 시간 저장해놓은거

    for r in records:
        x = r.split(" ")
        x0 = x[0].split(":")
        if x[1] not in car_number : car_number.append(x[1])
        if x[2]=="IN":  #"05:34 5961 IN", in이면 timedic에 시간을넣고
            time_dic[x[1]] = int(x0[0])*60 + int(x0[1])
            if x[1] not in timesave_dic:
                timesave_dic[x[1]] = 0

        elif x[2] == "OUT":
            take_time = (int(x0[0]) * 60 + int(x0[1])) - time_dic[x[1]]
            if x[1] not in timesave_dic :
                timesave_dic[x[1]] = take_time
            else:
                timesave_dic[x[1]] += take_time
            time_dic[x[1]] = -1 #출차되면 time_dic은 0으로 만들어주고

    car_number.sort()
    lasttime = 23*60 + 59
    for num in car_number:
        fee = 0

        if time_dic[num] == -1:
            fee+=fees[1]
            if (timesave_dic[num]-fees[0])%fees[2] == 0:
                fee+=((timesave_dic[num] - fees[0]) // fees[2])*fees[3]
            else:
                fee += ((timesave_dic[num] - fees[0]) // fees[2]) * fees[3] + fees[3]
        else:
            timesave_dic[num] += lasttime - time_dic[num]
            fee += fees[1]
            if (timesave_dic[num] - fees[0]) % fees[2] == 0:
                fee += ((timesave_dic[num] - fees[0]) // fees[2]) * fees[3]
            else:
                fee += ((timesave_dic[num] - fees[0]) // fees[2]) * fees[3] + fees[3]
        if fee<fees[1]:
            fee = fees[1]
        answer.append(fee)

    return answer