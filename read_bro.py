import json
test3 = []
test4 = []
test = open("/Users/jianguan/Desktop/CC1-5.json","r")
for line in test:
    test2 = json.loads(line)
    test3.append(test2)
test.close()

for i in test3:
    if "hpa" in i:
        test4.append(i["hpa"])
fileObject = open('/Users/jianguan/Desktop/CC1-5.txt', 'w')
for ip in test4:
	fileObject.write(str(ip))
	fileObject.write('\n')
fileObject.close()
print("finished")