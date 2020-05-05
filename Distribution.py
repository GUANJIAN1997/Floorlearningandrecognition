
from data_process import json2List
import matplotlib.pyplot as plt
import numpy as np

filepath1 = "/Users/jianguan/Desktop/毕业/预实验/1.json"
filepath2 = "/Users/jianguan/Desktop/毕业/预实验/2.json"
filepath3 = "/Users/jianguan/Desktop/毕业/预实验/3.json"
filepath4 = "/Users/jianguan/Desktop/毕业/预实验/4.json"
filepath5 = "/Users/jianguan/Desktop/毕业/预实验/5.json"
filepath6 = "/Users/jianguan/Desktop/毕业/预实验/6.json"
filepath7 = "/Users/jianguan/Desktop/毕业/预实验/7.json"




def find_ritsumei():
    rowdata1 = []
    rowdata2 = []
    rowdata3 = []
    rowdata4 = []
    rowdata5 = []
    rowdata6 = []
    rowdata7 = []
    rowdata_All = []

    rowdata1 = json2List(filepath1)
    rowdata2 = json2List(filepath2)
    rowdata3 = json2List(filepath3)
    rowdata4 = json2List(filepath4)
    rowdata5 = json2List(filepath5)
    rowdata6 = json2List(filepath6)
    rowdata7 = json2List(filepath7)



    if rowdata1:
        rowdata_All.append(rowdata1)
    if rowdata2:
        rowdata_All.append(rowdata2)
    if rowdata3:
        rowdata_All.append(rowdata3)
    if rowdata4:
        rowdata_All.append(rowdata4)
    if rowdata5:
        rowdata_All.append(rowdata5)
    if rowdata6:
        rowdata_All.append(rowdata6)
    if rowdata7:
        rowdata_All.append(rowdata7)

    wifi_data = []
    wifi_data_dic_list = []

    for rowdata in rowdata_All:
        wifi_data_transfer = []
        for i in rowdata:
            if "nodeId" in i:
                transfer_list = []
                for j in i["scanResults"]:
                    if j["essid"] == "Rits-Webauth" or j["essid"] == "eduroam":
                        transfer_list.append(j["bssid"])
                        transfer_list.append(j["rssi"])
                wifi_data_transfer.append(transfer_list)
        wifi_data.append(wifi_data_transfer)
    for wifi_data_i in wifi_data:
        wifi_data_dic_list_transfer = []
        for i in wifi_data_i:
            wifi_data_dic = dict(zip(i[::2], i[1::2]))
            wifi_data_dic_list_transfer.append(wifi_data_dic)
        wifi_data_dic_list.append(wifi_data_dic_list_transfer)
    return wifi_data_dic_list             #7层的bssid和rssi的字典数据
print(len(find_ritsumei()))

def wifibssid():


    wifi_bssid1 = []
    wifi_bssid2 = []
    wifi_bssid3 = []
    wifi_bssid4 = []
    wifi_bssid5 = []
    wifi_bssid6 = []
    wifi_bssid7 = []

    wifi_data_dic_list = find_ritsumei()
    for wifi_data_number in range(len(wifi_data_dic_list)):
        if wifi_data_number == 0:
            for wifi_data_i in wifi_data_dic_list[wifi_data_number]:
                for key in wifi_data_i:
                    if key not in wifi_bssid1:
                        wifi_bssid1.append(key)
        if wifi_data_number == 1:
            for wifi_data_i in wifi_data_dic_list[wifi_data_number]:
                for key in wifi_data_i:
                    if key not in wifi_bssid2:
                        wifi_bssid2.append(key)
        if wifi_data_number == 2:
            for wifi_data_i in wifi_data_dic_list[wifi_data_number]:
                for key in wifi_data_i:
                    if key not in wifi_bssid3:
                        wifi_bssid3.append(key)
        if wifi_data_number == 3:
            for wifi_data_i in wifi_data_dic_list[wifi_data_number]:
                for key in wifi_data_i:
                    if key not in wifi_bssid4:
                        wifi_bssid4.append(key)
        if wifi_data_number == 4:
            for wifi_data_i in wifi_data_dic_list[wifi_data_number]:
                for key in wifi_data_i:
                    if key not in wifi_bssid5:
                        wifi_bssid5.append(key)
        if wifi_data_number == 5:
            for wifi_data_i in wifi_data_dic_list[wifi_data_number]:
                for key in wifi_data_i:
                    if key not in wifi_bssid6:
                        wifi_bssid6.append(key)
        if wifi_data_number == 6:
            for wifi_data_i in wifi_data_dic_list[wifi_data_number]:
                for key in wifi_data_i:
                    if key not in wifi_bssid7:
                        wifi_bssid7.append(key)
    return wifi_bssid1,wifi_bssid2,wifi_bssid3         #每层检测出来的bssid总数

