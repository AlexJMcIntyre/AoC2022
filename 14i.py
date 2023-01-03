file = open("14.txt")
paths_raw = file.readlines()


def print_cave():
    for cave_row_p in cave:
        print(cave_row_p)


# populate list of rock structure paths
paths = []
for path_raw in paths_raw:
    paths.append(path_raw.strip().split(" -> "))

x_max = 500
x_min = 500
y_max = 0
y_min = 0

# get dimensions
for path in paths:
    for node in path:
        node_split = node.split(",")
        if int(node_split[0]) > x_max:
            x_max = int(node_split[0])
        if int(node_split[0]) < x_min:
            x_min = int(node_split[0])
        if int(node_split[1]) > y_max:
            y_max = int(node_split[1])
        if int(node_split[1]) < y_min:
            y_min = int(node_split[1])

# pad x
x_min -= 1
x_max += 1

# pad y
y_max += 1

# create blank environment, note cave uses [y][x]!
cave = []
for y in range(y_min-1, y_max):
    cave_row = []
    for x in range(x_min-1, x_max):
        cave_row.append(".")
    cave.append(cave_row)

so = (500, 0)
cave[so[1]-y_min][so[0]-x_min] = "+"

# add rock structure paths
for path in paths:
    node_list = []
    for nodes in path:  # store as list of (x,y) coordinates
        node_list.append(nodes.split(","))
    for n in range(1, len(node_list)):
        # print(n, node_list[n-1], " > ", node_list[n])
        if node_list[n-1][0] == node_list[n][0]:
            # this is a structure along the y-axis, constant x
            x = int(node_list[n][0])
            rock_min_y = int(min(node_list[n - 1][1], node_list[n][1]))
            rock_max_y = int(max(node_list[n - 1][1], node_list[n][1]))
            for y in range(rock_min_y, rock_max_y+1):
                cave[y-y_min][x-x_min] = '#'
        else:
            # this is a structure along the x-axis, constant y
            y = int(node_list[n][1])
            rock_min_x = int(min(node_list[n - 1][0], node_list[n][0]))
            rock_max_x = int(max(node_list[n - 1][0], node_list[n][0]))
            for x in range(rock_min_x, rock_max_x+1):
                cave[y-y_min][x-x_min] = '#'


def drop_sand():
    sand = list(so)
    while True:
        if cave[sand[1]+1-y_min][sand[0]-x_min] == ".":  # move down?
            if sand[1]+1 == y_max:  # Abyss Check
                print("done!")
                return 1
            else:
                sand[1] += 1
        elif cave[sand[1]+1-y_min][sand[0]-1-x_min] == ".":  # move down and left?
            if sand[1]+1 == y_max:  # Abyss Check
                print("done!")
                return 1
            else:
                sand[1] += 1
                sand[0] -= 1
        elif cave[sand[1]+1-y_min][sand[0]+1-x_min] == ".":  # move down and right?
            if sand[1]+1 == y_max:  # Abyss Check
                print("done!")
                return 1
            else:
                sand[1] += 1
                sand[0] += 1
        else:  # sand has come to rest
            cave[sand[1]-y_min][sand[0]-x_min] = 'O'
            return 0


sand_count = 0
test = 0
while test == 0:
    sand_count += 1
    test = drop_sand()

print(sand_count-1)
print_cave()
