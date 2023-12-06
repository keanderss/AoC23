import re
import linecache


def calcpoints(card):
    nums = []
    wnums = []
    win = False
    points = 0
    for q in card:
        if win:
            if q.isnumeric():
                wnums.append(q)
        elif q == "|":
            win = True
        else:
            if q.isnumeric():
                nums.append(q)
    for w in wnums:
        for n in nums:
            if w == n:
                points += 1
    return points


cards = []


def drawcard(i):
    s = str(linecache.getline("input.txt", i))
    print(s)
    s2 = s.split()
    if len(s2) > 0:
        cards.append(i)
    points = calcpoints(s2)
    print(points)
    for p in range(points):
        #print("1 draws 8, 2 draws 2, 3 draws 2, 4 draws 1")
        print("holding card: " + str(i))
        print("drawing card: " + str(i + p + 1))
        drawcard(i + p + 1)
    return s


# main loop
i = 1
while True:
    s = drawcard(i)
    if s == "":
        break
    i += 1

print(cards)
tot = len(cards)
print("sumtotal: " + str(tot))
