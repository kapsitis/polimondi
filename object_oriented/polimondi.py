from backtrack import *


class Polimondi:

    liss = []
    p = 0
    x111 = 0
    mysett = []
    p = 0

    def __init__(self, n):
        self.N = n
        self.liss.append([0, self.N])
        self.p = [0, self.N]
        self.x111 = self.N-1
        for i in range(1, self.N+1):
            self.mysett.append([i, 0, -i])


    # Funkcija 33.rindā pārbauda, vai gadījumā, ja pēdējais nogrieznis ar garumu 1 ir pielikts,
    # vai viņš nav horizontāli novietots, tādā gadījumā polimonds būtu nepareizs,
    # jo jau pirmais nogrieznis ir horizontāls.

    # Visa pārēja funkcijas daļa sataisa jaunu sarakstu (new_mysett_elem), kur ir ieliktas
    # iespējamās jauno malu koordinātas. 58. rinda pārbauda, vai neviens no jaunajiem punktiem
    # jau neatrodas sarakstā mysett.

    def checks(self, move):
        self.move = move
        self.list1 = self.liss.copy()
        self.list1.append(move)
        if move[0] == 0 and (move[1] == 1 or move[1] == -1):
            return False
        new_mysett_elem = []
        ped = self.mysett[-1]
        ll0 = self.move[0]
        ll1 = self.move[1]
        for k in range(self.N-(self.level)):
            if ll0 == 0 and ll1 > 0:
                new_mysett_elem.append(
                    [(k+1+ped[0]), (ped[1]), (ped[2])-(k+1)])
            elif ll0 == 0 and ll1 < 0:
                new_mysett_elem.append(
                    [(ped[0])-(k+1), (ped[1]), (k+1+ped[2])])
            elif ll0 > 0 and ll1 > 0:
                new_mysett_elem.append(
                    [(k+1+ped[0]), (ped[1])-(k+1), (ped[2])])
            elif ll0 < 0 and ll1 < 0:
                new_mysett_elem.append(
                    [(ped[0])-(k+1), (k+1+ped[1]), (ped[2])])
            elif ll0 < 0 and ll1 > 0:
                new_mysett_elem.append(
                    [(ped[0]), (k+1+ped[1]), (ped[2])-(k+1)])
            elif ll0 > 0 and ll1 < 0:
                new_mysett_elem.append(
                    [(ped[0]), (ped[1])-(k+1), (k+1+ped[2])])
        if all(a not in self.mysett for a in new_mysett_elem) == False:
            return False
        else:
            self.new_mysett_elem = new_mysett_elem
            # print(self.liss)
            # print(self.new_mysett_elem)
            # print(self.mysett)
            # print(" ")
            return True

    # Funkcija pārbauda, vai pievienojot jauno malu, ir iespējams atgriezties atpakaļ sākumpunktā
    # ar atlikušajām malām. d-jau izveidotā polimonda augstums, v-platums.

    def checks2(self, level):
        d = 0
        v = 0
        for k in self.list1:
            d += k[0]
            v += k[1]
        m = self.N - self.level - 1
        mm = m*(m+1)/2
        if mm < abs(d) or mm < abs(v):
            return False
        return True

    def valid(self, level, move):
        self.p = move
        if self.checks(move) and self.checks2(move):
            # print(move)
            return True

    def done(self, level):
        if level == self.N - 1:
            return True
        return False

    # Pievienojam jauno malu sarakstā liss un šīs malas visus punktus sarakstā mysett.

    def record(self, level, move):
        self.liss.append(move)
        for k in self.new_mysett_elem:
            self.mysett.append(k)

    # Parāpjamies atpakaļ, ja bija sasniegts strupceļš

    def undo(self, level, move):
        self.liss = self.liss[:-1]
        self.mysett = self.mysett[:-(self.N-(level))]
        self.new_mysett_elem = []

    # Izvada risinājumu kompaktā formā

    def display(self):
        print("{},".format(self.liss))

    # Atgriež četrus (pirmājā solī divus) iespējamos gājienus, kā polimondu no dotā punkta var turpināt.

    def moves(self, level):
        self.level = level
        if self.level == 1:
            li1 = [[self.x111, -self.x111 / 2], [self.x111, self.x111 / 2]]
        else:
            x1 = self.N - (self.level)
            p = self.p
            if p[0] == 0 and p[1] > 0 or p[0] == 0 and p[1] < 0:
                li1 = [[x1, -x1 / 2], [x1, x1 / 2],
                       [-x1, -x1 / 2], [-x1, x1 / 2]]
            elif p[0] < 0 and p[1] > 0 or p[0] > 0 and p[1] < 0:
                li1 = [[0, -x1], [x1, x1 / 2], [0, x1], [-x1, -x1 / 2]]
            elif p[0] < 0 and p[1] < 0 or p[0] > 0 and p[1] > 0:
                li1 = [[0, -x1], [x1, -x1 / 2], [0, x1], [-x1, x1 / 2]]
        return li1


def main():
    q = Polimondi(7)
    b = Backtrack(q)
    if b.attempt(1):
        q.display()


if __name__ == '__main__':
    main()
