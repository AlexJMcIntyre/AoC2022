import itertools
import math
from itertools import combinations
file = open("16.txt")
valves_raw = file.readlines()


class Valve:
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels
        self.visited = False
        self.status = "Closed"
        self.distance = 1000000
        self.oppy = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

# populate valves from input:
valves = []
for valve_raw in valves_raw:
    valve_raw = valve_raw.replace("valves", "valve")
    valve_parts = valve_raw.strip().split(";")
    l_name = valve_parts[0][6:8]
    l_flow = valve_parts[0][23:]
    l_tunnels = valve_parts[1][23:].split(", ")
    valves.append(Valve(l_name, l_flow, l_tunnels))


def valve_by_name(name):
    for vn in valves:
        if vn.name == name:
            return vn
    print("Valve", name, "not found")


def min_tent_dist():
    td = 10000000
    tv = 0
    for vm in valves:
        if vm.distance < td and vm.visited is False:
            tv = vm
            td = vm.distance
    return tv


def calc_distances(start):
    for vd in valves:
        vd.visited = False  # 1
        vd.distance = 1000000  # 2
    current = valve_by_name(start)
    valve_by_name(start).distance = 0
    while True:
        for t in current.tunnels:  # 3
            if valve_by_name(t).visited is False and valve_by_name(t).distance > current.distance + 1:
                valve_by_name(t).distance = current.distance+1
        current.visited = True
        next_test = min_tent_dist()
        if next_test == 0:
            return 1
        else:
            current = next_test


dist_dict = {}
valves_to_visit = []

for v in valves:
    if int(v.flow) > 0:
        valves_to_visit.append(v.name)
    calc_distances(v.name)
    for t in valves:
        dist_dict[(v.name, t.name)] = (valve_by_name(t.name).distance, int(valve_by_name(t.name).flow))
# dictionary has format (start, destination) : (distance, destination flow)




def calc_comb(cc):
    s_start = "AA"  # always start any walk at AA
    t = 30  # 30 minutes for a walk
    release = 0  # initial pressure release is 0
    for s in range(len(cc)):  # for each step in walk
        s_destination = cc[s]  # destination is next step
        s_distance = dist_dict[(s_start, s_destination)][0]
        #  print(start, ">", dest)
        t -= (s_distance + 1)
        if t < 0:
            return release
        release += int(dist_dict[(s_start, s_destination)][1]) * t
        s_start = s_destination
    return release


best_guess = 0

for i in range(15):
    print("trying walk length",i)
    comb = itertools.permutations(valves_to_visit, i)
    # comb has format (name 1, name 2 etc)
    for x, c in enumerate(comb):
        if x % 1000000 == 0:
            tot = math.factorial(15)/math.factorial(15-i)
            print("{0:.00%}".format(x/tot), best_guess)
        best_guess = max(best_guess, calc_comb(c))

print(max(combos))


