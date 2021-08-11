# open file through with block
with open("withblk.txt","w") as f:
     print(f.readlines())


fh = open("scratch.txt","rt")
print(fh.readlines())
fh.close()