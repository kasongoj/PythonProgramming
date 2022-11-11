
#f = open("inputFile1","r")
#f = open("inputFile1", "rt")   #r: read  #t:text
#f = open("inputFile1", "at")   #a: apped #t: text
# f = open("inputFile", "at")
# f.write("adding another line to input file")
# print(f.read())
g = open("inputFile1", "w")
g.write("kasongo")
g = open("inputFile1", "r")
print(g.read())

