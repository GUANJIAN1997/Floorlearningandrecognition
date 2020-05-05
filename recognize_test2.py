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
                if i[key] > -90:
                    floor1[key]=[]
                    floor1[key].append(i[key])
            elif i[key] > -90:
                floor1[key].append(i[key])


    for i in wifi_data_dic_list[1]:
        for key in i:
            if key not in floor2:
                if i[key] > -90:
                    floor2[key]=[]
                    floor2[key].append(i[key])
            elif i[key] > -90:
                floor2[key].append(i[key])

    for i in wifi_data_dic_list[2]:
        for key in i:
            if key not in floor3:
                if i[key] > -90:
                    floor3[key]=[]
                    floor3[key].append(i[key])
            elif i[key] > -90:
                floor3[key].append(i[key])

    for i in wifi_data_dic_list[3]:
        for key in i:
            if key not in floor4:
                if i[key] > -90:
                    floor4[key]=[]
                    floor4[key].append(i[key])
            elif i[key] > -90:
                floor4[key].append(i[key])

    for i in wifi_data_dic_list[4]:
        for key in i:
            if key not in floor5:
                if i[key] > -90:
                    floor5[key]=[]
                    floor5[key].append(i[key])
            elif i[key] > -90:
                floor5[key].append(i[key])

    for i in wifi_data_dic_list[5]:
        for key in i:
            if key not in floor6:
                if i[key] > -90:
                    floor6[key]=[]
                    floor6[key].append(i[key])
            elif i[key] > -90:
                floor6[key].append(i[key])

    for i in wifi_data_dic_list[6]:
        for key in i:
            if key not in floor7:
                if i[key] > -90:
                    floor7[key]=[]
                    floor7[key].append(i[key])
            elif i[key] > -90:
                floor7[key].append(i[key])
    learned_floor=[]
    learned_floor.append(floor1)
    learned_floor.append(floor2)
    learned_floor.append(floor3)
    learned_floor.append(floor4)
    learned_floor.append(floor5)
    learned_floor.append(floor6)
    learned_floor.append(floor7)






    return learned_floor


# print(find_floor())



