from data_process import getmaxbarometric


class Combine:

    def combine_floor(self):

        wifi_floor_list = getmaxbarometric()
        floor_baro = []
        for floor_dic in wifi_floor_list:
            floor_baro.append(floor_dic[list(floor_dic)[-1]])

        the_same_floor = []

        for i in range(len(floor_baro)):
            change = i
            while change <= len(floor_baro)-2:
                orignal = i
                diffierence = abs(abs(floor_baro[orignal]) - abs(floor_baro[change+1]))
                if diffierence < 0.039:
                    the_same_floor.append(orignal)
                    the_same_floor.append(change+1)
                change = change + 1

        the_same_floor = list(zip(the_same_floor[0::2],the_same_floor[1::2]))

        for i in the_same_floor:
            for key in wifi_floor_list[i[1]]:
                if len(key) == 17:
                    if key in wifi_floor_list[i[0]]:
                        wifi_floor_list[i[1]][key] = list(set(wifi_floor_list[i[0]][key] + wifi_floor_list[i[1]][key]))
                    else:
                        wifi_floor_list[i[0]][key] = wifi_floor_list[i[1]][key]
        delete_floor = []
        for i in the_same_floor:
            delete_floor.append(i[1])
        delete_floor.sort(reverse=True)


        for i in delete_floor:
            wifi_floor_list.pop(i)


        return wifi_floor_list
combine = Combine()
# print(combine.combine_floor())
# print(len(combine.combine_floor()[0]))
# print(len(combine.combine_floor()[1]))
# print(len(combine.combine_floor()[2]))
# print(len(combine.combine_floor()[3]))
