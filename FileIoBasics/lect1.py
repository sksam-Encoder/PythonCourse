# fp = open("scratch.txt")  rb -> reads the file in binary form , rt -> reads the file in text mode
fp = open("scratch.txt", "rt")
count = 0
# content  =fp.read()
# print(type(content))
# print(content)

#  reading contents line by line
# for ln in fp:
#     print(ln)
#     count+=1

for line in fp:
    print(line, end=" ")

fp.close()
# print('count =',count)
