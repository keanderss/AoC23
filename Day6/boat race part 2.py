import linecache

filename = "input.txt"
lines = []
races = []
therace = ["", ""]


def initialize():
    i = 0
    while True:
        i += 1
        line = linecache.getline(filename, i)
        if line == "":
            break
        strings = line.split()
        lines.append(strings)
    for i in range(len(lines[0])):
        if lines[0][i].isnumeric() and lines[1][i].isnumeric():
            r = int(lines[0][i]), int(lines[1][i])
            races.append(r)

    for r in races:
        therace[0] = therace[0] + str(r[0])
        therace[1] = therace[1] + str(r[1])


def race(r):
    time = int(r[0])
    speed = 0
    record = int(r[1])
    margins = []
    for hold in range(time + 1):
        t = time - hold
        distance = speed * t
        if distance > record:
            margins.append(distance)
        speed += 1
    print("Ways to beat record: " + str(len(margins)))
    return len(margins)


initialize()
race(therace)

