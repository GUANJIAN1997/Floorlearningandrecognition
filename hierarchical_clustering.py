import numpy as np
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster
import data_process as dp
from matplotlib import pyplot as plt
# def Tonumpy(dp):
#     barometric_n = []
#     transfer = []
#     for i in dp.get_barometric():
#         transfer.append(i)
#         barometric_n.append(transfer)
#         transfer = []
#     barometric_numpy = np.array(barometric_n)
#     return barometric_numpy

def Tonumpy2(dp):
    upordown_n = []
    transfer = []
    a = dp.upordown(dp.get_barometric())[0]
    for i in a:
        transfer.append(i)
        upordown_n.append(transfer)
        transfer = []
    upordown_numpy = np.array(upordown_n)
    return upordown_numpy
# print(Tonumpy2(dp))

def clustering(dp,method="single",threshold = 0.3):
    a = Tonumpy2(dp)
    Z = linkage(a,"single")
    cluster_assignments = fcluster(Z, threshold, criterion='distance')
    # print(cluster_assignments)
    num_clusters = cluster_assignments.max()
    return cluster_assignments,num_clusters
# s = clustering(dp)
# print(s)
# x = np.arange(0,len(Tonumpy(dp)))
# plt.figure(figsize=(25, 10))
# plt.scatter(x,Tonumpy(dp)[:, 0])
# plt.show()

plt.figure(figsize=(10, 8))


plt.scatter(np.arange(0,len(Tonumpy2(dp))), Tonumpy2(dp)[:, 0], c=clustering(dp,method="single",threshold = 0.3)[0], cmap = "jet")
plt.show()

def find_floor():
    floor_list = []
    a = dp.getmaxbarometric()         #得到大于50的wifi和对应气压的字典
    b = dp.upordown(dp.get_barometric())[0]   #得到除去上下楼的气压
    c = clustering(dp,method="single",threshold = 0.3)
    print(c[0])
    # for i in a:
    #     s = b.index(a[i])
    #     floor = c[0][s]
    #     floor_list.append(floor)
    #
    #
    #
    # # s = dp.upordown(dp.get_barometric())[0].index(989.5461)
    # # floor = clustering[0][s]　　
    #
    #
    # d = []
    # e = []
    # f = []
    # g = []
    #
    # maxwifimac = []
    # num = 0
    # for i in floor_list:
    #     if i == 1:
    #         d.append(num)
    #         num = num + 1
    #     if i == 2:
    #         e.append(num)
    #         num = num + 1
    #     if i == 3:
    #         f.append(num)
    #         num = num + 1
    #     if i == 4:
    #         g.append(num)
    #         num = num + 1
    #
    # for i in a:
    #     maxwifimac.append(i)
    #
    # class1 = []
    # class2 = []
    # class3 = []
    # class4 = []
    #
    # for i in d:
    #     class1.append(maxwifimac[i])
    # for i in e:
    #     class2.append(maxwifimac[i])
    # for i in f:
    #     class3.append(maxwifimac[i])
    # for i in g:
    #     class4.append(maxwifimac[i])
    #
    #
    # class1_baro = []
    # class2_baro = []
    # class3_baro = []
    # class4_baro = []
    #
    #
    # for i in class1:
    #     class1_baro.append(a[i])
    # for i in class2:
    #     class2_baro.append(a[i])
    # for i in class3:
    #     class3_baro.append(a[i])
    # for i in class4:
    #     class4_baro.append(a[i])
    #
    # # print(class4_baro)
    # class1_baro_median = np.median(class1_baro)
    # class2_baro_median = np.median(class2_baro)
    # class3_baro_median = np.median(class3_baro)
    # class4_baro_median = np.median(class4_baro)
    #
    # # print(class1_baro_median,class2_baro_median,class3_baro_median,class4_baro_median,class5_baro_median)
    #
    # differnce1_5 = class1_baro_median - class3_baro_median
    # differnce5_6 = class3_baro_median - class4_baro_median
    # differnce5_3 = class3_baro_median - class2_baro_median
    # differnce3_1 = class2_baro_median - class1_baro_median
    # class1.append("X0")
    # class3.append("X0-"+str(round(differnce1_5,4)))
    #
    # class4.append("X0-"+str(round(differnce5_6+differnce1_5,4)))
    #
    # class2.append("X0-"+str(round(differnce5_3+differnce1_5,4)))

    return 0

test = find_floor()
print(test)
