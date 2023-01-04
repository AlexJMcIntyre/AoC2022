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

sensors = []
for sensor_raw in sensors_raw:
    sensor_parts = sensor_raw.strip().replace(":", ",").split(",")
    lx = int(sensor_parts[0][12:])
    ly = int(sensor_parts[1][3:])
    lbx = int(sensor_parts[2][24:])
    lby = int(sensor_parts[3][3:])
    sensors.append(Sensor(lx, ly, lbx, lby))

sc = []  # spaces to check
# for each sensor, work out spaces at range + 1
limit = 4000000

for s in sensors:
    xr = s.x + s.s_range + 1
    yr = s.y
    for r in range(s.s_range + 1):
        xr -= 1
        yr += 1
        if 0 <= xr <= limit and 0 <= yr <= limit:
            sc.append((xr, yr))
    for r in range(s.s_range + 1):
        xr -= 1
        yr -= 1
        if 0 <= xr <= limit and 0 <= yr <= limit:
            sc.append((xr, yr))
    for r in range(s.s_range + 1):
        xr += 1
        yr -= 1
        if 0 <= xr <= limit and 0 <= yr <= limit:
            sc.append((xr, yr))
    for r in range(s.s_range + 1):
        xr += 1
        yr += 1
        if 0 <= xr <= limit and 0 <= yr <= limit:
            sc.append((xr, yr))

sc = list(dict.fromkeys(sc))  # remove dupes
print(len(sc), "to check")

for space in sc:
    in_range = 0
    # for each space to check, see if it falls within range of a sensor
    for sensor in sensors:
        if abs(space[0]-sensor.x)+abs(space[1]-sensor.y)<=sensor.s_range:
            # in range, break
            in_range = 1
            break
    if in_range == 0:
        print("Winner at ", space[0], space[1])