import linecache
import sys
import threading
import multiprocessing as mp
import time
import os


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

    def subremaining(self, rr):
        self.remaining -= rr
        if self.remaining < 0:
            self.remaining = 0
        self.progress = int((1 - (self.remaining / self.seedtotal)) * 100)

    def getprogress(self):
        return str(self.progress)

    def getlowest(self):
        return self.lowestlocation

    def checklocation(self, location):
        if location < self.lowestlocation:
            self.lowestlocation = location

    def trackthread(self):
        self.threadcount += 1

    def getresult(self):
        print("Lowest location: " + str(self.getlowest()))

    def setseedcount(self, seedcount):
        self.seedtotal = seedcount
        self.seedtotalstr = str(seedcount)
        self.remaining = seedcount


def initialize():
    i = 0
    mapcount = 0
    while True:
        i += 1
        line = linecache.getline(filename, i)
        if line.startswith("seeds:"):
            linearrway = line.split()
            for j in linearrway:
                if j.isnumeric():
                    seedranges.append(j)
        elif line.startswith("seed-to-soil map:"):
            createmap(seedtosoil, i + 1)
            rangemaps.append(seedtosoil)
            mapcount += 1
        elif line.startswith("soil-to-fertilizer map:"):
            createmap(soiltofertilizer, i + 1)
            rangemaps.append(soiltofertilizer)
            mapcount += 1
        elif line.startswith("fertilizer-to-water map:"):
            createmap(fertilizertowater, i + 1)
            rangemaps.append(fertilizertowater)
            mapcount += 1
        elif line.startswith("water-to-light map:"):
            createmap(watertolight, i + 1)
            rangemaps.append(watertolight)
            mapcount += 1
        elif line.startswith("light-to-temperature map:"):
            createmap(lighttotemperature, i + 1)
            rangemaps.append(lighttotemperature)
            mapcount += 1
        elif line.startswith("temperature-to-humidity map:"):
            createmap(temperaturetohumidity, i + 1)
            rangemaps.append(temperaturetohumidity)
            mapcount += 1
        elif line.startswith("humidity-to-location map:"):
            createmap(humiditytolocation, i + 1)
            rangemaps.append(humiditytolocation)
            mapcount += 1
        else:
            if mapcount == 7:
                for k in range(len(seedranges)):
                    if k % 2 == 0:
                        seedk = seedranges[k]
                        seedintk = int(seedk)
                        seedp1 = seedranges[k + 1]
                        seedintp1 = int(seedp1)
                        pair = (seedintk, seedintk + seedintp1)
                        rangepairs.append(pair)
                return len(rangepairs)
            if i > 999:
                print("Initialization error!")
                break


def createmap(m, i):
    while True:
        line = linecache.getline(filename, i)
        linearray = line.split()
        if len(linearray) == 0:
            break
        m.append([int(numeric_string) for numeric_string in linearray])
        i += 1
    return m


def convert(m, i):
    for j in m:
        if j[1] <= i <= j[1] + j[2]:
            return i + (j[0] - j[1])
    return i


def comparerange(i, j, k):
    rangelist = []
    if k == 6:
        x = convert(rangemaps[k], i), convert(rangemaps[k], j)
        return x
    else:
        for r in rangemaps[k]:
            if r[1] < i < j < r[1] + r[2]:
                x = comparerange(convert(rangemaps[k], i), convert(rangemaps[k], j), k + 1)
                if isinstance(x, tuple):
                    rangelist.append(x)
                else:
                    rangelist.extend(x)
            if r[1] < i < r[1] + r[2] < j:
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


def scanrange(start, stop):
    time0 = time.time()
    if stop - start > 0:
        for seed in range(start, stop):
            progresstracker.checklocation(
                convert(humiditytolocation, convert(temperaturetohumidity, convert(lighttotemperature,
                                                                                   convert(watertolight,
                                                                                           convert(
                                                                                               fertilizertowater,
                                                                                               convert(
                                                                                                   soiltofertilizer,
                                                                                                   convert(
                                                                                                       seedtosoil,
                                                                                                       seed))))))))
    else:
        seed = start
        progresstracker.checklocation(
            convert(humiditytolocation, convert(temperaturetohumidity, convert(lighttotemperature,
                                                                               convert(watertolight,
                                                                                       convert(
                                                                                           fertilizertowater,
                                                                                           convert(
                                                                                               soiltofertilizer,
                                                                                               convert(
                                                                                                   seedtosoil,
                                                                                                   seed))))))))
    time1 = time.time()
    time2 = "{:.2f}".format(time1 - time0)
    progresstracker.subremaining(stop - start + 1)
    print("PID: " + str(os.getpid()) + " \tThreads: " + str(threading.active_count()) + " \tCompleted: " + str(
        progresstracker.getprogress()) + "% \tTime: " + str(time2) + " s \tLowest: " + str(progresstracker.getlowest()))


def run():
    for i in range(rangecount):
        x = comparerange(rangepairs[i][0], rangepairs[i][1], 0)
        for y in x:
            progresstracker.checklocation(y[0])
            progresstracker.checklocation(y[1])
    progresstracker.getresult()


def run2(start, stop):
    progresstracker.setseedcount(stop - start)
    threadsperrange = rangecount ** rangecount
    if threadsperrange * rangecount > 102400:
        threadsperrange = int(102400 / rangecount)
    div = int((stop - start) / threadsperrange)
    for j in range(threadsperrange):
        thread_args = (start + j * div, start + (j + 1) * div - 1)
        thread = threading.Thread(target=scanrange, args=thread_args)
        threads.append(thread)

    if (stop - start + threadsperrange * div) > 0:
        thread_args = (start + threadsperrange * div, stop)
        t2 = threading.Thread(target=scanrange, args=thread_args)
        threads.append(t2)

    for t in threads:
        t.start()


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
rangecount = initialize()
seedsremaining = seedcount
seedstr = str(seedcount)
for i in range(len(seedranges)):
    if i % 2 == 0:
        seedc = seedranges[i + 1]
        seedcount += int(seedc)
progresstracker = ProgressTracker(seedcount)

if __name__ == "__main__":
    print("1: actual solution")
    print("2: brute force")
    var = ""
    while var != ("1" or "2"):
        var = input()
        if var == "1":
            run()
        elif var == "2":
            processes = []
            for r in rangepairs:
                p = mp.Process(target=run2, args=r)
                processes.append(p)
            mp.parent_process()
            for p in processes:
                p.start()
