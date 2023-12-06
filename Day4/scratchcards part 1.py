import re

f = open("input.txt", "r")
c = 0
tot = 0
#main loop
while True:
    s = f.readline()
    sog = re.sub("\n", "", s) #og string
    c += 1
    #breaks loop if the read line is empty
    if s == "":
        break
    s2 = s.split()
    i = 0
    nums = []
    wnums = []
    win = False
    points = 0
    for q in s2:
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
                if points > 0:
                    points *= 2
                else:
                    points += 1
    tot += points




    print(s2)


    #count the sumtotal
    ##tot += int(s4)
    #output
    ##print(str(c) + ": " + sog + "\t\t\t\t\tno-abc: " + s3 + "\t\t\t\t\tfinal: " + s4)
print("sumtotal: " + str(tot))
