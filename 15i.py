file = open("15.txt")
sensors_raw = file.readlines()


class Sensor:
    def __init__(self, x, y, bx, by):
        self.x = x
        self.y = y
        self.bx = bx
        self.by = by
        self.s_range = abs(x-bx)+abs(y-by)

    def __str__(self):
        return "sensor at " + str(self.x) + ", " + str(self.y) + "; range " + str(self.s_range)

    # def __repr__(self):
    #     return self.x, self.y, self.s_range


sensors = []
for sensor_raw in sensors_raw:
    sensor_parts = sensor_raw.strip().replace(":", ",").split(",")
    lx = int(sensor_parts[0][12:])
    ly = int(sensor_parts[1][3:])
    lbx = int(sensor_parts[2][24:])
    lby = int(sensor_parts[3][3:])
    sensors.append(Sensor(lx, ly, lbx, lby))

ty = 2000000
tlist = []  # spaces on target row where an unknown beacon cannot
blist = []  # known beacons to remove from answer
for s in sensors:
    #  s.x centre of range on target row
    x_range = s.s_range - abs(s.y - ty) # slack on x-axis for target row
    if x_range < 0:
        # print(s, "does not feature on target row")
        pass
    else:
        # print(s, "looking at range", s.x-x_range, "to", s.x+x_range+1)
        for r in range(s.x-x_range, s.x+x_range+1):
            # print(r)
            tlist.append(r)
    # while we're here, account for beacons on this row:
    if s.by == ty:
        blist.append(s.bx)


tlist = list(dict.fromkeys(tlist))  # remove dupes
blist = list(dict.fromkeys(blist))

print(len(tlist) - len(blist))

