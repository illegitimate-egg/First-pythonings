acc = 0
pc = 0

mem = [
    555, 903, 556, 903, 557, 903, 558, 903,
    559, 903, 560, 903, 561, 903, 562, 903,
    563, 903, 000, 000, 000, 000, 000, 000,
    000, 000, 000, 000, 000, 000, 000, 000,
    000, 000, 000, 000, 000, 000, 000, 000,
    000, 000, 000, 000, 000, 000, 000, 000,
    000, 000, 000, 000, 000, 000, 000, 83,
    112, 97, 103, 104, 101, 116, 116, 105
]

def inp():
    global acc
    acc = input("> ")
    print("\n")

def out():
    global acc
    print(acc, end="")

def charout():
    global acc
    print(chr(acc), end="")

def lda(loc):
    global acc
    acc = mem[loc]

def sta(loc):
    global acc
    mem[loc] = a

def add(loc):
    global acc
    acc = acc + mem[loc]

def sub(loc):
    global acc
    acc = acc - mem[loc]

def brp(loc):
    global acc
    if (abs(acc) == acc):
        pc = loc

def brz(loc):
    global acc
    if (acc == 0):
        pc = loc

def bra(loc):
    global acc
    pc = loc

def halt():
    while(True):
        print("", end="")

instructions = [
    901, inp,
    902, out,
    903, charout,
    5  , lda,
    3  , sta,
    1  , add,
    2  , sub,
    8  , brp,
    7  , brz,
    6  , bra,
    0  , halt
]

while(True):
    instr = mem[pc]
    if (int(instr) == 0):
        halt()
        
    ini = int(str(instr)[0])
    data = int(str(instr)[1]+str(instr)[2])
    if ini == 5 or ini == 3 or ini == 1 or ini == 2 or ini == 8 or ini == 7 or ini == 6:
        instructions[instructions.index(ini)+1](data)
    else:
        instructions[instructions.index(instr)+1]()
    pc += 1
