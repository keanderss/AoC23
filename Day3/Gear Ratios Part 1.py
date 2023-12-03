import re

filename = ("input.txt")
lines = 0
slen = 0
tot = 0
#line counter
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
#creates the map
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
    i += 1

#prints the map
def printMap(m):
    i = 0
    for y in m:
        print("y" + str(i) + ": \t" + str(y))
        i += 1
print()
print()
print()
printMap(m)
print()
print()
print()


def findNumb(m1,m2,x,y):
    for i in range(3):
        for j in range(3):
            x2 = x+i-1
            y2 = y+j-1
            if x2 < 0:
                x2 = 0
            if y2 < 0:
                y2 = 0
            if x2 > slen-1:
                x2 = slen-1
            if y2 > lines-1:
                y2 = lines-1
            if m2[y2][x2] == ".":
                numb = re.findall("[0-9]", m1[y2][x2])
                if len(numb) > 0:
                    m2[y2][x2] = numb[0]
                    findNumb(m1,m2,x2,y2)

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
        symb = re.findall("[^0-9.]", m[yi][xi])
        if len(symb) > 0:
            findNumb(m, m2, xi, yi)

numArray = []
def numBuilder():
    for q in m2:
        temp = []
        for i in range(len(q)):
            if q[i] != ".":
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

diffchecker()

numBuilder()
printMap(m2)
print()
printMap(m3)
print(numArray)
tot = 0
for n in numArray:
    tot += n

print("sumtotal: " + str(tot))

