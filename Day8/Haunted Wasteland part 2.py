import linecache
import time
import sympy

stime = time.time()
instructions = []
keys = []
values = []
ins_conv = {"L": 0, "R": 1}
for line in linecache.getlines("input.txt"):
    split_line = line.split()
    if len(split_line) > 1:
        keys.append(split_line[0])
        values.append((split_line[2].strip("(").rstrip(","), split_line[3].rstrip(")")))
    elif len(split_line) == 1:
        instructions = [ins_conv[i] for i in list(split_line[0])]
dic = dict(zip(keys, values))
source = [dic[k] for k in keys if k[2] == "A"]


def calcsteps(node):
    i = 0
    steps = 0
    k = node[instructions[i]]
    while k[2] != "Z":
        if i == len(instructions):
            i = 0
        k = node[instructions[i]]
        node = dic[k]
        i += 1
        steps += 1
    return steps


step_list = [calcsteps(node) for node in source]
dont_smash_it = []
prime = 2
while not all(number == 1 for number in step_list):
    if any(number % prime == 0 for number in step_list):
        for index, number in enumerate(step_list):
            if number % prime == 0:
                step_list[index] = number / prime
        dont_smash_it.append(prime)
    else:
        prime = sympy.nextprime(prime)
steps = 1
for prime in dont_smash_it:
    steps *= prime
print(f"steps: {steps}\ttime: {"{:.3f}".format(time.time() - stime)}s")
