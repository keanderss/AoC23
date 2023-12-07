import linecache
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


def convert(m, i):
    for j in range(len(m)):
        if i in range(m[j][1], m[j][1] + m[j][2]):
            return i + (m[j][0] - m[j][1])
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
            mapcount += 1
        elif line.startswith("soil-to-fertilizer map:"):
            print("Creating soil to fertilizer map!")
            createmap(soiltofertilizer, i + 1)
            print(soiltofertilizer)
            mapcount += 1
        elif line.startswith("fertilizer-to-water map:"):
            print("Creating fertilizer to water map!")
            createmap(fertilizertowater, i + 1)
            print(fertilizertowater)
            mapcount += 1
        elif line.startswith("water-to-light map:"):
            print("Creating water to light map!")
            createmap(watertolight, i + 1)
            print(watertolight)
            mapcount += 1
        elif line.startswith("light-to-temperature map:"):
            print("Creating light to temperature map!")
            createmap(lighttotemperature, i + 1)
            print(lighttotemperature)
            mapcount += 1
        elif line.startswith("temperature-to-humidity map:"):
            print("Creating temperature to humidity map!")
            createmap(temperaturetohumidity, i + 1)
            print(temperaturetohumidity)
            mapcount += 1
        elif line.startswith("humidity-to-location map:"):
            print("Creating humidity to location map!")
            createmap(humiditytolocation, i + 1)
            print(humiditytolocation)
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

    def gettotal(self):
        return self.seedtotal

    def subremaining(self):
        self.remaining -= 1
        self.progress = int((1 - (self.remaining / self.seedtotal)) * 100)

    def getprogressstr(self):
        return str(self.remaining) + "/" + self.seedtotalstr + " (" + str(self.progress) + "%)"


def scanrange(start, stop):
    for seed in range(start, stop):
        print("Seeds left: " + pt.getprogressstr() + "\tChecking seed: " + str(
            seed) + "\tActive threads: " + str(threading.active_count()))
        locations.append(convert(humiditytolocation, convert(temperaturetohumidity, convert(lighttotemperature,
                                                                                            convert(watertolight,
                                                                                                    convert(
                                                                                                        fertilizertowater,
                                                                                                        convert(
                                                                                                            soiltofertilizer,
                                                                                                            convert(
                                                                                                                seedtosoil,
                                                                                                                seed))))))))
        pt.subremaining()
    print("locations: " + str(locations))
    if len(locations) > 0:
        print("Lowest location: " + str(min(locations)))
    print("Active threads: " + str(threading.active_count()) + "")


def run():
    for i in range(tcount):
        t = threading.Thread(target=scanrange, args=(rangepairs[i][0], rangepairs[i][1]))
        threads.append(t)

    for t in threads:
        t.start()


tcount = initialize()
for i in range(len(seedranges)):
    if i % 2 == 0:
        seedc = seedranges[i + 1]
        print("p1: " + str(seedc))
        seedcount += int(seedc)
seedsremaining = seedcount
seedstr = str(seedcount)
pt = ProgressTracker(seedcount)
print("seedcount: " + seedstr)
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
run()
