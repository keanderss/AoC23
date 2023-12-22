import linecache

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
dik = dict(zip(keys, values))
node = "AAA"
i = 0
steps = 0
while node != "ZZZ":
    if i == len(instructions):
        i = 0
    nodes = dik[node]
    node = nodes[instructions[i]]
    i += 1
    steps += 1
print(f"steps: {steps}")

