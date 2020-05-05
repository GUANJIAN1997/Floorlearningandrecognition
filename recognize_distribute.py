import json
import numpy as np
filepath = "/Users/jianguan/Desktop/毕业/楼层判定实验数据/test1234567.json"
from recognize_test import find_floor
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




def getmaxbarometric():

    learned_floor = find_floor()
    learned_floor_dic = []
    for i in learned_floor:
        learned_floor_dic.append(dict(zip(i[0::2],i[1::2])))

    wifi_data_dic_list = get_wifi_bro()



    # deleted_upordown_number = set(list(range(len(get_barometric())-1)))-set(upordown(get_barometric())[1]) #删除上下楼的数据的标号之后的标号
    upordown_number = upordown(get_barometric())[1]
    deleted_upordown_number2  = list(range(len(get_barometric()) - 1))
    # print(upordown_number)
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
    print(wifi_data_dic_list[0])
    for i in range(len(deleted_upordown_number2)):              #1.5一个，编号，0到总个数，其中上下楼的编号已经被标注成"階層移動"
        if deleted_upordown_number2[i] != "階層移動":

            for key in wifi_data_dic_list[i]:          #1.5秒的wifi数据
                if key not in one_floor:
                    if wifi_data_dic_list[i][key][0] > -100:
                        one_floor.append(key)
                        one_floor.append(wifi_data_dic_list[i][key])      #添加bssid和对应的rssi和气压（新的bssid）

                elif wifi_data_dic_list[i][key][0] > -100:
                    one_floor[one_floor.index(key)+1].insert(len(one_floor[one_floor.index(key)+1])-1,wifi_data_dic_list[i][key][0])

            similation_7 = []
            jiao_7 = []
            for i in learned_floor:
                if len(list(set(i[0::2]) & set(one_floor[0::2]))):
                    similation_7.append(len(list(set(i[0::2]) | set(one_floor[0::2]))) / len(list(set(i[0::2]) & set(one_floor[0::2]))))
                    jiao_7.append(list(set(i[0::2]) & set(one_floor[0::2])))
                else:
                    similation_7.append(0)
                    jiao_7.append([])
            similationWiFi.append(similation_7)   #wifi的类似度
            jiao.append(jiao_7)                    #现在目前累计得到的bssid和学习到的每层的bssid的交集

            #目前累计收到的信号计算概率分布
            one_floor_dic = dict(zip(one_floor[0::2], one_floor[1::2]))
            floor7_pro = []
            for i in range(len(jiao_7)):
                transfer1 = []
                if jiao_7[i]:
                    for k in jiao_7[i]:
                        transfer1.append(k)
                        transfer2 = []
                        count1 = 0
                        count2 = 0
                        count3 = 0
                        count4 = 0
                        count5 = 0
                        count6 = 0
                        count7 = 0
                        count8 = 0
                        count9 = 0
                        count10 = 0
                        count11 = 0
                        count12 = 0
                        count13 = 0
                        count14 = 0
                        count15 = 0
                        count16 = 0
                        count = []
                        for j in one_floor_dic[k]:
                            if -100 <= j < -95:
                                count1 += 1
                            if -95 <= j < -90:
                                count2 += 1
                            if -90 <= j < -85:
                                count3 += 1
                            if -85 <= j < -80:
                                count4 += 1
                            if -80 <= j < -75:
                                count5 += 1
                            if -75 <= j < -70:
                                count6 += 1
                            if -70 <= j < -65:
                                count7 += 1
                            if -65 <= j < -60:
                                count8 += 1
                            if -60 <= j < -55:
                                count9 += 1
                            if -55 <= j < -50:
                                count10 += 1
                            if -50 <= j < -45:
                                count11 += 1
                            if -45 <= j < -40:
                                count12 += 1
                            if -40 <= j < -35:
                                count13 += 1
                            if -35 <= j < -30:
                                count14 += 1
                            if -30 <= j < -25:
                                count15 += 1
                            if -25 <= j < -20:
                                count16 += 1

                        count.append(count1)
                        count.append(count2)
                        count.append(count3)
                        count.append(count4)
                        count.append(count5)
                        count.append(count6)
                        count.append(count7)
                        count.append(count8)
                        count.append(count9)
                        count.append(count10)
                        count.append(count11)
                        count.append(count12)
                        count.append(count13)
                        count.append(count14)
                        count.append(count15)
                        count.append(count16)
                        sum_count = sum(count)
                        if sum_count:
                            for q in count:
                                if q:
                                    transfer2.append(round((float(q) / float(sum(count))), 6))
                                    #
                                else:
                                    transfer2.append(float(0.000001))
                        transfer1.append(transfer2)
                    floor7_pro.append(transfer1)
                else:
                    transfer3 = []
                    transfer3.append("N")
                    transfer3.append([])
                    floor7_pro.append(transfer3)
            floor7_pro_dic = []
            for i in floor7_pro:
                floor7_pro_dic.append(dict(zip(i[0::2],i[1::2])))


            # if len(jiao) == 78:
            #     print(floor7_pro_dic)
            #
            # if len(jiao) == 1:
            #     print(floor7_pro)


            KL7 = []
            for i in range(len(jiao_7)):
                KL_sum = 0
                for j in jiao_7[i]:
                    if j:

                        KL_sum += scipy.stats.entropy(learned_floor_dic[i][j],floor7_pro_dic[i][j])
                if len(jiao_7[i]):


                    KL7.append(KL_sum)

                else:
                    KL7.append("NO")

            distance.append(KL7)

            distancefinal_7 = []
            for i in range(len(KL7)):
                if KL7[i]!="NO":
                    distancefinal_7.append(KL7[i] * similation_7[i])



                else:
                    distancefinal_7.append("NO")
            distancefinal.append(distancefinal_7)

            distancefinal_7_num = []
            for i in distancefinal_7:
                if i != "NO":
                    distancefinal_7_num.append(i)
            if distancefinal_7_num:

                floor = distancefinal_7.index(min(distancefinal_7_num)) + 1
            else:
                floor = 0

            # if len(jiao) == 233:
            #     print(floor7_pro_dic)
            # if len(jiao) == 234:
            #     print(floor7_pro_dic)
            # if len(jiao) == 235:
            #     print(floor7_pro_dic)

            print("————————————————————————————————————————認識中————————————————————————————————————————")
            print(len(floor7_pro_dic[0]))
            print(len(floor7_pro_dic[1]))
            print(len(floor7_pro_dic[2]))
            print(len(floor7_pro_dic[3]))
            print(len(floor7_pro_dic[4]))
            print(len(floor7_pro_dic[5]))
            print(len(floor7_pro_dic[6]))
            print(similation_7)
            print(jiao_7)
            print(KL7)
            print(distancefinal_7)
            print("推定した階層は"+str(floor)+"F"+"です")
            print(str(len(jiao))+"秒が経ちました")




        else:

            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~階層移動~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
            one_floor = []



    #         if boolean == True:     #用这个boolean的意义是因为階層移動有好多个 我只需要一个 否则就会多次操作
    #             baro = wifi_data_dic_list[i-1][list(wifi_data_dic_list[i-1])[0]][1]    #取得最新气压
    #             one_floor_dic = dict(zip(one_floor[0::2], one_floor[1::2]))
    #             for key in one_floor_dic:
    #                 one_floor_dic[key].pop(-1)
    #
    #             fingerprint.append(wifi_data_dic_list[i-1])              #添加fingerprint
    #
    #             if one_floor_dic:
    #                 floor_barometric.append(baro)
    #                 if len(floor_barometric) == 1:
    #                     one_floor_dic["X0"]=0
    #                 elif len(floor_barometric) >=2:
    #                     floor_barometric_difference.append(floor_barometric[-1] - floor_barometric[-2])
    #
    #                     one_floor_dic[("X0"+"+"+"("+str(round(float(sum(floor_barometric_difference)),4))+")")]=round(float(sum(floor_barometric_difference)),4)
    #                 wifi_floor_list.append(one_floor_dic)
    #         one_floor_dic = {}
    #         print("————————————————————————————————————————階層移動————————————————————————————————————————")
    #         one_floor = []
    #         boolean = False
    # if one_floor:
    #     floor_barometric.append(one_floor[len(one_floor)-1][len(one_floor[len(one_floor)-1])-1])
    #     floor_barometric_difference.append(floor_barometric[-1] - floor_barometric[-2])
    #     one_floor_dic = dict(zip(one_floor[0::2], one_floor[1::2]))
    #     for key in one_floor_dic:
    #         one_floor_dic[key].pop(-1)
    #     one_floor_dic[("X0"+"+"+"("+str(round(float(sum(floor_barometric_difference)),4))+")")]=round(float(sum(floor_barometric_difference)),4)
    #     wifi_floor_list.append(one_floor_dic)


    return wifi_floor_list


    # for i in deleted_upordown_number2:
    #     if i != "階層移動":
    #         for key in wifi_data_dic_list[i]:
    #             if wifi_data_dic_list[i][key][0] >= -45:
    #                 key1.append(key)
    #                 key1.append(wifi_data_dic_list[i][key][1])     #如果用聚类的方法找到相对应的超过45的wifi时候需要
    # over45_wifi_baro = dict(zip(key1[0::2], key1[1::2]))
    # return over45_wifi_baro  # 把rssi大于-45的wifi选出来给他们加上气压的标签
#

getmaxbarometric()

# def gps():
#     A = []
#     B = []
#     num = 0
#     a = json2List(filepath)
#     for i in a:
#
#         if "accuracy" in i:
#
#             if i["accuracy"] < 15:
#                 A.append(num)
#                 break
#             else:
#                 A = []
#         else:num = num+1
#     for i in A:
#         B.append(a[i+1]["hpa"])
#
#     c = np.median(B)
#     print(c)
#
# test  = gps()
