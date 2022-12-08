file = open("day08.txt")
lines = file.read().splitlines()

w=len(lines[0])

m = [[0 for x in range(0,w)] for y in range(0,w)]


if 1==1:
    for x in range(0,w):
        mx = -1
        for y in range(0,w):
            h = int(lines[y][x])
            if h > mx:
                m[y][x] = 1
                mx = h

if 1==1:
    for x in range(0,w):
        mx = -1
        for y in range(0,w):
            h = int(lines[w-y-1][x])
            if h > mx:
                m[w-y-1][x] = 1
                mx = h


if 1==1:
    for y in range(0,w):
        mx = -1
        for x in range(0,w):
            h = int(lines[y][w-x-1])
            if h > mx:
                m[y][w-x-1] = 1
                mx = h

if 1==1:
    for y in range(0,w):
        mx = -1
        for x in range(0,w):
            h = int(lines[y][x])
            if h > mx:
                m[y][x] = 1
                mx = h



tot = 0
for r in m:
    tot = tot+sum(r)
    print(r)

print("Svar:",tot)
exit()

