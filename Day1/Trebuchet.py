import re

f = open("input.txt", "r")
c = 0
tot = 0
while True:
    s = f.readline()
    sog = re.sub("\n", "", s)
    c += 1
    if s == "":
        break
    s2 = []
    for x in s:
        s2.extend(re.findall("^one|^two|^three|^four|^five|^six|^seven|^eight|^nine|^[1-9]", s))
        s = s[1:]
    i = 0
    for x in s2:
        s2[i] = re.sub("one", "1", s2[i])
        s2[i] = re.sub("two", "2", s2[i])
        s2[i] = re.sub("three", "3", s2[i])
        s2[i] = re.sub("four", "4", s2[i])
        s2[i] = re.sub("five", "5", s2[i])
        s2[i] = re.sub("six", "6", s2[i])
        s2[i] = re.sub("seven", "7", s2[i])
        s2[i] = re.sub("eight", "8", s2[i])
        s2[i] = re.sub("nine", "9", s2[i])
        i += 1
    s3 = ""
    for x in s2:
        s3 += x
    s4 = s2[0] + s2[-1]
    tot += int(s4)
    print(str(c) + ": " + sog + "\t\t\t\t\tno-abc: " + s3 + "\t\t\t\t\tfinal: " + s4)
print("sumtotal: " + str(tot))
