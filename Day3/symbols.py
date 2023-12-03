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
    #finds all matches and puts them into an array
    s = re.sub("[.]","", s)
    s = re.sub("[0-9]", "", s)
    s = re.sub("[\n]", "", s)
    s = re.sub("[*]", "", s)
    s = re.sub("[-]", "", s)
    s = re.sub("[%]", "", s)
    s = re.sub("[$]", "", s)
    s = re.sub("[=]", "", s)
    s = re.sub("[@]", "", s)
    s = re.sub("[#]", "", s)
    s = re.sub("[/]", "", s)
    s = re.sub("[&]", "", s)
    s = re.sub("[+]", "", s)
    #   @#$%&/=+-*
    print(s)