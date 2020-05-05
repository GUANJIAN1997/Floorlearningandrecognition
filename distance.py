from data_process import json2List
import numpy as np

filepath1 = "/Users/jianguan/Desktop/毕业/预实验/finger1.json"
filepath2 = "/Users/jianguan/Desktop/毕业/预实验/finger2.json"
def distance():
    rowdata1 = json2List(filepath1)

    wifi_data1 = []
    wifi_data2 = []
    wifi_data_dic_list1 = []
    wifi_data_dic_list2 = []

    for i in rowdata1:
        if "nodeId" in i:
            transfer_list = []
            for j in i["scanResults"]:

                if j["essid"] == "Rits-Webauth" or j["essid"] == "eduroam":
                    transfer_list.append(j["bssid"])
                    transfer_list.append(j["rssi"])

            wifi_data1.append(transfer_list)

    for i in wifi_data1:
        wifi_data_dic = dict(zip(i[::2], i[1::2]))
        wifi_data_dic_list1.append(wifi_data_dic)


    rowdata2 = json2List(filepath2)



    for i in rowdata2:
        if "nodeId" in i:
            transfer_list = []
            for j in i["scanResults"]:

                if j["essid"] == "Rits-Webauth" or j["essid"] == "eduroam":
                    transfer_list.append(j["bssid"])
                    transfer_list.append(j["rssi"])

            wifi_data2.append(transfer_list)

    for i in wifi_data2:
        wifi_data_dic = dict(zip(i[0::2], i[1::2]))
        wifi_data_dic_list2.append(wifi_data_dic)

    # sorted(wifi_data_dic_list1[-1].items(),key=lambda item:item[1])
    #
    # sorted(wifi_data_dic_list2[-1].items(), key=lambda item: item[1])

    rssi1 = []
    rssi2 = []

    for key in wifi_data_dic_list2[0]:
        if key in wifi_data_dic_list1[0]:
            rssi1.append(wifi_data_dic_list1[0][key])
            rssi2.append(wifi_data_dic_list2[0][key])


    rssi1 = np.array(rssi1)
    rssi2 = np.array(rssi2)

    dist = np.linalg.norm(rssi1 - rssi2)
    wifi = len(set(list(wifi_data_dic_list1[0].keys())) | set(list(wifi_data_dic_list2[0].keys()))) / len(set(list(wifi_data_dic_list1[0].keys())) & set(list(wifi_data_dic_list2[0].keys())))
    dist = dist * wifi
    return dist


print(distance())


