# import sys

file = open("12.txt")
map_raw = file.readlines()
start = [0, 0]
destination = [0, 0]
next_id = 0

map_height = len(map_raw)
map_width = len(map_raw[0].strip())


# sys.setrecursionlimit(1000000) #eep

class MapSquare:

    def __init__(self, elev, fx, fy):
        global start, destination, next_id
        self.id = next_id
        next_id += 1
        self.elev = elev
        if self.elev == "S":
            self.elev = "a"
            start = [fx, fy]
        if self.elev == "E":
            self.elev = "z"
            destination = [fx, fy]
        #        self.up_valid = 0
        #        self.down_valid = 0
        #        self.left_valid = 0
        #        self.right_valid = 0
        self.neighbours = []
        self.visited = 0
        self.x = fx
        self.y = fy
        self.distance = 10000000

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id

    def check_moves(self):
        #  check up
        if self.y != 0 and ord(get_by_xy(self.x, self.y - 1).elev) <= ord(self.elev) + 1:
            self.neighbours.append(get_by_xy(self.x, self.y - 1).id)
        #  check down
        if self.y != map_height - 1 and ord(get_by_xy(self.x, self.y + 1).elev) <= ord(self.elev) + 1:
            self.neighbours.append(get_by_xy(self.x, self.y + 1).id)
        # check left
        if self.x != 0 and ord(get_by_xy(self.x - 1, self.y).elev) <= ord(self.elev) + 1:
            self.neighbours.append(get_by_xy(self.x - 1, self.y).id)
        # check right
        if self.x != map_width - 1 and ord(get_by_xy(self.x + 1, self.y).elev) <= ord(self.elev) + 1:
            self.neighbours.append(get_by_xy(self.x + 1, self.y).id)


def get_by_xy(fx, fy):
    for s in map:
        if s.x == fx and s.y == fy:
            return s
    print("Not found")


def get_by_id(fid):
    for s in map:
        if s.id == fid:
            return s


def draw_distance():
    for y in range(map_height):
        l = []
        for x in range(map_width):
            l.append(get_by_xy(x, y).distance)
        print(l)
    print(" ")


# load map from file:
print("loading map")
map = []
for y, line_raw in enumerate(map_raw):
    line = line_raw.strip()
    for x, square in enumerate(line):
        map.append(MapSquare(square, x, y))

print(str(map_width * map_height) + " total squares")
#print(start, destination)

# calculate valid moves
for l in map:
    #print(l.id)
    l.check_moves()



c = get_by_xy(*start)
c.distance = 0
v = 0
while get_by_xy(*destination).visited == 0:
    #print("now looking at " + str(c.id))
    for n in c.neighbours:
        nm = get_by_id(n)
        if nm.visited == 0:
            nm.distance = min(nm.distance, c.distance + 1)
    c.visited = 1
    v += 1
    nextbestdistance = 1000000
    for m in map:
        #print("checking" + str(m.id) + " visited:" + str(m.visited) + ", distance = " + str(m.distance))
        if m.visited == 0 and m.distance < nextbestdistance:
            next = m.id
            nextbestdistance = m.distance
            #print("allocating next as " + str(next))
    c = get_by_id(next)
    #print("moving on to " + str(c.id))

print(get_by_xy(*destination).distance)
