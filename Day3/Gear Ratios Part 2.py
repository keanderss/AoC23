import re

filename = ("input.txt")
lines = 0
slen = 0
tot = 0
# line counter
f = open(filename, "r")
while True:
    s = f.readline()
    if s == "":
        break
    slen = len(s)
    lines += 1
f = open(filename, "r")
i = 0
m = [[]] * lines
m2 = [[]] * lines
m3 = [[]] * lines
m4 = [[]] * lines
# creates the map
while True:
    s = f.readline()
    if s == "":
        break
    y = []
    for q in s:
        y.extend(q)
    m[i] = y
    y2 = ["."] * len(s)
    m2[i] = y2
    y3 = ["."] * len(s)
    m3[i] = y3
    y4 = ["."] * len(s)
    m4[i] = y4
    i += 1


# prints the map
def printMap(m):
    i = 0
    for y in m:
        print("y" + str(i) + ": \t" + str(y))
        i += 1


def findNumb(m1, m2, x, y):
    for i in range(3):
        for j in range(3):
            x2 = x + i - 1
            y2 = y + j - 1
            if x2 < 0:
                x2 = 0
            if y2 < 0:
                y2 = 0
            if x2 > slen - 1:
                x2 = slen - 1
            if y2 > lines - 1:
                y2 = lines - 1
            if m2[y2][x2] == ".":
                numb = re.findall("[0-9*]", m1[y2][x2])
                if len(numb) > 0:
                    m2[y2][x2] = numb[0]
                    findNumb(m1, m2, x2, y2)

ratioList = []
def findLplusRatio(map1, map2, x, y):
    xlist = []
    ylist = []
    for j in range(3):
        contig = False
        for i in range(3):
            x2 = x + i - 1
            y2 = y + j - 1
            if x2 < 0:
                x2 = 0
            if y2 < 0:
                y2 = 0
            if x2 > slen - 1:
                x2 = slen - 1
            if y2 > lines - 1:
                y2 = lines - 1
            print()
            print("map1: " + map1[y2][x2])
            print("map2: " + map2[y2][x2])
            if map2[y2][x2] == ".":
                print("y2: " + str(y2))
                print("x2: " + str(x2))
                symb = re.findall("[*]", map1[y2][x2])
                numb = re.findall("[0-9]", map1[y2][x2])
                if len(symb) > 0:
                    map2[y2][x2] = symb[0]
                    print("hello")
                if len(numb) > 0:
                    if not contig:
                        print("numb: " + str(numb))
                        xlist.append(x2)
                        ylist.append(y2)
                        print(xlist)
                        print(ylist)
                        # m2[y2][x2] = numb[0]
                        # findNumb(m1,m2,x2,y2)
                        contig = True
                else:
                    contig = False
    if len(xlist) % 2 == 0:
        nlist = []
        for c in range(2):
            x3 = xlist[c]
            y3 = ylist[c]
            while map1[y3][x3] != "." and map1[y3][x3] != "*":
                x3 -= 1
                print("hi")
            x3 += 1
            n = ""
            print(x3)
            print(y3)
            print(map1[y3][x3])
            while map1[y3][x3] != "." and map1[y3][x3] != "*":
                n += map1[y3][x3]
                x3 += 1
                ##print("sup")
            if len(n) > 0:
                print("n: " + n)
                nlist.append(n)
        print("xlist: " + str(xlist))
        print("ylist: " + str(ylist))
        print(nlist)
        ratioList.append(int(nlist[0]) * int(nlist[1]))
        print("rlist: " + str(ratioList))



# my dogshit code
# yi = 0
# for y in m:
#     xi = 0
#     for x in y:
#         ##symb = re.findall("@|#|[$]|%|&|/|=|[+]|-|[*]", m[yi][xi])     # @#$%&/=+-*
#         symb = re.findall("[^0-9.]", m[yi][xi])
#         if len(symb) > 0:
#             findNumb(m, m2, xi, yi)
#         xi += 1
#     yi += 1

# ChatGPT bugfix that actually works!
for yi in range(lines):
    for xi in range(slen):
        symb = re.findall("[*]", m[yi][xi])
        if len(symb) > 0:
            findNumb(m, m2, xi, yi)

for yi in range(lines):
    for xi in range(slen):
        symb = re.findall("[*]", m2[yi][xi])
        if len(symb) > 0:
            findLplusRatio(m2, m4, xi, yi)

numArray = []


def numBuilder():
    for q in m2:
        temp = []
        for i in range(len(q)):
            if q[i] != "." and q[i] != "*":
                temp.extend(q[i])
            else:
                if len(temp) > 0:
                    n = ""
                    for t in temp:
                        n += str(t)
                    numArray.append(int(n))
                    temp = []


def diffchecker():
    for i in range(lines):
        for j in range(slen):
            if m[i][j] == m2[i][j]:
                m3[i][j] = m[i][j]
            else:
                if m2[i][j] == ".":
                    symb = re.findall("[^0-9.]", m[i][j])
                    if len(symb) > 0:
                        m3[i][j] = "s"
                    else:
                        m3[i][j] = "d"
                else:
                    m3[i][j] = "!"


# diffchecker()
numBuilder()
print()
printMap(m)
print()
printMap(m2)
print()
# printMap(m3) #diffmap
print()
printMap(m4)
print()
print(ratioList)
print()
tot = 0
for n in ratioList:
    tot += n

print("sumtotal: " + str(tot))
