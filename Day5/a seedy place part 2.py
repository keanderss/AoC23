import linecache
import sys
import threading
import multiprocessing as mp
import time
import os


class ProgressTracker:
    def __init__(self, seeds):
        self.seed_total = seeds
        self.seed_total_str = str(seeds)
        self.remaining = seeds
        self.progress = int((1 - (self.remaining / self.seed_total)) * 100)
        self.lowest_location = sys.maxsize

    def get_total(self):
        return self.seed_total

    def sub_remaining(self, rr):
        self.remaining -= rr
        if self.remaining < 0:
            self.remaining = 0
        self.progress = int((1 - (self.remaining / self.seed_total)) * 100)

    def get_progress(self):
        return str(self.progress)

    def get_lowest(self):
        return self.lowest_location

    def check_location(self, location):
        if location < self.lowest_location:
            self.lowest_location = location

    def get_result(self):
        print("Lowest location: " + str(self.get_lowest()))

    def set_seed_count(self, seed_count):
        self.seed_total = seed_count
        self.seed_total_str = str(seed_count)
        self.remaining = seed_count


def initialize():
    i = 0
    map_count = 0
    while True:
        i += 1
        line = linecache.getline(filename, i)
        if line.startswith("seeds:"):
            line_array = line.split()
            for j in line_array:
                if j.isnumeric():
                    seed_ranges.append(j)
        elif line.startswith("seed-to-soil map:"):
            create_map(seed_to_soil, i + 1)
            range_maps.append(seed_to_soil)
            map_count += 1
        elif line.startswith("soil-to-fertilizer map:"):
            create_map(soil_to_fertilizer, i + 1)
            range_maps.append(soil_to_fertilizer)
            map_count += 1
        elif line.startswith("fertilizer-to-water map:"):
            create_map(fertilizer_to_water, i + 1)
            range_maps.append(fertilizer_to_water)
            map_count += 1
        elif line.startswith("water-to-light map:"):
            create_map(water_to_light, i + 1)
            range_maps.append(water_to_light)
            map_count += 1
        elif line.startswith("light-to-temperature map:"):
            create_map(light_to_temperature, i + 1)
            range_maps.append(light_to_temperature)
            map_count += 1
        elif line.startswith("temperature-to-humidity map:"):
            create_map(temperature_to_humidity, i + 1)
            range_maps.append(temperature_to_humidity)
            map_count += 1
        elif line.startswith("humidity-to-location map:"):
            create_map(humidity_to_location, i + 1)
            range_maps.append(humidity_to_location)
            map_count += 1
        else:
            if map_count == 7:
                for k in range(len(seed_ranges)):
                    if k % 2 == 0:
                        seed_int_k = int(seed_ranges[k])
                        seed_int_p1 = int(seed_ranges[k + 1])
                        pair = (seed_int_k, seed_int_k + seed_int_p1)
                        range_pairs.append(pair)
                return len(range_pairs)
            if i > 999:
                print("Initialization error!")
                break


def create_map(m, i):
    while True:
        line = linecache.getline(filename, i)
        line_array = line.split()
        if len(line_array) == 0:
            break
        m.append([int(numeric_string) for numeric_string in line_array])
        i += 1
    return m


def convert(m, i):
    for j in m:
        if j[1] <= i <= j[1] + j[2]:
            return i + (j[0] - j[1])
    return i


def compare_range(i, j, k):
    rangelist = []
    if k == 6:
        x = convert(range_maps[k], i), convert(range_maps[k], j)
        return x
    else:
        for r in range_maps[k]:
            if r[1] < i < j < r[1] + r[2]:
                x = compare_range(convert(range_maps[k], i), convert(range_maps[k], j), k + 1)
                if isinstance(x, tuple):
                    rangelist.append(x)
                else:
                    rangelist.extend(x)
            if r[1] < i < r[1] + r[2] < j:
                x = compare_range(convert(range_maps[k], i), convert(range_maps[k], r[1] + r[2]), k + 1)
                if isinstance(x, tuple):
                    rangelist.append(x)
                else:
                    rangelist.extend(x)
            if i < r[1] < j < r[1] + r[2]:
                x = compare_range(convert(range_maps[k], r[1]), convert(range_maps[k], j), k + 1)
                if isinstance(x, tuple):
                    rangelist.append(x)
                else:
                    rangelist.extend(x)
        x = compare_range(convert(range_maps[k], i), convert(range_maps[k], j), k + 1)
        if isinstance(x, tuple):
            rangelist.append(x)
        else:
            rangelist.extend(x)
    return rangelist


def scan_range(start, stop, t0):
    for seed in range(start, stop + 1):
        pt.check_location(
            convert(humidity_to_location,
                    convert(temperature_to_humidity,
                            convert(light_to_temperature,
                                    convert(water_to_light,
                                            convert(fertilizer_to_water,
                                                    convert(soil_to_fertilizer,
                                                            convert(seed_to_soil, seed))))))))
    pt.sub_remaining(stop - start + 1)
    print(f"PID: {os.getpid()} \tThreads: {threading.active_count()} \tCompleted: {pt.get_progress()}% \tTime: {"{:.3f}".format(time.time() - t0)}s \tLowest: {pt.get_lowest()}")


def run():
    for i in range(range_count):
        x = compare_range(range_pairs[i][0], range_pairs[i][1], 0)
        for y in x:
            pt.check_location(y[0])
            pt.check_location(y[1])
    pt.get_result()


def run2(start, stop, t0):
    seeds = stop - start
    pt.set_seed_count(seeds)
    threads_per_range = 1000
    if threads_per_range > seeds:
        threads_per_range = seeds
    div = seeds // threads_per_range
    for j in range(threads_per_range):
        threads.append(threading.Thread(target=scan_range, args=(start + j * div, start + (j + 1) * div - 1, t0)))
    if (seeds % threads_per_range) > 0:
        threads.append(threading.Thread(target=scan_range, args=(start + threads_per_range * div, stop, t0)))
    for t in threads:
        t.start()


filename = "input.txt"
seed_ranges = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
locations = []
range_pairs = []
threads = []
seed_count = 0
range_maps = []
range_count = initialize()
seeds_remaining = seed_count
seed_str = str(seed_count)
for i in range(len(seed_ranges)):
    if i % 2 == 0:
        seed_count += int(seed_ranges[i + 1])
pt = ProgressTracker(seed_count)
if __name__ == "__main__":
    print("1: actual solution")
    print("2: brute force")
    var = ""
    while var != "1" or "2":
        var = input()
        if var == "1":
            t0 = time.time()
            run()
            t1 = time.time()
            print(f"Time to complete: {"{:.3f}".format(t1 - t0)} s")
            break
        elif var == "2":
            t0 = time.time()
            processes = []
            for r in range_pairs:
                processes.append(mp.Process(target=run2, args=(r[0], r[1], t0)))
            for p in processes:
                p.start()
            break
