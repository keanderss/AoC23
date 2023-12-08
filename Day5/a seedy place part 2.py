import linecache
import sys
import threading

filename = "input.txt"
seedranges = []
seedtosoil = []
soiltofertilizer = []
fertilizertowater = []
watertolight = []
lighttotemperature = []
temperaturetohumidity = []
humiditytolocation = []
locations = []
rangepairs = []
threads = []
seedcount = 0
rangemaps = []


def convert(m, i):
    for j in m:
        if j[1] <= i <= j[1] + j[2]:
            return i + (j[0] - j[1])
    return i


def createmap(map, i):
    while True:
        line = linecache.getline(filename, i)
        linearray = line.split()
        if len(linearray) == 0:
            break
        map.append([int(numeric_string) for numeric_string in linearray])
        i += 1
    return map


def printmap(m):
    i = 0
    for y in m:
        print("y" + str(i) + ": \t" + str(y))
        i += 1


def initialize():
    print("Initializing!\n")
    i = 0
    mapcount = 0
    while True:
        i += 1
        line = linecache.getline(filename, i)
        if line.startswith("seeds:"):
            print("Loading seeds!")
            linearrway = line.split()
            for j in linearrway:
                if j.isnumeric():
                    seedranges.append(j)
            print(seedranges)
        elif line.startswith("seed-to-soil map:"):
            print("Creating seed to soil map!")
            createmap(seedtosoil, i + 1)
            print(seedtosoil)
            rangemaps.append(seedtosoil)
            mapcount += 1
        elif line.startswith("soil-to-fertilizer map:"):
            print("Creating soil to fertilizer map!")
            createmap(soiltofertilizer, i + 1)
            print(soiltofertilizer)
            rangemaps.append(soiltofertilizer)
            mapcount += 1
        elif line.startswith("fertilizer-to-water map:"):
            print("Creating fertilizer to water map!")
            createmap(fertilizertowater, i + 1)
            print(fertilizertowater)
            rangemaps.append(fertilizertowater)
            mapcount += 1
        elif line.startswith("water-to-light map:"):
            print("Creating water to light map!")
            createmap(watertolight, i + 1)
            print(watertolight)
            rangemaps.append(watertolight)
            mapcount += 1
        elif line.startswith("light-to-temperature map:"):
            print("Creating light to temperature map!")
            createmap(lighttotemperature, i + 1)
            print(lighttotemperature)
            rangemaps.append(lighttotemperature)
            mapcount += 1
        elif line.startswith("temperature-to-humidity map:"):
            print("Creating temperature to humidity map!")
            createmap(temperaturetohumidity, i + 1)
            print(temperaturetohumidity)
            rangemaps.append(temperaturetohumidity)
            mapcount += 1
        elif line.startswith("humidity-to-location map:"):
            print("Creating humidity to location map!")
            createmap(humiditytolocation, i + 1)
            print(humiditytolocation)
            rangemaps.append(humiditytolocation)
            mapcount += 1
        else:
            if mapcount == 7:
                for i in range(len(seedranges)):
                    if i % 2 == 0:
                        seedi = seedranges[i]
                        seedinti = int(seedi)
                        seedp1 = seedranges[i + 1]
                        seedintp1 = int(seedp1)
                        pair = (seedinti, seedinti + seedintp1)
                        rangepairs.append(pair)
                return len(rangepairs)
            if i > 999:
                print("Initialization error!")
                break


class ProgressTracker:
    def __init__(self, seeds):
        self.seedtotal = seeds
        self.seedtotalstr = str(seeds)
        self.remaining = seeds
        self.progress = int((1 - (self.remaining / self.seedtotal)) * 100)
        self.lowestlocation = sys.maxsize
        self.threadcount = 0

    def gettotal(self):
        return self.seedtotal

    def subremaining(self):
        self.remaining -= 1
        self.progress = int((1 - (self.remaining / self.seedtotal)) * 100)

    def getprogressstr(self):
        return str(self.remaining) + "/" + self.seedtotalstr + " (" + str(self.progress) + "%)"

    def getlowest(self):
        return self.lowestlocation

    def checklocation(self, location):
        if location < self.lowestlocation:
            self.lowestlocation = location

    def trackthread(self):
        self.threadcount += 1

    def stoptracking(self):
        self.threadcount -= 1
        if self.threadcount == 0:
            print()
            print("Done! Lowest location: " + str(self.getlowest()))
            print()


