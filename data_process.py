import json
import numpy as np
filepath = "/Users/jianguan/Desktop/毕业/楼层判定实验数据/test1234567.json"

# class dataprocess:
#     '处理数据的类，将手机的气压数据，wifi数据，gps数据整理好，并具备识别出楼层移动并且记录，删除移动数据的功能'
#     rowdata = []
#     f =


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
                if j["essid"] == "eduroam":
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

    wifi_data_dic_list = get_wifi_bro()



    # deleted_upordown_number = set(list(range(len(get_barometric())-1)))-set(upordown(get_barometric())[1]) #删除上下楼的数据的标号之后的标号
    upordown_number = upordown(get_barometric())[1]
    deleted_upordown_number2  = list(range(len(get_barometric()) - 1))
    # print(upordown_number)
    for i in upordown_number:
        deleted_upordown_number2[i] = "階層移動"     #把上下楼的标号标注階層移動*******代替deleted_upordown_number

    # print(deleted_upordown_number2)
    # print(deleted_upordown_number2.index("階層移動"))

    wifi_floor_list = []
    floor_barometric = []
    floor_barometric_difference = []
    boolean = True
    one_floor = []
    one_floor_dic = {}
    fingerprint = []

    # print(wifi_data_dic_list)
    for i in range(len(deleted_upordown_number2)):              #1.5一个，编号，0到总个数，其中上下楼的编号已经被标注成"階層移動"
        if deleted_upordown_number2[i] != "階層移動":
            for key in wifi_data_dic_list[i]:
                if key not in one_floor:
                    one_floor.append(key)
                    one_floor.append(wifi_data_dic_list[i][key])      #添加bssid和对应的rssi和气压（新的bssid）

                elif wifi_data_dic_list[i][key][0] not in one_floor[one_floor.index(key)+1]:      #添加不同的rssi值
                    one_floor[one_floor.index(key)+1].insert(len(one_floor[one_floor.index(key)+1])-1,wifi_data_dic_list[i][key][0])

            # print("————————————————————————————————————————学習中 ————————————————————————————————————————")
            # print(one_floor)
            boolean = True

        else:
            if boolean == True:     #用这个boolean的意义是因为階層移動有好多个 我只需要一个 否则就会多次操作
                baro = wifi_data_dic_list[i-1][list(wifi_data_dic_list[i-1])[0]][1]
                one_floor_dic = dict(zip(one_floor[0::2], one_floor[1::2]))
                for key in one_floor_dic:
                    one_floor_dic[key].pop(-1)

                fingerprint.append(wifi_data_dic_list[i-1])              #添加fingerprint

                if one_floor_dic:
                    floor_barometric.append(baro)
                    if len(floor_barometric) == 1:
                        one_floor_dic["X0"]=0
                    elif len(floor_barometric) >=2:
                        floor_barometric_difference.append(floor_barometric[-1] - floor_barometric[-2])

                        one_floor_dic[("X0"+"+"+"("+str(round(float(sum(floor_barometric_difference)),4))+")")]=round(float(sum(floor_barometric_difference)),4)
                    wifi_floor_list.append(one_floor_dic)
            one_floor_dic = {}
            # print("————————————————————————————————————————階層移動————————————————————————————————————————")
            one_floor = []
            boolean = False
    if one_floor:
        floor_barometric.append(one_floor[len(one_floor)-1][len(one_floor[len(one_floor)-1])-1])
        floor_barometric_difference.append(floor_barometric[-1] - floor_barometric[-2])
        one_floor_dic = dict(zip(one_floor[0::2], one_floor[1::2]))
        for key in one_floor_dic:
            one_floor_dic[key].pop(-1)
        one_floor_dic[("X0"+"+"+"("+str(round(float(sum(floor_barometric_difference)),4))+")")]=round(float(sum(floor_barometric_difference)),4)
        wifi_floor_list.append(one_floor_dic)


    return wifi_floor_list

# print(len(getmaxbarometric()[0]))
    # for i in deleted_upordown_number2:
    #     if i != "階層移動":
    #         for key in wifi_data_dic_list[i]:
    #             if wifi_data_dic_list[i][key][0] >= -45:
    #                 key1.append(key)
    #                 key1.append(wifi_data_dic_list[i][key][1])     #如果用聚类的方法找到相对应的超过45的wifi时候需要
    # over45_wifi_baro = dict(zip(key1[0::2], key1[1::2]))
    # return over45_wifi_baro  # 把rssi大于-45的wifi选出来给他们加上气压的标签
#

print(len(getmaxbarometric()[0]))
print(len(getmaxbarometric()[1]))
print(len(getmaxbarometric()[2]))
print(len(getmaxbarometric()[3]))
print(len(getmaxbarometric()[4]))
print(len(getmaxbarometric()[5]))
print(len(getmaxbarometric()[6]))

print(getmaxbarometric())

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
