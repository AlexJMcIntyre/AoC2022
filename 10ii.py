file = open("10.txt")
codeList = file.readlines()

NextInstruction = 0
x = 1
c = 1

CyclesLeft = 0
dx = 0


def load_instruction(instr):
    global CyclesLeft, dx, NextInstruction
    s = codeList[instr].find(" ")
    if codeList[instr][:s] == "noop":
        CyclesLeft = 1
        dx = 0
    else:
        dx = int(codeList[instr][s:].strip())
        CyclesLeft = 2
    NextInstruction += 1


def get_sprite(x):
    sprite = ""
    for i in range(40):
        if abs(x - i) <= 1:
            sprite += "#"
        else:
            sprite += "."
    return sprite

load_instruction(NextInstruction)

sg = []
sl = ""

while NextInstruction < len(codeList):
    sprite = get_sprite(x)
    sl += sprite[(c % 40)-1]
    if (c % 40) == 0:
        sg.append(sl)
        sl = ""
    CyclesLeft -= 1
    if CyclesLeft == 0:
        x += dx
        load_instruction(NextInstruction)
    c += 1

sg.append(sl)
for l in sg:
    print(l)
