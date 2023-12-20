import linecache
from collections import Counter

hands = []
c_values = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
h_values = {"[5]": 7, "[4, 1]": 6, "[3, 2]": 5, "[3, 1, 1]": 4, "[2, 2, 1]": 3, "[2, 1, 1, 1]": 2, "[1, 1, 1, 1, 1]": 1}
for line in linecache.getlines("input.txt"):
    split_line = line.split()
    hand = [c_values[split_line[0][i]] for i in range(5)]
    common = Counter(hand).most_common()
    if 1 in hand and len(common) > 1:
        Jhindex = 0
        for i in range(len(common)):
            if common[i][0] == 1:
                Jhindex = i
                break
        Windex = 0
        if common[Windex][1] == 1:
            biggest = 0
            for w in range(len(common)):
                if common[w][0] > biggest:
                    biggest = common[w][0]
                    Windex = w
        if Windex == Jhindex:
            Windex = Windex + 1
        common[Windex] = common[Windex][0], common[Windex][1] + common[Jhindex][1]
        if Windex != 0:
            common.insert(0, common.pop(Windex))
            if Windex > Jhindex:
                Jhindex += 1
        common.remove(common[Jhindex])
    strength = h_values[str([common[j][1] for j in range(len(common))])]
    hands.extend([[strength, hand, int(split_line[1])]])
hands.sort()
winnings = 0
for i in range(len(hands)):
    print(f"{i + 1}:  \t{hands[i]}")
    winnings += (i+1)*hands[i][2]
print(winnings)
