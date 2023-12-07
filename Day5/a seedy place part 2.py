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
def run():
    for i in range(len(seedranges)):
        if i % 2 == 0:
            seedi = seedranges[i]
            print("seedi: " + seedi)
            seedinti = int(seedi)
            seedp1 = seedranges[i + 1]
            print("seedp1: " + seedp1)
            seedintp1 = int(seedp1)
            pair = (seedinti, seedinti + seedintp1)
            rangepairs.append(pair)
            print(rangepairs)





def scanrange(start, stop):
    print("hi")
    for s in range(start, stop):
        getseedlocation(s)

run()

t1 = threading.Thread(target=scanrange, args=(rangepairs[0][0], rangepairs[0][0] + rangepairs[0][1]))
t2 = threading.Thread(target=scanrange, args=(rangepairs[1][0], rangepairs[1][0] + rangepairs[1][1]))
t3 = threading.Thread(target=scanrange, args=(rangepairs[2][0], rangepairs[2][0] + rangepairs[2][1]))
t4 = threading.Thread(target=scanrange, args=(rangepairs[3][0], rangepairs[3][0] + rangepairs[3][1]))
t5 = threading.Thread(target=scanrange, args=(rangepairs[4][0], rangepairs[4][0] + rangepairs[4][1]))
t6 = threading.Thread(target=scanrange, args=(rangepairs[5][0], rangepairs[5][0] + rangepairs[5][1]))
t7 = threading.Thread(target=scanrange, args=(rangepairs[6][0], rangepairs[6][0] + rangepairs[6][1]))
t8 = threading.Thread(target=scanrange, args=(rangepairs[7][0], rangepairs[7][0] + rangepairs[7][1]))
t9 = threading.Thread(target=scanrange, args=(rangepairs[8][0], rangepairs[8][0] + rangepairs[8][1]))
t10 = threading.Thread(target=scanrange, args=(rangepairs[9][0], rangepairs[9][0] + rangepairs[9][1]))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

print("Lowest location: " + str(min(locations)))
