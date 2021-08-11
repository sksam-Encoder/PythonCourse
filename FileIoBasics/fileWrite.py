# fh = open("fle.txt","w")
# fh.write("w(mode)->  write method is basically used for writing contents in file..\n"
#          "and the w mode erase the previous content and rewrite")
# print(type(fh))
# fh.close()
# fh = open("fle.txt","a")
# a = fh.write("\na(mode) is commonly used for appending the contents into file \n"
#          " without erasing previous contents")
# print(a)
# fh.close()

#  Handle read and write both oprations
fh = open("fle2.txt","r+")
# a = fh.write(" (r+) mode is used for read and write both operation we can do\n")
print(fh.read())
a = fh.write("\n content is over!")
print(a)
print(fh.read())
fh.close()
#  we cant se the result specific time bec when we open the file whatever the operation we performed
# it cant be visible because the file is still open and the file resources is already been used
#  for seeing the result again we have to close and reopen the file.

