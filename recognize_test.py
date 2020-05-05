from __future__ import division
from make_rssi_floor import find_ritsumei
import numpy as np
import matplotlib.pyplot as plt
from data_process import json2List

def find_floor():


    floor1 = {}
    floor2 = {}
    floor3 = {}
    floor4 = {}
    floor5 = {}
    floor6 = {}
    floor7 = {}



    wifi_data_dic_list = find_ritsumei()
    for i in wifi_data_dic_list[0]:
        for key in i:
            if key not in floor1:
                if i[key] > -100:
                    floor1[key]=[]
                    floor1[key].append(i[key])
            elif i[key] > -100:
                floor1[key].append(i[key])


    for i in wifi_data_dic_list[1]:
        for key in i:
            if key not in floor2:
                if i[key] > -100:
                    floor2[key]=[]
                    floor2[key].append(i[key])
            elif i[key] > -100:
                floor2[key].append(i[key])

    for i in wifi_data_dic_list[2]:
        for key in i:
            if key not in floor3:
                if i[key] > -100:
                    floor3[key]=[]
                    floor3[key].append(i[key])
            elif i[key] > -100:
                floor3[key].append(i[key])

    for i in wifi_data_dic_list[3]:
        for key in i:
            if key not in floor4:
                if i[key] > -100:
                    floor4[key]=[]
                    floor4[key].append(i[key])
            elif i[key] > -100:
                floor4[key].append(i[key])

    for i in wifi_data_dic_list[4]:
        for key in i:
            if key not in floor5:
                if i[key] > -100:
                    floor5[key]=[]
                    floor5[key].append(i[key])
            elif i[key] > -100:
                floor5[key].append(i[key])

    for i in wifi_data_dic_list[5]:
        for key in i:
            if key not in floor6:
                if i[key] > -100:
                    floor6[key]=[]
                    floor6[key].append(i[key])
            elif i[key] > -100:
                floor6[key].append(i[key])

    for i in wifi_data_dic_list[6]:
        for key in i:
            if key not in floor7:
                if i[key] > -100:
                    floor7[key]=[]
                    floor7[key].append(i[key])
            elif i[key] > -100:
                floor7[key].append(i[key])
    learned_floor=[]
    learned_floor.append(floor1)
    learned_floor.append(floor2)
    learned_floor.append(floor3)
    learned_floor.append(floor4)
    learned_floor.append(floor5)
    learned_floor.append(floor6)
    learned_floor.append(floor7)
    learned_floor_Probability = []
    # print(np.mean(learned_floor[0]["a0:cf:5b:a3:5d:30"]))
    # print(np.mean(learned_floor[0]["a0:cf:5b:a2:ce:70"]))
    # print(np.mean(learned_floor[0]["a0:cf:5b:a3:4f:f0"]))
    # print(np.std(learned_floor[0]["a0:cf:5b:a3:5d:30"], ddof=1))
    # print(np.std(learned_floor[0]["a0:cf:5b:a2:ce:70"], ddof=1))
    # print(np.std(learned_floor[0]["a0:cf:5b:a3:4f:f0"], ddof=1))
    for i in learned_floor:     #有七层的数据
        transfer1 = []
        for key in i:
            transfer2 = []
            transfer1.append(key)
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
            for j in i[key]:
                if -100<=j<-95:
                    count1+=1
                if -95<=j<-90:
                    count2+=1
                if -90<=j<-85:
                    count3+=1
                if -85<=j<-80:
                    count4+=1
                if -80<=j<-85:
                    count5+=1
                if -85<=j<-70:
                    count6+=1
                if -70<=j<-65:
                    count7+=1
                if -65<=j<-60:
                    count8+=1
                if -60<=j<-55:
                    count9+=1
                if -55<=j<-50:
                    count10+=1
                if -50<=j<-45:
                    count11+=1
                if -45<=j<-40:
                    count12+=1
                if -40<=j<-35:
                    count13+=1
                if -35<=j<-30:
                    count14+=1
                if -30<=j<-25:
                    count15+=1
                if -25<=j<-20:
                    count16+=1
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
                for k in count:
                    if k:
                        transfer2.append(round(float(k) / float(sum(count)),6))
                    else:
                        transfer2.append(float(0.000001))
            transfer1.append(transfer2)
        learned_floor_Probability.append(transfer1)









    # filepath = "/Users/jianguan/Desktop/毕业/test_5F.json"
    #
    # wifi_data_dic_list_test = []
    #
    # rowdata = json2List(filepath)
    # rowdata_All = []
    # rowdata_All.append(rowdata)
    # wifi_data = []
    # for rowdata in rowdata_All:
    #     wifi_data_transfer = []
    #     for i in rowdata:
    #         if "nodeId" in i:
    #             transfer_list = []
    #             for j in i["scanResults"]:
    #                 if j["essid"] == "Rits-Webauth" or j["essid"] == "eduroam":
    #                     transfer_list.append(j["bssid"])
    #                     transfer_list.append(j["rssi"])
    #             wifi_data_transfer.append(transfer_list)
    #     wifi_data.append(wifi_data_transfer)
    # for wifi_data_i in wifi_data:
    #     wifi_data_dic_list_transfer = []
    #     for i in wifi_data_i:
    #         wifi_data_dic = dict(zip(i[::2], i[1::2]))
    #         wifi_data_dic_list_transfer.append(wifi_data_dic)
    #     wifi_data_dic_list_test.append(wifi_data_dic_list_transfer)
    #
    # floor1_num = 0
    # floor2_num = 0
    # floor3_num = 0
    # floor4_num = 0
    # floor5_num = 0
    # floor6_num = 0
    # floor7_num = 0
    #

    # for key in wifi_data_dic_list_test[0][5]:
    #     if key in floor1:
    #         if min(floor1[key]) <= wifi_data_dic_list_test[0][5][key] <= max(floor1[key]):
    #             floor1_num = floor1_num + 1
    #
    #     if key in floor2:
    #         if min(floor2[key]) <= wifi_data_dic_list_test[0][5][key] <= max(floor2[key]):
    #             floor2_num = floor2_num + 1
    #     if key in floor3:
    #         if min(floor3[key]) <= wifi_data_dic_list_test[0][5][key] <= max(floor3[key]):
    #             floor1_num = floor3_num + 1
    #     if key in floor4:
    #         if min(floor4[key]) <= wifi_data_dic_list_test[0][5][key] <= max(floor4[key]):
    #             floor4_num = floor4_num + 1
    #     if key in floor5:
    #         if min(floor5[key]) <= wifi_data_dic_list_test[0][5][key] <= max(floor5[key]):
    #             floor5_num = floor5_num + 1
    #     if key in floor6:
    #         if min(floor6[key]) <= wifi_data_dic_list_test[0][5][key] <= max(floor6[key]):
    #             floor6_num = floor6_num + 1
    #     if key in floor1:
    #         if min(floor7[key]) <= wifi_data_dic_list_test[0][5][key] <= max(floor7[key]):
    #             floor7_num = floor7_num + 1
    #
    #     sum = floor1_num+floor2_num+floor3_num+floor4_num+floor5_num+floor6_num+floor7_num

    # for key in wifi_data_dic_list_test[0][5]:
    #     if key in floor1:
    #
    #         floor1_num = floor1_num + 1
    #
    #     if key in floor2:
    #
    #         floor2_num = floor2_num + 1
    #     if key in floor3:
    #
    #         floor1_num = floor3_num + 1
    #     if key in floor4:
    #
    #         floor4_num = floor4_num + 1
    #     if key in floor5:
    #
    #         floor5_num = floor5_num + 1
    #     if key in floor6:
    #
    #         floor6_num = floor6_num + 1
    #     if key in floor1:
    #
    #         floor7_num = floor7_num + 1


        # if sum != 0:
        #     percent_1 = format(float(floor1_num) / float(sum), ".2f")
        #
        #     percent_2 = format(float(floor2_num) / float(sum), ".2f")
        #     percent_3 = format(float(floor3_num) / float(sum), ".2f")
        #     percent_4 = format(float(floor4_num) / float(sum), ".2f")
        #     percent_5 = format(float(floor5_num) / float(sum), ".2f")
        #     percent_6 = format(float(floor6_num) / float(sum), ".2f")
        #     percent_7 = format(float(floor7_num) / float(sum), ".2f")
    # print(len(floor1))
    # print(len(floor2))
    # print(len(floor3))
    # print(len(floor4))
    # print(len(floor5))
    # print(len(floor6))
    # print(len(floor7))
    #
    # return floor1_num,floor2_num,floor3_num,floor4_num,floor5_num,floor6_num,floor7_num
    # return percent_1,percent_2,percent_3,percent_4,percent_5,percent_6,percent_7
    # return wifi_data_dic_list_test

    # return learned_floor,learned_floor_Probability
    return learned_floor_Probability

