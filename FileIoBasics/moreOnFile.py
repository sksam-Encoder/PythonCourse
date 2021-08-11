fh = open("scratch.txt")
print(fh.tell())  # points the character for reading
print(fh.readline())
print(fh.tell())
print(fh.readline())
fh.seek(0)  # make file handel to point specific character.
print(fh.readline())

fh.close()
