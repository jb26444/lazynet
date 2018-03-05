import sys


word = "#"
f = open("base.txt", "r+")
d = f.readlines()
f.seek(0)
for line in d:
    if word in d:
       print (d.split(word))
       f.write(d)
f.truncate()
f.close()