def find_rssi():

    fig = plt.figure()
    ax = plt.subplot()
    wifi_data = find_ritsumei()
    wifi_bssid = wifibssid()
    bssid_rssi1 = []
    bssid_rssi2 = []
    bssid_rssi3 = []
    bssid_rssi4 = []
    bssid_rssi5 = []
    bssid_rssi6 = []
    bssid_rssi7 = []
    for bssid in wifi_bssid[0]:
        rssi_floor_multi_bssid1 = []
        for floor_numbuer in range(len(wifi_data)):
            rssi_floor_one_bssid1 = []
            for dic in wifi_data[floor_numbuer]:
                if bssid in dic:
                    rssi_floor_one_bssid1.append(dic[bssid])
            rssi_floor_multi_bssid1.append(rssi_floor_one_bssid1)
        bssid_rssi1.append(rssi_floor_multi_bssid1)       #bssid_rssi这个列表里有36个列表（一层里检测出来的bssid的数量）然后36个列表里有7个列表存着每层的rssi

    for bssid in wifi_bssid[1]:
        rssi_floor_multi_bssid2 = []
        for floor_numbuer in range(len(wifi_data)):
            rssi_floor_one_bssid2 = []
            for dic in wifi_data[floor_numbuer]:
                if bssid in dic:
                    rssi_floor_one_bssid2.append(dic[bssid])
            rssi_floor_multi_bssid2.append(rssi_floor_one_bssid2)
        bssid_rssi2.append(rssi_floor_multi_bssid2)

    for bssid in wifi_bssid[2]:
        rssi_floor_multi_bssid3 = []
        for floor_numbuer in range(len(wifi_data)):
            rssi_floor_one_bssid3 = []
            for dic in wifi_data[floor_numbuer]:
                if bssid in dic:
                    rssi_floor_one_bssid3.append(dic[bssid])
            rssi_floor_multi_bssid3.append(rssi_floor_one_bssid3)
        bssid_rssi3.append(rssi_floor_multi_bssid3)

    for bssid in wifi_bssid[3]:
        rssi_floor_multi_bssid4 = []
        for floor_numbuer in range(len(wifi_data)):
            rssi_floor_one_bssid4 = []
            for dic in wifi_data[floor_numbuer]:
                if bssid in dic:
                    rssi_floor_one_bssid4.append(dic[bssid])
            rssi_floor_multi_bssid4.append(rssi_floor_one_bssid4)
        bssid_rssi4.append(rssi_floor_multi_bssid4)

    for bssid in wifi_bssid[4]:
        rssi_floor_multi_bssid5 = []
        for floor_numbuer in range(len(wifi_data)):
            rssi_floor_one_bssid5 = []
            for dic in wifi_data[floor_numbuer]:
                if bssid in dic:
                    rssi_floor_one_bssid5.append(dic[bssid])
            rssi_floor_multi_bssid5.append(rssi_floor_one_bssid5)
        bssid_rssi5.append(rssi_floor_multi_bssid5)

    for bssid in wifi_bssid[5]:
        rssi_floor_multi_bssid6 = []
        for floor_numbuer in range(len(wifi_data)):
            rssi_floor_one_bssid6 = []
            for dic in wifi_data[floor_numbuer]:
                if bssid in dic:
                    rssi_floor_one_bssid6.append(dic[bssid])
            rssi_floor_multi_bssid6.append(rssi_floor_one_bssid6)
        bssid_rssi6.append(rssi_floor_multi_bssid6)

    for bssid in wifi_bssid[6]:
        rssi_floor_multi_bssid7 = []
        for floor_numbuer in range(len(wifi_data)):
            rssi_floor_one_bssid7 = []
            for dic in wifi_data[floor_numbuer]:
                if bssid in dic:
                    rssi_floor_one_bssid7.append(dic[bssid])
            rssi_floor_multi_bssid7.append(rssi_floor_one_bssid7)
        bssid_rssi7.append(rssi_floor_multi_bssid7)

    return bssid_rssi1,bssid_rssi2,bssid_rssi3,bssid_rssi4,bssid_rssi5,bssid_rssi6,bssid_rssi7

