class Monkey:
    def __init__(self, items, oper, test, ttrue, tfalse):
        self.items = items
        self.oper = oper
        self.test = test
        self.ttrue = ttrue
        self.tfalse = tfalse
        self.insp = 0

    def inspect(self):
        for x, i in enumerate(self.items):
            # print("item " + str(x))
            t = self.oper.split()
            tr = []
            for ts in t:
                tr.append(ts.replace("old", str(i)))
            if tr[1] == "*":
                i = int(tr[0]) * int(tr[2])
            elif tr[1] == "/":
                i = int(tr[0]) / int(tr[2])
            elif tr[1] == "+":
                i = int(tr[0]) + int(tr[2])
            elif tr[1] == "-":
                i = int(tr[0]) - int(tr[2])
            else:
                print("unexpected operator")
                # other operations here

            # i = (i/3)
            # manage worry here!
            i = i % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)

            if i % self.test == 0:
                monkeys[self.ttrue].items.append(i)
            else:
                monkeys[self.tfalse].items.append(i)
            self.items[x] = -1  # mark for removal
            self.insp += 1
        self.items[:] = [value for value in self.items if value != -1]


monkeys = []
monkeys.append(Monkey([89, 95, 92, 64, 87, 68], "old * 11", 2, 7, 4))  # 0
monkeys.append(Monkey([87, 67], "old + 1", 13, 3, 6))  # 1
monkeys.append(Monkey([95, 79, 92, 82, 60], "old + 6", 3, 1, 6))  # 2
monkeys.append(Monkey([67, 97, 56], "old * old", 17, 7, 0))  # 3
monkeys.append(Monkey([80, 68, 87, 94, 61, 59, 50, 68], "old * 7", 19, 5, 2))  # 4
monkeys.append(Monkey([73, 51, 76, 59], "old + 8", 7, 2, 1))  # 5
monkeys.append(Monkey([92], "old + 5", 11, 3, 0))  # 6
monkeys.append(Monkey([99, 76, 78, 76, 79, 90, 89], "old + 7", 5, 4, 5))  # 6

for r in range(10000):  # each round
    # print("round " + str(r))
    for m in monkeys:  # each monkey
        #  print("monkey " + str(m))
        m.inspect()

for m in monkeys:
    print(m.insp)
