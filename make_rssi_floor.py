
from data_process import json2List
import matplotlib.pyplot as plt
import numpy as np

# filepath1 = "/Users/jianguan/Desktop/毕业/预实验/1.1.1.json"
# filepath2 = "/Users/jianguan/Desktop/毕业/预实验/2.2.2.json"
# filepath3 = "/Users/jianguan/Desktop/毕业/预实验/3.3.3.json"
# filepath4 = "/Users/jianguan/Desktop/毕业/预实验/4.4.4.json"
# filepath5 = "/Users/jianguan/Desktop/毕业/预实验/5.5.5.json"
# filepath6 = "/Users/jianguan/Desktop/毕业/预实验/6.6.6.json"
# filepath7 = "/Users/jianguan/Desktop/毕业/预实验/7.7.7.json"

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


def make_x():      #得到一个三维列表36个bssid里面有7个楼层的rssi  36，7

    wifi_data_dic = find_ritsumei()

    global floor_bssid
    floor_bssid =["a0:cf:5b:9f:bb:f0","a0:cf:5b:9f:bb:f1","a0:cf:5b:9f:bb:fe","a0:cf:5b:9f:bb:ff",
                   "a0:cf:5b:9f:af:00","a0:cf:5b:9f:af:01","a0:cf:5b:9f:af:0f","a0:cf:5b:9f:af:0e",
                   "a0:cf:5b:9f:b0:91","a0:cf:5b:9f:b0:90","a0:cf:5b:9f:b0:9e","a0:cf:5b:9f:b0:9f",
                   "f0:29:29:60:3a:10","f0:29:29:60:3a:11","f0:29:29:60:3a:1e","f0:29:29:60:3a:1f",
                   "a0:cf:5b:c2:2d:81","a0:cf:5b:c2:2d:80","a0:cf:5b:c2:2d:8e","a0:cf:5b:c2:2d:8f",
                   "a0:cf:5b:9f:dd:00","a0:cf:5b:9f:dd:01","a0:cf:5b:9f:dd:0e","a0:cf:5b:9f:dd:0f",
                   "a0:cf:5b:a3:7e:d1","a0:cf:5b:a3:7e:d0","a0:cf:5b:a3:7e:de","a0:cf:5b:a3:7e:df",
                   "a0:cf:5b:a3:7e:50","a0:cf:5b:a3:7e:51","a0:cf:5b:a3:7e:5e","a0:cf:5b:a3:7e:5f",
                   "a0:cf:5b:9f:d4:60","a0:cf:5b:9f:d4:61","a0:cf:5b:9f:d4:6e","a0:cf:5b:9f:d4:6f",
                   "a0:cf:5b:9f:cd:20","a0:cf:5b:9f:cd:21","a0:cf:5b:9f:cd:2e","a0:cf:5b:9f:cd:2f",
                   "a0:cf:5b:a3:a3:60","a0:cf:5b:a3:a3:61","a0:cf:5b:a3:a3:6e","a0:cf:5b:a3:a3:6f",
                   "a0:cf:5b:c2:00:e0","a0:cf:5b:c2:00:e1","a0:cf:5b:c2:00:ee","a0:cf:5b:c2:00:ef",
                   "a0:cf:5b:a3:4f:50","a0:cf:5b:a3:4f:51","a0:cf:5b:a3:4f:5e","a0:cf:5b:a3:4f:5f",
                   "a0:cf:5b:9f:36:1e","a0:cf:5b:9f:36:1f","a0:cf:5b:9f:36:10","a0:cf:5b:9f:36:11",
                   "a0:cf:5b:a3:4b:70","a0:cf:5b:a3:4b:71","a0:cf:5b:a3:4b:7e","a0:cf:5b:a3:4b:7f",
                   "a0:cf:5b:9f:cc:e0","a0:cf:5b:9f:cc:e1","a0:cf:5b:9f:cc:ee","a0:cf:5b:9f:cc:ef",
                   "a0:cf:5b:a3:21:f1","a0:cf:5b:a3:21:f0","a0:cf:5b:a3:21:fe","a0:cf:5b:a3:21:ff",
                   "a0:cf:5b:9f:cc:f0","a0:cf:5b:9f:cc:f1","a0:cf:5b:9f:cc:fe","a0:cf:5b:9f:cc:ff",
                   "a0:cf:5b:9f:c6:c0","a0:cf:5b:9f:c6:c1","a0:cf:5b:9f:c6:ce","a0:cf:5b:9f:c6:cf",
                   "a0:cf:5b:a3:8b:91","a0:cf:5b:a3:8b:90","a0:cf:5b:a3:8b:9e","a0:cf:5b:a3:8b:9f",
                   "a0:cf:5b:a3:5d:30","a0:cf:5b:a3:5d:31","a0:cf:5b:a3:5d:3e","a0:cf:5b:a3:5d:3f",
                   "a0:cf:5b:a2:ce:7e","a0:cf:5b:a2:ce:7f","a0:cf:5b:a2:ce:70","a0:cf:5b:a2:ce:71",
                   "a0:cf:5b:a3:4f:f0","a0:cf:5b:a3:4f:f1","a0:cf:5b:a3:4f:fe","a0:cf:5b:a3:4f:ff",
                   "a0:cf:5b:9f:e7:a1","a0:cf:5b:9f:e7:a0","a0:cf:5b:9f:e7:ae","a0:cf:5b:9f:e7:af",
                   "a0:cf:5b:9f:36:80","a0:cf:5b:9f:36:81","a0:cf:5b:9f:36:8e","a0:cf:5b:9f:36:8f",
                   "a0:cf:5b:9f:d1:a0","a0:cf:5b:9f:d1:a1","a0:cf:5b:9f:d1:ae","a0:cf:5b:9f:d1:af",
                   "a0:cf:5b:a3:52:c1","a0:cf:5b:a3:52:c0","a0:cf:5b:a3:52:ce","a0:cf:5b:a3:52:cf",
                   "a0:cf:5b:9f:d3:70","a0:cf:5b:9f:d3:71","a0:cf:5b:9f:d3:7e","a0:cf:5b:9f:d3:7f",
                   "a0:cf:5b:a3:5e:20","a0:cf:5b:a3:5e:21","a0:cf:5b:a3:5e:2e","a0:cf:5b:a3:5e:2f",
                   "a0:cf:5b:9f:c6:f0","a0:cf:5b:9f:c6:f1","a0:cf:5b:9f:c6:fe","a0:cf:5b:9f:c6:ff",
                   "a0:cf:5b:c2:0e:21","a0:cf:5b:c2:0e:20","a0:cf:5b:c2:0e:2e","a0:cf:5b:c2:0e:2f",
                   "a0:cf:5b:a3:79:50","a0:cf:5b:a3:79:51","a0:cf:5b:a3:79:5e","a0:cf:5b:a3:79:5f",
                   "a0:cf:5b:c2:0b:91","a0:cf:5b:c2:0b:90","a0:cf:5b:c2:0b:9e","a0:cf:5b:c2:0b:9f",
                   "a0:cf:5b:9f:c1:41","a0:cf:5b:9f:c1:40","a0:cf:5b:9f:c1:4e","a0:cf:5b:9f:c1:4f",
                   "a0:cf:5b:a2:ce:40","a0:cf:5b:a2:ce:41","a0:cf:5b:a2:ce:4e","a0:cf:5b:a2:ce:4f"]

    bssid_rssi = []

    for bssid in floor_bssid:
        rssi_floor_multi_bssid = []
        for wifi_data_dic_floor_number in range(len(wifi_data_dic)):
            rssi_floor_one_bssid = []
            for wifi_data_dic_floor_i in wifi_data_dic[wifi_data_dic_floor_number]:
                if bssid in wifi_data_dic_floor_i:
                    rssi_floor_one_bssid.append(wifi_data_dic_floor_i[bssid])
            rssi_floor_multi_bssid.append(rssi_floor_one_bssid)
        bssid_rssi.append(rssi_floor_multi_bssid)

    x = bssid_rssi
    for i in x:
        for j in range(len(i)):
            i[j] = np.array(i[j])


    return x


def make_y():
    bssid_rssi = make_x()


    y_floor = []

    for bssid_multi_floor_rssi in bssid_rssi:
        y_floor_each_bssid = []
        for rssi_floor_one_number in range(len(bssid_multi_floor_rssi)):
            y_floor_i = []
            for i in range(len(bssid_multi_floor_rssi[rssi_floor_one_number])):
                y_floor_i.append(rssi_floor_one_number + 1)
            y_floor_each_bssid.append(y_floor_i)
        y_floor.append(y_floor_each_bssid)

    y = y_floor

    for i in y:
        for j in range(len(i)):
            i[j] = np.array(i[j])

    return y


def make_figure():

    x = make_x()
    y = make_y()
    global floor_bssid
    for number in range(len(x)):

        plt.figure()
        plt.title(floor_bssid[number])
        for i in range(len(x[number])):
            plt.scatter(x[number][i],y[number][i])
        plt.savefig("/Users/jianguan/Desktop/毕业/预实验/图片/" + str(floor_bssid[number]))
        plt.show()


    plt.close("all")
    
    return 0