print(len(find_floor()[0]))
print(len(find_floor()[1]))
print(len(find_floor()[2]))
print(len(find_floor()[3]))
print(len(find_floor()[4]))
print(len(find_floor()[5]))
print(len(find_floor()[6]))


# print(find_floor()[0][4])
# print(find_floor()[0][5])
# print(find_floor()[0].index("a0:cf:5b:9f:36:11"))
# print(find_floor()[1].index("a0:cf:5b:9f:36:11"))
# print(find_floor()[2].index("a0:cf:5b:9f:36:11"))
# print(find_floor()[3].index("a0:cf:5b:9f:36:11"))
# print(find_floor()[4].index("a0:cf:5b:9f:36:11"))
# print(find_floor()[5].index("a0:cf:5b:9f:36:11"))
# # print(find_floor()[6].index("a0:cf:5b:9f:36:11"))
#
#
#
# plt.figure(figsize=(20,10))
# num_list = find_floor()[0][37]
# plt.bar(["[-100,-95)","[-95,-90)","[-90,-85)","[-85,-80)","[-80,-85)","[-85,-70)","[-70,-65)","[-65,-60)","[-60,-55)","[-55,-50)","[-50,-45)","[-45,-40)","[-40,-35)","[-35,-30)","[-30,-25)","[-25,-20)"], num_list)
# plt.show()
# #
# plt.figure(figsize=(20,10))
# num_list = find_floor()[1][23]
# plt.bar(["[-100,-95)","[-95,-90)","[-90,-85)","[-85,-80)","[-80,-85)","[-85,-70)","[-70,-65)","[-65,-60)","[-60,-55)","[-55,-50)","[-50,-45)","[-45,-40)","[-40,-35)","[-35,-30)","[-30,-25)","[-25,-20)"], num_list)
# plt.show()
# #
# plt.figure(figsize=(20,10))
# num_list = find_floor()[2][41]
# plt.bar(["[-100,-95)","[-95,-90)","[-90,-85)","[-85,-80)","[-80,-85)","[-85,-70)","[-70,-65)","[-65,-60)","[-60,-55)","[-55,-50)","[-50,-45)","[-45,-40)","[-40,-35)","[-35,-30)","[-30,-25)","[-25,-20)"], num_list)
# plt.show()
# # for i in range(10):
# #     plt.figure(figsize=(20,10))
# #     num_list = find_floor()[0][1::2][i]
# #     plt.bar(["[-100,-95)","[-95,-90)","[-90,-85)","[-85,-80)","[-80,-85)","[-85,-70)","[-70,-65)","[-65,-60)","[-60,-55)","[-55,-50)","[-50,-45)","[-45,-40)","[-40,-35)","[-35,-30)","[-30,-25)","[-25,-20)"], num_list)
# #     plt.show()
# # plt.close("all")
# plt.figure(figsize=(20,10))
# num_list = find_floor()[3][39]
# plt.bar(["[-100,-95)","[-95,-90)","[-90,-85)","[-85,-80)","[-80,-85)","[-85,-70)","[-70,-65)","[-65,-60)","[-60,-55)","[-55,-50)","[-50,-45)","[-45,-40)","[-40,-35)","[-35,-30)","[-30,-25)","[-25,-20)"], num_list)
# plt.show()
#
# plt.figure(figsize=(20,10))
# num_list = find_floor()[4][43]
# plt.bar(["[-100,-95)","[-95,-90)","[-90,-85)","[-85,-80)","[-80,-85)","[-85,-70)","[-70,-65)","[-65,-60)","[-60,-55)","[-55,-50)","[-50,-45)","[-45,-40)","[-40,-35)","[-35,-30)","[-30,-25)","[-25,-20)"], num_list)
# plt.show()
#
# plt.figure(figsize=(20,10))
# num_list = find_floor()[5][15]
# plt.bar(["[-100,-95)","[-95,-90)","[-90,-85)","[-85,-80)","[-80,-85)","[-85,-70)","[-70,-65)","[-65,-60)","[-60,-55)","[-55,-50)","[-50,-45)","[-45,-40)","[-40,-35)","[-35,-30)","[-30,-25)","[-25,-20)"], num_list)
# plt.show()
