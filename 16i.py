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


def calc_distances(start):  # from the start node, find best distances to all other nodes
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

for v in valves:  # this populates the list of interesting nodes to visit and the lookup table of all possible steps
    if int(v.flow) > 0:
        valves_to_visit.append(v.name)
    calc_distances(v.name)
    for t in valves:
        dist_dict[(v.name, t.name)] = (valve_by_name(t.name).distance, int(valve_by_name(t.name).flow))
# dictionary has format (start, destination) : (distance, destination flow)


def calc_comb(cc):  # this is to calculate the pressure release of a path. Expecting an iterable of node names
    s_start = "AA"  # always start any walk at AA
    t = 30  # 30 minutes for a walk
    release = 0  # initial pressure release is 0
    for s in range(len(cc)):  # for each step in walk
        s_destination = cc[s]  # destination is next step
        s_distance = dist_dict[(s_start, s_destination)][0]
        t -= (s_distance + 1)
        if t < 0:
            return release
        release += int(dist_dict[(s_start, s_destination)][1]) * t
        s_start = s_destination
    return release


all_paths = [] #  format is [([path], time remaining)]

# populate initial first steps:
calc_distances("AA")
for v in valves_to_visit:
    all_paths.append([[v], 30-dist_dict[("AA", v)][0]-1])


def refine_path():
    for p in all_paths:
        if p[1] != -1:
            # path to refine
            # print("refining", p)
            c_path = p[0]
            c_time = p[1]
            # add next visits or mark -1 to say path ended (out of time or no more to visit)
            vta = []  # visits to add
            for v in valves_to_visit:
                if v not in p[0] and (p[1] - dist_dict[(p[0][-1], v)][0]-1) > 0:
                    temp_path = c_path.copy()
                    temp_path.append(v)
                    vta.append([temp_path, p[1] - dist_dict[(p[0][-1], v)][0]-1])
            if len(vta) == 0:
                # no valves to add. Dont add new nodes, but mark as -1
                p[1] = -1
            else:
                # remove old path to replace with new ones
                all_paths.remove(p)
                for v in vta:
                    all_paths.append(v)

            return 0  # after refining this path
    print("No more refinement")
    return 1


refining = 0
j = 0
while refining == 0:
    if j % 10000 == 0:
        print(j,"possible paths found")
    refining = refine_path()
    j += 1

print("found", len(all_paths), "to test through")

best = 0
bestwalk = []
for p in all_paths:
    if calc_comb(p[0]) > best:
        best = calc_comb(p[0])
        bestwalk = p[0]

print(best)
print(bestwalk)


