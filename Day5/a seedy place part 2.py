import linecache
import threading

tcount = 10000
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


def convert(m, i):
    # print()
    # print("Starting conversion!")
    for j in range(len(m)):
        mapj0 = m[j][0]
        mapj0int = int(mapj0)
        mapj1 = m[j][1]
        mapj1int = int(mapj1)
        mapj2 = m[j][2]
        mapj2int = int(mapj2)
        # print("Searching for " + str(i) + " in " + str(range(mapj1int, mapj1int + mapj2int)))
        diff = mapj0int - mapj1int
        # print("j: " + str(j))
        # print("i: " + str(i))
        # print(mapj0 + " " + mapj1 + " " + mapj2)
        # print("diff: " + str(diff))
        idiff = i + diff
        # print("i + diff: " + str(idiff))
        if i in range(mapj1int, mapj1int + mapj2int):
            # print("Match for " + str(i) + " found in " + str(range(mapj1int, mapj1int + mapj2int)))
            return idiff
    # print("Returning default value: " + str(i))
    # print()
    return i


def getseedlocation(seed):
    soil = convert(seedtosoil, seed)
    fertilizer = convert(soiltofertilizer, soil)
    water = convert(fertilizertowater, fertilizer)
    light = convert(watertolight, water)
    temperature = convert(lighttotemperature, light)
    humidity = convert(temperaturetohumidity, temperature)
    location = convert(humiditytolocation, humidity)
    locations.append(location)
    print("Seed " + str(seed) + ", soil " + str(soil) + ", fertilizer " + str(fertilizer) + ", water " + str(
        water) + ", light " + str(light) + ", temperature " + str(temperature) + ", humidity " + str(
        humidity) + ", location " + str(location) + ".")


def createmap(map, i):
    while True:
        line = linecache.getline(filename, i)
        linearray = line.split()
        if len(linearray) == 0:
            break
        map.append(linearray)
        i += 1
    return map


def printmap(m):
    i = 0
    for y in m:
        print("y" + str(i) + ": \t" + str(y))
        i += 1


def initialize():
    print("Initializing!")
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
                break
            if i > 999:
                print("Initialization error!")
                break


initialize()
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
rangepairs = []
rangestarts = []
rangeends = []
def run():
    for i in range(len(seedranges)):
        if i % 2 == 0:
            seedi = seedranges[i]
            # print("seedi: " + seedi)
            seedinti = int(seedi)
            seedp1 = seedranges[i + 1]
            # print("seedp1: " + seedp1)
            seedintp1 = int(seedp1)
            pair = (seedinti, seedinti + seedintp1)
            rangestarts.append(seedinti)
            rangeends.append(seedinti + seedintp1)
            rangepairs.append(pair)
            # print(rangepairs)

def scanrange(start, stop):
    print("hi")
    for s in range(start, stop):
        getseedlocation(s)
run()

rangemin = min(rangestarts)
rangemax = max(rangeends)
fullrange = rangemax - rangemin
print(fullrange)

n = fullrange // tcount
print(n)

threads = []

for i in range(tcount):
    t = threading.Thread(target=scanrange, args=(i * n, (i + 1) * n))
    threads.append(t)

for t in threads:
    t.start()





print("Lowest location: " + str(min(locations)))
