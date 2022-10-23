
# funkcija no dīvainajām Dekarta koordinātām listu pārveido uz listu, kur katrs saraksta saraksts
# tiek pārveidots par vienu burtu atkarībā no tā uz kuru virzienu iet mala.
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
            elem = list(e)
    return mysett


# funkcija pārbauda, vai polimonds beigās atgriežas sākuma koordinātās, kā arī, vai polimonds
# sevi nekur nekrusto(vai funkcijas point_gen() izveidotais sets satur tieši tik punktus, lai
# nebūtu iespējams, ka polimonds krustojas).
def checks(a, p, pp):
    global N
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
            print("{},".format(a))
            # print("{},".format(maina2(p)))

# galvenā funkcija.
# Tā paņem sarakstu ar dīvainajām Dekarta koordinātām un izveido visas burtu viknes, kur ir
# vēl divi jauni burti iesprausti iekšā. 
def doing(k):
    global komb
    k.append("A")
    for a in komb:
        i = 0
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
        k1.insert(a[0], li[0])
        k2.insert(a[0], li[1])
        # print(k1)
        # print(k2)
        li2 = [k1, k2]
        for o in li2:
            i = 1
            if (o[a[i] - 1] == "A" or o[a[i] - 1] == "D") and (o[a[i]] == "E" or o[a[i]] == "B"):
                li = ["C", "F"]
            elif (o[a[i] - 1] == "A" or o[a[i] - 1] == "D") and (o[a[i]] == "F" or o[a[i]] == "C"):
                li = ["B", "E"]
            elif (o[a[i] - 1] == "B" or o[a[i] - 1] == "E") and (o[a[i]] == "F" or o[a[i]] == "C"):
                li = ["D", "A"]
            elif (o[a[i] - 1] == "B" or o[a[i] - 1] == "E") and (o[a[i]] == "A" or o[a[i]] == "D"):
                li = ["C", "F"]
            elif (o[a[i] - 1] == "C" or o[a[i] - 1] == "F") and (o[a[i]] == "A" or o[a[i]] == "D"):
                li = ["B", "E"]
            elif (o[a[i] - 1] == "C" or o[a[i] - 1] == "F") and (o[a[i]] == "E" or o[a[i]] == "B"):
                li = ["A", "D"]
            k11 = o.copy()
            k12 = o.copy()
            k11.insert(a[1], li[0])
            k12.insert(a[1], li[1])
            k11.pop(-1)
            k12.pop(-1)
            checks(maina2(k11), k[:-1], k11)
            # checks(maina2(k12), k[:-1], k12)


lis = [


]


N = len(lis[0])

lists = []
for i in lis:
    lists.append(maina1(i))


komb = gen()

for t in lists:
    doing(t)
