import data_process as dp

fileObject = open("/Users/jianguan/Desktop/毕业/楼层判定实验数据/CC1-5.txt", 'w')
for ip in dp.get_barometric():
	fileObject.write(str(ip))
	fileObject.write('\n')
fileObject.close()
print("finished")