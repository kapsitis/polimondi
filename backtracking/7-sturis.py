import math

N = 7


class PointTg:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    # Ar šo funkciju var pieskaitīt pašreizējam punktam izmaiņu "delta" (jauno malu)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return PointTg(x, y, z)

    # Atgriež trijstūru režģī novilktas malas garumu (ja paralēla režģa līnijām)
    # Vai nu arī - īsāko ceļu no PointTg virsotnes līdz sākumpunktam (ejot pa trijstūrīšu līnijām)
    def abs(self):
        return int(max(abs(self.x), abs(self.y), abs(self.z)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __ne__(self, other):
        return not self.__eq__(other)


def pointset(a, b, n, myset):
    oldsize = len(myset)
    # Pievienojam jaunos punktus
    end = list(a)
    b = list(b)
    for x in range(1, n + 1):
        end = list(end)
        end[0] += b[0]
        end[1] += b[1]
        end[2] += b[2]
        end = tuple(end)
        myset = (myset) + (end,)
    newsize = len(set(myset))
    if list(end) == [0, 0, 0]:
        newsize += 1
    if newsize - oldsize != n:
        return False
    else:
        return myset


def galv(list1, m, t, mysett):
    if (list1[-1][0] == 0 and (list1[-1][1] == 1 or list1[-1][1] == -1)) or ((list1[-1][0] == 1 or list1[-1][0] == -1) and list1[-1][0] == 0):
        return False
    lis = [list1[0], list1[1], list1[2],
           list1[3], list1[4], list1[5], list1[6]]
    d = int(((m - 1) * m) / 2)
    p0 = PointTg(0, 0, 0)

    dlist = []
    ddlist = []
    dddlist = []
    for ll in lis:
        LL0 = int(round(ll[0]))
        LL1 = int(round(ll[1]))
        if ll[1] == 0.5:
            LL1 = 1
        if ll[1] == -0.5:
            LL1 = -1
        if LL0 == 0:
            dlist.append(PointTg(LL1, 0, -LL1))
            if len(ddlist) == 0:
                ddlist.append((LL1, 0, -LL1))
                dddlist.append([LL1, 0, -LL1])
            else:
                if LL1 != 0:
                    j = ddlist[-1]
                    j0 = j[0] + LL1
                    j2 = j[2] - LL1
                    ddlist.append((j0, j[1], j2))
                    dddlist.append([j0, j[1], j2])
        elif LL0 * LL1 > 0:
            dlist.append(PointTg(LL0, -LL0, 0))
            if len(ddlist) == 0:
                ddlist.append((LL0, -LL0, 0))
                dddlist.append([LL0, -LL0, 0])
            else:
                if LL1 != 0:
                    j = ddlist[-1]
                    j0 = j[0] + LL0
                    j1 = j[1] - LL0
                    ddlist.append((j0, j1, j[2]))
                    dddlist.append([j0, j1, j[2]])
        elif LL0 * LL1 < 0:
            dlist.append(PointTg(0, -LL0, LL0))
            if len(ddlist) == 0:
                ddlist.append((0, -LL0, LL0))
                dddlist.append([0, -LL0, LL0])
            else:
                if LL1 != 0:
                    j = ddlist[-1]
                    j1 = j[1] - LL0
                    j2 = j[2] + LL0
                    ddlist.append((j[0], j1, j2))
                    dddlist.append([j[0], j1, j2])

    p = p0
    for delta in dlist:
        p += delta
    myset = mysett
    if (p.abs()) <= d:
        a = ddlist[t - 1]
        aa = ddlist[t]
        n = m
        if a[0] == aa[0]:
            if int(aa[1]) == int(a[1] + n):
                g = (0, 1, -1)
            elif int(aa[1]) == int(int(a[1]) - n):
                g = (0, -1, 1)
        elif a[1] == aa[1]:
            if int(aa[0]) == int(a[0] + n):
                g = (1, 0, -1)
            elif int(aa[0]) == int(a[0] - n):
                g = (-1, 0, 1)
        elif a[2] == aa[2]:
            if int(aa[0]) == int(a[0] + n):
                g = (1, -1, 0)
            elif int(aa[0]) == int(a[0] - n):
                g = (-1, 1, 0)
        mai = pointset(a, g, m, myset)
        if mai != False:
            mysett = mai
            return mysett
        else:
            return False
    else:
        return False


def maina(lis2d):
    dlist = []
    for ll in lis2d:
        LL0 = int(round(ll[0]))
        LL1 = int(round(ll[1]))
        if LL0 == 0:
            dlist.append(PointTg(LL1, 0, -LL1))
        elif LL0 * LL1 > 0:
            dlist.append(PointTg(LL0, -LL0, 0))
        elif LL0 * LL1 < 0:
            dlist.append(PointTg(0, -LL0, LL0))
    return dlist


mysett = ()
for i in range(N+1):
    mysett = list(mysett)
    mysett.append((i, 0, -i))
    mysett = tuple(mysett)


def doing(p, x1, mysets):
    global mysett, liss, N
    if x1 == 0:
        print("{},".format(liss))
        return False
    if x1 == N-1:
        if p[0] == 0 and p[1] > 0 or p[0] == 0 and p[1] < 0:
            li1 = [[x1, -x1 / 2], [x1, x1 / 2]]
    else:
        if p[0] == 0 and p[1] > 0 or p[0] == 0 and p[1] < 0:
            li1 = [[x1, -x1 / 2], [x1, x1 / 2], [-x1, -x1 / 2], [-x1, x1 / 2]]
        elif p[0] < 0 and p[1] > 0 or p[0] > 0 and p[1] < 0:
            li1 = [[0, -x1], [x1, x1 / 2], [0, x1], [-x1, -x1 / 2]]
        elif p[0] < 0 and p[1] < 0 or p[0] > 0 and p[1] > 0:
            li1 = [[0, -x1], [x1, -x1 / 2], [0, x1], [-x1, x1 / 2]]
    for y2 in li1:
        mysett = mysets
        p[0] = y2[0]
        p[1] = y2[1]
        liss[0] = [0, 7]
        liss[N-x1] = y2
        mi2 = galv(liss, x1, N-x1, mysett)
        if mi2 != False:
            if doing(p, x1-1, mi2) == False:
                mysett = set(list(mysett)[:-(x1-1)])
                for i in range(x1):
                    liss[-i][0] = 0
                    liss[-i][1] = 0
            else:
                return True
        mysett = mysets
        for i in range(x1):
            liss[-i][0] = 0
            liss[-i][1] = 0

    return False


liss = []
for i in range(N):
    liss.append([0, 0])
p = [0, N]
x111 = N-1
mysett = ()
for i in range(N+1):
    mysett = list(mysett)
    mysett.append((i, 0, -i))
    mysett = tuple(mysett)

doing(p, x111, mysett)
