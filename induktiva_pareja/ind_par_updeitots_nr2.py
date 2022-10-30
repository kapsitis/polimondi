
# funkcija no dīvainajā Dekarta koordinātām listu pārveido uz listu, kur katrs saraksta saraksts
# tiek pārveidots par vienu burtu atkarībā no tā uz kuru virzienu iet mala.
import ast
from datetime import datetime

start_time = datetime.now()


def maina1(k):
    liss = []
    for a in k:
        a1 = a[0]
        a2 = a[1]
        if a1 == 0 and a2 > 0:
            liss.append("A")
        elif a1 == 0 and a2 < 0:
            liss.append("D")
        elif a1 > 0 and a2 > 0:
            liss.append("B")
        elif a1 > 0 and a2 < 0:
            liss.append("C")
        elif a1 < 0 and a2 > 0:
            liss.append("F")
        elif a1 < 0 and a2 < 0:
            liss.append("E")
    return liss


# funkcija no saraksta ar burtiem pārveido uz listu ar dīvainajām Dekarta koordinātām.
def maina2(k):
    liss = []
    p = len(k)
    for a in range(p):
        b = p-a
        if k[a] == "A":
            liss.append([0, b])
        elif k[a] == "D":
            liss.append([0, -b])
        elif k[a] == "B":
            liss.append([b, b/2])
        elif k[a] == "C":
            liss.append([b, -b/2])
        elif k[a] == "E":
            liss.append([-b, -b/2])
        elif k[a] == "F":
            liss.append([-b, b/2])
    return liss

# ģenerē sarakstu, ar visiem iespējamajiem sarakstiem, kur saraksta
# pirmajā vietā ir indekss, kurā vietā pievieno pirmo jauno malu
# un otrajā vietā ir indekss, kurā vietā pievieno otro jauno malu.


def gen():
    global N
    lis = []
    for a in range(1, N+1):
        for b in range(a+1, N+2):
            lis.append([a, b])
    return lis


# funkcija ģenerē setu ar visiem izstaigātajiem polimonda punktiem.
# funkcijai kā arguments tiek iedots saraksts, kurš sastāv no burtu virknes.
def point_gen(lis):
    global N
    mysett = {(0, 0, 0)}
    elem = (0, 0, 0)
    for x in range(N+2):
        e1 = elem[0]
        e2 = elem[1]
        e3 = elem[2]
        for y in range(N+3-x):
            if lis[x] == "A":
                e = (e1+y, e2+0, e3-y)
            if lis[x] == "B":
                e = (e1+y, e2-y, e3+0)
            if lis[x] == "C":
                e = (e1+0, e2-y, e3+y)
            if lis[x] == "D":
                e = (e1-y, e2+0, e3+y)
            if lis[x] == "E":
                e = (e1-y, e2+y, e3+0)
            if lis[x] == "F":
                e = (e1+0, e2+y, e3-y)
            mysett.add(e)
            # print(e)
            elem = list(e)
    return mysett


# pagaidām funkcija pārbauda tikai, vai polimonds beigās atgriežas sākuma koordinātās.
def checks(a, p, pp):
    # with open("output11_id.txt", "a") as f:
    #     print("{},".format(a), file=f)
    h = 0
    w = 0
    for k in a:
        h += k[0]
        w += k[1]
    if h == 0 and w == 0:
        point_count = point_gen(pp)
        if len(point_count) == ((N+2)*(N+3)/2):
            with open("output1717.txt", "a") as f:
                print("{},".format(a), file=f)
            # print("{},".format(a))
            # print("{},".format(maina2(p)))


