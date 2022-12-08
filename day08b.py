file = open("day08.txt")
lines = file.read().splitlines()

w=len(lines[0])

yy = 3
xx = 2

m = [[0 for x in range(0,w)] for y in range(0,w)]

for xx in range(1,w-1):
    for yy in range(1,w-1):

        mh = int(lines[yy][xx])
        d = [0,0,0,0]

        for x in range(xx+1,w):
            h = int(lines[yy][x])
            if h >= mh:
                break
        d[2]=x-xx

        for x in range(xx-1,-1,-1):
            h = int(lines[yy][x])
            if h >= mh:
                break
        d[1]=xx-x

        for y in range(yy+1,w):
            h = int(lines[y][xx])
            if h >= mh:
                break
        d[3]=y-yy

        for y in range(yy-1,-1,-1):
            h = int(lines[y][xx])
            if h >= mh:
                break
        d[0]=yy-y

        sc = d[0] * d[1] * d[2]* d[3]

        m[yy][xx] = sc


q = - 1
for r in m:
    print(r)
    qq = max(r)
    if qq>q:
        q = qq

print("Svar:",q)
exit()

