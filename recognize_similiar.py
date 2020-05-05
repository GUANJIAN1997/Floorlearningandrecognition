import json
import numpy as np
filepath = "/Users/jianguan/Desktop/毕业/楼层判定实验数据/test1356.json"
from recognize_test2 import find_floor
import scipy.stats

def json2List(filepath):
    rowdata = []
    f = open(filepath,"r")
    for line in f:
        decodes = json.loads(line)
        rowdata.append(decodes)
    f.close()
    return rowdata

def get_barometric():
    barometric_data = []
    barometric_data_HZ = []
    transfer_list = []
    a = json2List(filepath)
    for i in a:
        if "hpa" in i:
            transfer_list.append(i["hpa"])
        if "nodeId" in i:
            barometric_data.append(transfer_list)
            transfer_list = []
    barometric_data.append(transfer_list)
    # print(barometric_data)
    for i in barometric_data:
        barometric_data_HZ.append(round(np.median(i), 4))
    # array = np.array(barometric_data_HZ)
    # np.savetxt("/Users/jianguan/Desktop/result3.txt", array)
    return barometric_data_HZ    #得到1.5s的一个气压
# s = get_barometric()
# print(s)

def upordown(gb):
    num = 0
    test = []
    upordown_num = []
    # upordown_barometric = []

    for num in range(len(gb)-3):
        if (abs(gb[num] - gb[num + 1]) >=0.027 and abs(gb[num + 1] - gb[num + 2]) >= 0.027):
            upordown_num.append(num)

        elif abs(gb[num] - gb[num + 1]) < 0.045 and abs(gb[num + 1] - gb[num + 2]) < 0.045 and abs(gb[num + 2] - gb[num + 3]) < 0.045 :
            test.append(gb[num])
        else:
            upordown_num.append(num)

    # print(upordown_num)

    return test,upordown_num     #得到删除上下楼之后气压值还有上下楼时候的气压编号

# a = upordown(get_barometric())
# print(a)

def get_wifi_bro():

    barometric_data_HZ = get_barometric()
    rowdata = json2List(filepath)

    wifi_data = []
    wifi_data_dic_list = []
    transfer_list = []
    transfer_list2 = []

    num_wifi = 0
    num_wifi_list = []
    for i in rowdata:
        if "nodeId" in i:
            transfer_list = []
            for j in i["scanResults"]:
                # print(j)
                if j["essid"] == "Rits-Webauth" or j["essid"] == "eduroam":
                    transfer_list.append(j["bssid"])
                    transfer_list2.append(j["rssi"])
                    transfer_list.append(transfer_list2)
                    transfer_list2 = []

            # print(transfer_list)
            wifi_data.append(transfer_list)
            num_wifi = num_wifi + 1
            if not transfer_list:
                num_wifi_list.append(num_wifi)





    for i in wifi_data:
        wifi_data_dic = dict(zip(i[::2],i[1::2]))
        wifi_data_dic_list.append(wifi_data_dic)
    num = 0
    for i in wifi_data_dic_list:
        # print(i)
        for j in i:
            # print(j)
            i[j].append(barometric_data_HZ[num])

        num = num + 1

    return wifi_data_dic_list      #得到MAC地址字典值是列表形式的rssi和对应的气压值（每1.5秒一个字典）

# print(get_wifi_bro())

def learned_floor_processing():
    learned_floor_dic = find_floor()
    del_key = []
    for i in learned_floor_dic:
        del_key_i = []
        for key in i:
            if len(i[key])<2:
                del_key_i.append(key)
        del_key.append(del_key_i)

    for i in range(7):
        if del_key[i]:
            for j in del_key[i]:
                learned_floor_dic[i].pop(j)



    for i in learned_floor_dic:
        for key in i:
            minimaze = np.mean(i[key]) - 2 * np.std(i[key],ddof=1)
            maximaze = np.mean(i[key]) + 2 * np.std(i[key],ddof=1)
            i[key] = []
            i[key].append(minimaze)
            i[key].append(maximaze)
    return learned_floor_dic

def getmaxbarometric():
    wifi_data_dic_list = get_wifi_bro()
    learned_floor_dic = learned_floor_processing()

    upordown_number = upordown(get_barometric())[1]
    deleted_upordown_number2  = list(range(len(get_barometric()) - 1))

    for i in upordown_number:
        deleted_upordown_number2[i] = "階層移動"     #把上下楼的标号标注階層移動*******代替deleted_upordown_number


    wifi_floor_list = []
    floor_barometric = []
    floor_barometric_difference = []
    boolean = True
    one_floor = []
    fingerprint = []
    similationWiFi = []
    jiao = []
    distance = []
    distancefinal = []
    for i in range(len(deleted_upordown_number2)):              #1.5一个，编号，0到总个数，其中上下楼的编号已经被标注成"階層移動"
        if deleted_upordown_number2[i] != "階層移動":

            for key in wifi_data_dic_list[i]:          #1.5秒的wifi数据
                if key not in one_floor:
                    if wifi_data_dic_list[i][key][0] > -90:
                        one_floor.append(key)
                        one_floor.append(wifi_data_dic_list[i][key])      #添加bssid和对应的rssi和气压（新的bssid）
                elif wifi_data_dic_list[i][key][0] > -90:
                    one_floor[one_floor.index(key)+1].insert(len(one_floor[one_floor.index(key)+1])-1,wifi_data_dic_list[i][key][0])
            one_floor_dic = dict(zip(one_floor[0::2],one_floor[1::2]))
            baro = 0
            for key in one_floor_dic:
                if one_floor_dic[key][-1] > 1:
                    baro = one_floor_dic[key].pop()
                minimaze = round((np.mean(one_floor_dic[key]) - 1*np.std(one_floor_dic[key])),2)
                maximaze = round((np.mean(one_floor_dic[key]) + 1*np.std(one_floor_dic[key])),2)
                one_floor_dic[key] = []
                one_floor_dic[key].append(minimaze)
                one_floor_dic[key].append(maximaze)

            jiao_7 = []
            for i in learned_floor_dic:
                if len(list(set(list(i.keys())) & set(list(one_floor_dic.keys())))):
                    jiao_7.append(list(set(list(i.keys())) & set(list(one_floor_dic.keys()))))
                else:
                    jiao_7.append([])

            jiao.append(jiao_7)

            jiao_similiar = []
            for i in range(7):
                jiao_similiar_i = []
                if jiao_7[i]:
                    for j in jiao_7[i]:

                        if min(learned_floor_dic[i][j]) < min(one_floor_dic[j]) and max(learned_floor_dic[i][j]) > max(one_floor_dic[j]):
                            jiao_similiar_i.append(j)
                jiao_similiar.append(jiao_similiar_i)


            P = []
            P2=[]
            for i in range(7):
                P.append(len(jiao_similiar[i])/len(set(list(learned_floor_dic[i].keys())) | set(list(one_floor_dic.keys()))))
                P2.append(len(jiao_similiar[i]))


            # print(one_floor_dic)

            print("————————————————————————————————————————認識中————————————————————————————————————————")

            # print(jiao_similiar)
            print(P)
            print(str(len(jiao))+"秒が経ちました")





        else:

            print("————————————————————————————————————————————————————————————————————————————————階層移動————————————————————————————————————————————————————————————————————————————————")
            one_floor = []






    return wifi_floor_list


getmaxbarometric()