def adding(a, i, k):
    if (k[a[i] - 1] == "A" or k[a[i] - 1] == "D") and (k[a[i]] == "E" or k[a[i]] == "B"):
        li = ["C", "F"]
    elif (k[a[i] - 1] == "A" or k[a[i] - 1] == "D") and (k[a[i]] == "F" or k[a[i]] == "C"):
        li = ["B", "E"]
    elif (k[a[i] - 1] == "B" or k[a[i] - 1] == "E") and (k[a[i]] == "F" or k[a[i]] == "C"):
        li = ["D", "A"]
    elif (k[a[i] - 1] == "B" or k[a[i] - 1] == "E") and (k[a[i]] == "A" or k[a[i]] == "D"):
        li = ["C", "F"]
    elif (k[a[i] - 1] == "C" or k[a[i] - 1] == "F") and (k[a[i]] == "A" or k[a[i]] == "D"):
        li = ["B", "E"]
    elif (k[a[i] - 1] == "C" or k[a[i] - 1] == "F") and (k[a[i]] == "E" or k[a[i]] == "B"):
        li = ["A", "D"]
    k1 = k.copy()
    k2 = k.copy()
    k1.insert(a[i], li[0])
    k2.insert(a[i], li[1])
    li2 = [k1, k2]
    return li2


def doing(kk):
    global komb
    k = kk.copy()
    k.append("A")
    for a in komb:
        li2 = adding(a, 0, k)
        for o in li2:
            li2 = adding(a, 1, o)
            li2[0].pop(-1)
            li2[1].pop(-1)
            checks(maina2(li2[0]), k[:-1], li2[0])
            checks(maina2(li2[1]), k[:-1], li2[1])
    k = kk.copy()
    k = list(reversed(k))
    if k[0] == "C":
        k.append("C")
    elif k[0] == "B":
        k.append("B")
    elif k[0] == "E":
        k.append("E")
    elif k[0] == "F":
        k.append("F")
    for a in komb:
        li2 = adding(a, 0, k)
        for o in li2:
            li2 = adding(a, 1, o)
            li2[0].pop(-1)
            li2[1].pop(-1)
            checks(maina2(li2[0]), k[:-1], li2[0])
            checks(maina2(li2[1]), k[:-1], li2[1])
    k = kk.copy()
    k.append("A")
    for a in komb:
        li2 = adding(a, 0, k)
        k1 = li2[0].pop(-1)
        k2 = li2[1].pop(-1)
        k1 = list(reversed(k1))
        k2 = list(reversed(k2))
        if k1[0] == "C":
            k1.append("C")
        elif k1[0] == "B":
            k1.append("B")
        elif k1[0] == "E":
            k1.append("E")
        elif k1[0] == "F":
            k1.append("F")
        if k2[0] == "C":
            k2.append("C")
        elif k2[0] == "B":
            k2.append("B")
        elif k2[0] == "E":
            k2.append("E")
        elif k2[0] == "F":
            k2.append("F")
        a1 = [a[0], len(k1) - a[1]]
        li2 = [k1, k2]
        for o in li2:
            li2 = adding(a1, 1, o)
            k1 = li2[0].pop(-1)
            k2 = li2[1].pop(-1)
            k11 = list(reversed(k1))
            k12 = list(reversed(k2))
            checks(maina2(k11), k[:-1], k11)
            checks(maina2(k12), k[:-1], k12)
    k = kk.copy()
    k = list(reversed(k))
    if k[0] == "C":
        k.append("C")
    if k[0] == "B":
        k.append("B")
    if k[0] == "E":
        k.append("E")
    if k[0] == "F":
        k.append("F")
    for a in komb:
        li2 = adding(a, 0, k)
        k1 = li2[0].pop(-1)
        k2 = li2[1].pop(-1)
        k1 = list(reversed(k1))
        k2 = list(reversed(k2))
        k1.append("A")
        k2.append("A")
        li2 = [k1, k2]
        a1 = a.copy()
        a1[1] = int(len(k1) - a[i])
        for o in li2:
            li2 = adding(a1, 1, o)
            k11 = li2[0].pop(-1)
            k12 = li2[1].pop(-1)
            checks(maina2(k11), k[:-1], k11)
            checks(maina2(k12), k[:-1], k12)


lis = []


f = open("output15.txt", "r")
for k in f.readlines():
    l = list(ast.literal_eval(k))
    lis.append(l[0])


N = len(lis[0])

lists = []
for i in lis:
    lists.append(maina1(i))

# print(lists)

# lip = []
# for i in lists:
#     lip.append(maina2(i))

# print(lip)

komb = gen()

# print(komb)
for t in lists:
    doing(t)
# doing(lists[0])


end_time = datetime.now()
print("Laiks: {}".format(end_time - start_time))
