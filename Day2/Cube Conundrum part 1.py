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
    g = int(re.sub("[^0-9]", "", s2[1]))
    s2 = s2
    i = 0
    impossible = False
    for q in s2:
        print("Q: " + q)
        x = re.sub("[^0-9]", "", s2[i])
        print("s: " + x)
        try:
            x = int(x)
        except:
            x = 0
        print("X: " + str(x))
        if (i%2) == 0:
            if s2[i + 1].startswith("red"):
                if x > 12:
                    impossible = True
                    break
            elif s2[i + 1].startswith("green"):
                if x > 13:
                    impossible = True
                    break
            else:
                if x > 14:
                    impossible = True
                    break
            i += 1
        else:
            i += 1
            continue
    if not impossible:
        tot += g

    print(impossible)
    print(g)
    print(s2)


    #count the sumtotal
    ##tot += int(s4)
    #output
    ##print(str(c) + ": " + sog + "\t\t\t\t\tno-abc: " + s3 + "\t\t\t\t\tfinal: " + s4)
print("sumtotal: " + str(tot))
