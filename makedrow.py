from data_process import json2List
import matplotlib.pyplot as plt
import numpy as np


filepath = "/Users/jianguan/Desktop/毕业/预实验/1F进门.json"


def find_ritsumei():
    rowdata = json2List(filepath)
    wifi_data = []
    wifi_data_dic_list = []

    for i in rowdata:
        if "nodeId" in i:
            transfer_list = []
            for j in i["scanResults"]:

                if j["essid"] == "Rits-Webauth" or j["essid"] == "eduroam":
                    transfer_list.append(j["bssid"])
                    transfer_list.append(j["rssi"])

            wifi_data.append(transfer_list)

    for i in wifi_data:
        wifi_data_dic = dict(zip(i[::2], i[1::2]))
        wifi_data_dic_list.append(wifi_data_dic)
    return wifi_data_dic_list
# print(find_ritsumei())


def draw_picture():

    y1_bssid = []
    y2_bssid = []
    y3_bssid = []
    y4_bssid = []
    y5_bssid = []
    y6_bssid = []
    y7_bssid = []
    wifi_data_dic_list = find_ritsumei()
    for wifi_data in wifi_data_dic_list:
        for key in wifi_data:
            if (key == "a0:cf:5b:9f:bb:f0" or key =="a0:cf:5b:9f:bb:f1" or key =="a0:cf:5b:9f:bb:fe" or key =="a0:cf:5b:9f:bb:ff" or
                    key =="a0:cf:5b:9f:af:00" or key == "a0:cf:5b:9f:af:0f" or key =="a0:cf:5b:9f:af:0e" or key =="a0:cf:5b:9f:af:01" or
                    key =="a0:cf:5b:9f:b0:91" or key =="a0:cf:5b:9f:b0:90" or key =="a0:cf:5b:9f:b0:9e" or key =="a0:cf:5b:9f:b0:9f" or
                    key =="f0:29:29:60:3a:10" or key =="f0:29:29:60:3a:11" or key =="f0:29:29:60:3a:1f" or key =="f0:29:29:60:3a:1e" or
                    key =="a0:cf:5b:c2:2d:81" or key =="a0:cf:5b:c2:2d:80" or key =="a0:cf:5b:c2:2d:8e" or key =="a0:cf:5b:c2:2d:8f"
                    ):
                if key not in y1_bssid:
                    y1_bssid.append(key)

            elif (
                    key == "a0:cf:5b:9f:dd:00" or key == "a0:cf:5b:9f:dd:01" or key == "a0:cf:5b:9f:dd:0e" or key == "a0:cf:5b:9f:dd:0f" or
                    key == "a0:cf:5b:a3:7e:d1" or key == "a0:cf:5b:a3:7e:d0" or key == "a0:cf:5b:a3:7e:de" or key == "a0:cf:5b:a3:7e:df" or
                    key == "a0:cf:5b:a3:7e:50" or key == "a0:cf:5b:a3:7e:51" or key == "a0:cf:5b:a3:7e:5e" or key == "a0:cf:5b:a3:7e:5f" or
                    key == "a0:cf:5b:9f:d4:60" or key == "a0:cf:5b:9f:d4:61" or key == "a0:cf:5b:9f:d4:6e" or key == "a0:cf:5b:9f:d4:6f" or
                    key == "a0:cf:5b:9f:cd:20" or key == "a0:cf:5b:9f:cd:21" or key == "a0:cf:5b:9f:cd:2e" or key == "a0:cf:5b:9f:cd:2f"):
                if key not in y2_bssid:
                    y2_bssid.append(key)
            elif (
                    key == "a0:cf:5b:a3:a3:60" or key == "a0:cf:5b:a3:a3:61" or key == "a0:cf:5b:a3:a3:6e" or key == "a0:cf:5b:a3:a3:6f" or
                    key == "a0:cf:5b:c2:00:e0" or key == "a0:cf:5b:c2:00:e1" or key == "a0:cf:5b:c2:00:ee" or key == "a0:cf:5b:c2:00:ef" or
                    key == "a0:cf:5b:a3:4f:50" or key == "a0:cf:5b:a3:4f:51" or key == "a0:cf:5b:a3:4f:5e" or key == "a0:cf:5b:a3:4f:5f" or
                    key == "a0:cf:5b:9f:36:1e" or key == "a0:cf:5b:9f:36:1f" or key == "a0:cf:5b:9f:36:10" or key == "a0:cf:5b:9f:36:11" or
                    key == "a0:cf:5b:a3:4b:70" or key == "a0:cf:5b:a3:4b:71" or key == "a0:cf:5b:a3:4b:7e" or key == "a0:cf:5b:a3:4b:7f"):
                if key not in y3_bssid:
                    y3_bssid.append(key)

            elif(key == "a0:cf:5b:9f:cc:e0" or key =="a0:cf:5b:9f:cc:e1" or key =="a0:cf:5b:9f:cc:ee" or key =="a0:cf:5b:9f:cc:ef" or
                    key =="a0:cf:5b:a3:21:f1" or key == "a0:cf:5b:a3:21:f0" or key =="a0:cf:5b:a3:21:fe" or key =="a0:cf:5b:a3:21:ff" or
                    key =="a0:cf:5b:9f:cc:f0" or key =="a0:cf:5b:9f:cc:f1" or key =="a0:cf:5b:9f:cc:fe" or key =="a0:cf:5b:9f:cc:ff" or
                    key =="a0:cf:5b:9f:c6:c0" or key =="a0:cf:5b:9f:c6:c1" or key =="a0:cf:5b:9f:c6:ce" or key =="a0:cf:5b:9f:c6:cf" or
                    key =="a0:cf:5b:a3:8b:91" or key =="a0:cf:5b:a3:8b:90" or key =="a0:cf:5b:a3:8b:9e" or key =="a0:cf:5b:a3:8b:9f"
                    ):
                if key not in y4_bssid:
                    y4_bssid.append(key)

            elif (
                    key == "a0:cf:5b:a3:5d:30" or key == "a0:cf:5b:a3:5d:31" or key == "a0:cf:5b:a3:5d:3e" or key == "a0:cf:5b:a3:5d:3f" or
                    key == "a0:cf:5b:a2:ce:7e" or key == "a0:cf:5b:a2:ce:70" or key == "a0:cf:5b:a2:ce:71" or key == "a0:cf:5b:a2:ce:7f" or
                    key == "a0:cf:5b:a3:4f:f0" or key == "a0:cf:5b:a3:4f:f1" or key == "a0:cf:5b:a3:4f:fe" or key == "a0:cf:5b:a3:4f:ff" or
                    key == "a0:cf:5b:9f:e7:a1" or key == "a0:cf:5b:9f:e7:a0" or key == "a0:cf:5b:9f:e7:ae" or key == "a0:cf:5b:9f:e7:af" or
                    key == "a0:cf:5b:9f:36:80" or key == "a0:cf:5b:9f:36:81" or key == "a0:cf:5b:9f:36:8e" or key == "a0:cf:5b:9f:36:8f"):
                if key not in y5_bssid:
                    y5_bssid.append(key)

            elif (
                    key == "a0:cf:5b:9f:d1:a0" or key == "a0:cf:5b:9f:d1:a1" or key == "a0:cf:5b:9f:d1:ae" or key == "a0:cf:5b:9f:d1:af" or

                    key == "a0:cf:5b:a3:52:c1" or key == "a0:cf:5b:a3:52:c0" or key == "a0:cf:5b:a3:52:ce" or key == "a0:cf:5b:a3:52:cf" or

                    key == "a0:cf:5b:9f:d3:70" or key == "a0:cf:5b:9f:d3:71" or key == "a0:cf:5b:9f:d3:7e" or key == "a0:cf:5b:9f:d3:7f" or

                    key == "a0:cf:5b:a3:5e:20" or key == "a0:cf:5b:a3:5e:21" or key == "a0:cf:5b:a3:5e:2e" or key == "a0:cf:5b:a3:5e:2f" or

                    key == "a0:cf:5b:9f:c6:f0" or key == "a0:cf:5b:9f:c6:f1" or key == "a0:cf:5b:9f:c6:fe" or key == "a0:cf:5b:9f:c6:ff"):

                if key not in y6_bssid:
                    y6_bssid.append(key)

            elif (
                    key == "a0:cf:5b:c2:0e:21" or key == "a0:cf:5b:c2:0e:20" or key == "a0:cf:5b:c2:0e:2e" or key == "a0:cf:5b:c2:0e:2f" or

                    key == "a0:cf:5b:a3:79:50" or key == "a0:cf:5b:a3:79:51" or key == "a0:cf:5b:a3:79:5e" or key == "a0:cf:5b:a3:79:5f" or

                    key == "a0:cf:5b:c2:0b:91" or key == "a0:cf:5b:c2:0b:90" or key == "a0:cf:5b:c2:0b:9e" or key == "a0:cf:5b:c2:0b:9f" or

                    key == "a0:cf:5b:9f:c1:41" or key == "a0:cf:5b:9f:c1:40" or key == "a0:cf:5b:9f:c1:4e" or key == "a0:cf:5b:9f:c1:4f" or

                    key == "a0:cf:5b:a2:ce:40" or key == "a0:cf:5b:a2:ce:41" or key == "a0:cf:5b:a2:ce:4e" or key == "a0:cf:5b:a2:ce:4f"):

                if key not in y7_bssid:
                    y7_bssid.append(key)

    print(y7_bssid)     #检测收集的这一个文件里面有多少本层不同的bssid
    print(y6_bssid)
    print(y5_bssid)
    print(y4_bssid)
    print(y3_bssid)
    print(y2_bssid)
    print(y1_bssid)

    y1_rssi = []      #1.5秒会有一个字典 然后找这个字典里面对应的rssi
    y2_rssi = []
    y3_rssi = []
    y4_rssi = []
    y5_rssi = []
    y6_rssi = []
    y7_rssi = []



    for wifi_data in wifi_data_dic_list:
        y1_rssi_transfer = []
        for i in range(len(y1_bssid)):
            if y1_bssid[i] in wifi_data:
                y1_rssi_transfer.append(wifi_data[y1_bssid[i]])
            else:
                y1_rssi_transfer.append(None)
        y1_rssi.append(y1_rssi_transfer)




    for wifi_data in wifi_data_dic_list:
        y2_rssi_transfer = []
        for i in range(len(y2_bssid)):
            if y2_bssid[i] in wifi_data:
                y2_rssi_transfer.append(wifi_data[y2_bssid[i]])
            else:
                y2_rssi_transfer.append(None)
        y2_rssi.append(y2_rssi_transfer)

    for wifi_data in wifi_data_dic_list:
        y3_rssi_transfer = []
        for i in range(len(y3_bssid)):
            if y3_bssid[i] in wifi_data:
                y3_rssi_transfer.append(wifi_data[y3_bssid[i]])
            else:
                y3_rssi_transfer.append(None)
        y3_rssi.append(y3_rssi_transfer)

    for wifi_data in wifi_data_dic_list:
        y4_rssi_transfer = []
        for i in range(len(y4_bssid)):
            if y4_bssid[i] in wifi_data:
                y4_rssi_transfer.append(wifi_data[y4_bssid[i]])
            else:
                y4_rssi_transfer.append(None)
        y4_rssi.append(y4_rssi_transfer)


    for wifi_data in wifi_data_dic_list:
        y5_rssi_transfer = []
        for i in range(len(y5_bssid)):
            if y5_bssid[i] in wifi_data:
                y5_rssi_transfer.append(wifi_data[y5_bssid[i]])
            else:
                y5_rssi_transfer.append(None)
        y5_rssi.append(y5_rssi_transfer)

    for wifi_data in wifi_data_dic_list:
        y6_rssi_transfer = []
        for i in range(len(y6_bssid)):
            if y6_bssid[i] in wifi_data:
                y6_rssi_transfer.append(wifi_data[y6_bssid[i]])
            else:
                y6_rssi_transfer.append(None)
        y6_rssi.append(y6_rssi_transfer)

    for wifi_data in wifi_data_dic_list:
        y7_rssi_transfer = []
        for i in range(len(y7_bssid)):
            if y7_bssid[i] in wifi_data:
                y7_rssi_transfer.append(wifi_data[y7_bssid[i]])
            else:
                y7_rssi_transfer.append(None)
        y7_rssi.append(y7_rssi_transfer)


    x1 = np.arange(0, len(y1_bssid))
    x2 = np.arange(0, len(y2_bssid))
    x3 = np.arange(0, len(y3_bssid))
    x4 = np.arange(0, len(y4_bssid))
    x5 = np.arange(0, len(y5_bssid))
    x6 = np.arange(0, len(y6_bssid))
    x7 = np.arange(0, len(y7_bssid))

    plt.figure()


    for i in y1_rssi:
        plt.scatter(x1, np.array(i), c="red", alpha=0.6)


    for i in y2_rssi:
        plt.scatter(x2, np.array(i), c="blue", alpha=0.6)

    for i in y3_rssi:
        plt.scatter(x3, np.array(i), c="green", alpha=0.6)

    for i in y4_rssi:
        plt.scatter(x4, np.array(i), c="yellow", alpha=0.6)

    for i in y5_rssi:
        plt.scatter(x5, np.array(i), c="black", alpha=0.6)

    for i in y6_rssi:
        plt.scatter(x6, np.array(i), c="magenta", alpha=0.6)

    for i in y7_rssi:
        plt.scatter(x7, np.array(i), c="cyan", alpha=0.6)

    plt.show()

    return 0
test2 = draw_picture()