def scanrange(start, stop):
    pt.trackthread()
    for seed in range(start, stop):
        print("Remaining: " + pt.getprogressstr() + "\tSeed: " + str(
            seed) + " \tThreads: " + str(threading.active_count()) + " \tLowest: " + str(pt.getlowest()))
        pt.checklocation(convert(humiditytolocation, convert(temperaturetohumidity, convert(lighttotemperature,
                                                                                            convert(watertolight,
                                                                                                    convert(
                                                                                                        fertilizertowater,
                                                                                                        convert(
                                                                                                            soiltofertilizer,
                                                                                                            convert(
                                                                                                                seedtosoil,
                                                                                                                seed))))))))
        pt.subremaining()
    pt.stoptracking()


def comparerange(i, j, k):
    rangelist = []
    print("i: " + str(i) + " j: " + str(j) + " k: " + str(k))
    if k == 6:
        x = convert(rangemaps[k], i), convert(rangemaps[k], j)
        print(x)
        return x
    else:
        for r in rangemaps[k]:
            if r[1] < i < j < r[1] + r[2]:
                print("r:" + str(r[1]) + " - " + str(r[1] + r[2]))
                x = comparerange(convert(rangemaps[k], i), convert(rangemaps[k], j), k + 1)
                if isinstance(x, tuple):
                    rangelist.append(x)
                else:
                    rangelist.extend(x)
            if r[1] < i < r[1] + r[2] < j:
                print("r:" + str(r[1]) + " - " + str(r[1] + r[2]))
                x = comparerange(convert(rangemaps[k], i), convert(rangemaps[k], r[1] + r[2]), k + 1)
                if isinstance(x, tuple):
                    rangelist.append(x)
                else:
                    rangelist.extend(x)
            if i < r[1] < j < r[1] + r[2]:
                print("r:" + str(r[1]) + " - " + str(r[1] + r[2]))
                x = comparerange(convert(rangemaps[k], r[1]), convert(rangemaps[k], j), k + 1)
                if isinstance(x, tuple):
                    rangelist.append(x)
                else:
                    rangelist.extend(x)
        x = comparerange(convert(rangemaps[k], i), convert(rangemaps[k], j), k + 1)
        if isinstance(x, tuple):
            rangelist.append(x)
        else:
            rangelist.extend(x)
    return rangelist


def run():
    threadsperrange = tcount * (2 ** tcount)
    if threadsperrange * tcount > 102400:
        threadsperrange = int(102400 / tcount)
    for i in range(tcount):
        div = int((rangepairs[i][1] - rangepairs[i][0]) / threadsperrange)
        for j in range(threadsperrange):
            thread_args = (rangepairs[i][0] + j * div, rangepairs[i][0] + (j + 1) * div)
            thread = threading.Thread(target=scanrange, args=thread_args)
            threads.append(thread)

    for t in threads:
        t.start()

def run2():
    for i in range(tcount):
        print("range: " + str(rangepairs[i][0]) + " - " + str(rangepairs[i][1]))
        x = comparerange(rangepairs[i][0], rangepairs[i][1], 0)
        print()
        for y in x:
            pt.checklocation(y[0])
            pt.checklocation(y[1])

tcount = initialize()
for i in range(len(seedranges)):
    if i % 2 == 0:
        seedc = seedranges[i + 1]
        seedcount += int(seedc)
seedsremaining = seedcount
seedstr = str(seedcount)
pt = ProgressTracker(seedcount)
print()
printmap(seedtosoil)
print()
printmap(soiltofertilizer)
print()
printmap(fertilizertowater)
print()
printmap(watertolight)
print()
printmap(lighttotemperature)
print()
printmap(temperaturetohumidity)
print()
printmap(humiditytolocation)
print()
# retard mode
# run()

# for people who are smarter than me mode
run2()

print("Done! Lowest location: " + str(pt.getlowest()))
