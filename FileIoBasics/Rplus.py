fh = open("rplus.txt","r+")
# a = fh.write(" (r+) mode is used for read and write both operation we can do\n")
# print(fh.read())

# a = fh.write("\n Welcome here!")
# print(a)
# print(fh.read())
# fh.close()
print(fh.read())
fh.write("\n Welcome here!")
fh.close()

# in r+ mode only it is used when we need to read the content then write

# if we first write the content in the file then we read so in
# this case it does give expected output  becuase
# new content will be overwrite to old contenet