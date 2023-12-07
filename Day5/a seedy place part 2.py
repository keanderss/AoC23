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
    for j in range(3):
        #mapj0 = m[j][0]
        #mapj0int = int(m[j][0])
        #mapj1 = m[j][1]
        mapj1int = int(m[j][1])
        #mapj2 = m[j][2]
        #mapj2int = int(m[j][2])
        # print("Searching for " + str(i) + " in " + str(range(mapj1int, mapj1int + mapj2int)))
        #diff = mapj0int - mapj1int
        # print("j: " + str(j))
        # print("i: " + str(i))
        # print(mapj0 + " " + mapj1 + " " + mapj2)
        # print("diff: " + str(diff))
        # idiff = i + (mapj0int - mapj1int)
        # print("i + diff: " + str(idiff))
        if i in range(mapj1int, mapj1int + int(m[j][2])):
            # print("Match for " + str(i) + " found in " + str(range(mapj1int, mapj1int + mapj2int)))
            return i + (int(m[j][0]) - mapj1int)
    # print("Returning default value: " + str(i))
    # print()
    return i


def getseedlocation(seed):
    locations.append(convert(humiditytolocation, convert(temperaturetohumidity, convert(lighttotemperature, convert(watertolight, convert(fertilizertowater, convert(soiltofertilizer, convert(seedtosoil, seed))))))))
    #print("Seed " + str(seed) + ", soil " + str(soil) + ", fertilizer " + str(fertilizer) + ", water " + str(
    #    water) + ", light " + str(light) + ", temperature " + str(temperature) + ", humidity " + str(
    #    humidity) + ", location " + str(location) + ".\n")


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
    # print(seedranges)
    for i in range(len(seedranges)):
        if i % 2 == 0:
            seedi = seedranges[i]
            #print("seedi: " + seedi)
            seedinti = int(seedi)
            seedp1 = seedranges[i + 1]
            #print("seedp1: " + seedp1)
            seedintp1 = int(seedp1)
            pair = (seedinti, seedinti + seedintp1)
            rangestarts.append(seedinti)
            rangeends.append(seedinti + seedintp1)
            rangepairs.append(pair)
            #print(rangepairs)

def scanrange(start, stop):
    for s in range(start, stop):
        #print("range: " + str(start) + " " + str(stop))
        getseedlocation(s)
run()

#rangemin = min(rangestarts)
#rangemax = max(rangeends)
#fullrange = rangemax - rangemin
#print(fullrange)

tcount = len(rangepairs)
print("tcount: " + str(tcount))

threads = []
for i in range(tcount):
    #print(i)
    #print(rangepairs)
    #print("inputrange: " + str(rangepairs[i][0]) + " " + str(rangepairs[i][1]))
    t = threading.Thread(target=scanrange, args=(rangepairs[i][0], rangepairs[i][1]))
    threads.append(t)

for t in threads:
    t.start()

trunning = len(threads)
while trunning > 0:
    trunning = len(threads)
    #print("Active threads: " + str(trunning) + "\n")
    for t in threads:
        if not t.is_alive():
            t.join()
            threads.remove(t)

print("locations: " + str(locations))
if len(locations) > 0:
    print("Lowest location: " + str(min(locations)))
