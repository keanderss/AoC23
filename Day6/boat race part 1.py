import linecache

filename = "input.txt"
lines = []
races = []


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


def race(r):
    time = r[0]
    speed = 0
    record = r[1]
    margins = []
    for hold in range(time + 1):
        t = time - hold
        print("hold: " + str(hold) + " \ttime: " + str(t) + " \tspeed: " + str(speed) + " \trecord: " + str(record))
        distance = speed * t
        if distance > record:
            margins.append(distance)
        speed += 1
    print("Ways to beat record: " + str(len(margins)))
    return len(margins)

initialize()
print(races)
m = 1
for r in races:
    m *= race(r)
print(m)
