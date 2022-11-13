# https://dl.acm.org/doi/pdf/10.1145/331795.331886
# https://realpython.com/python-interface/
# https://stackoverflow.com/questions/19151/how-to-build-a-basic-iterator

from backtrack import *

# Mazliet izmainīts šaha dāmu algoritms - rindas un kolonnas numurētas, sākot ar 0. 
class QueenProblem: 
    # Galdiņa izmēru faktiski uzstāda __init__
    MAXROW = 0

    # Ja rowPos[x]==y  (y pieder [0;n-1]), tad x-tās kolonnas y-tajā rindiņā ir novietota dāma; 
    # ja rowPos[x]==-1, tad x kolonna ir tukša
    rowPos = []

    # Aizņemtās rindas. Ja row[x]==1, tad x-tajā rindā jau ir dāma.  Rindas numurē ar skaitļiem no [0; n-1]
    row = []

    # Aizņemtās diagonāles, kuras iet uz leju un pa kreisi. Ja leftDiag[x]==1, tad šajā diagonālē novietota dāma
    # Diagonāles skaitli iegūst, saskaitot rindiņu un kolonnu. Teiksim, dāma kreisajā augšējā stūrī (1,1) ir uz diagonāles 1+1=2. 
    # leftDiag[0] un leftDiag[1] neizmanto
    leftDiag = []
    # Aizņemtās diagonāles, kuras iet uz leju un pa kreisi. Ja leftDiag[x]==1, tad šajā diagonālē novietota dāma
    # Diagonāles skaitli iegūst, atņemot no kolonnas rindiņu. Šaha galdiņam 8*8 šīs diagonāles ir -7, -6, ...., 6, 7. 
    # Python gadījumā šim skaitlim vēl pieskaita MAXROW, piemēram 8. Skaitli rightDiag[0] neizmanto. 
    rightDiag = []



    # Izveido šaha galdiņu n*n; visas dāmu pozīcijas un visas apdraudētās pozīcijas sākotnēji ir False. 
    # (Polimondiem - visi saraksti sākumā ir tukši)
    def __init__(self, n):
        self.MAXROW = n
        self.leftDiag = [0]*(2*self.MAXROW-1)
        self.rightDiag = [0] * (2*self.MAXROW-1)
        self.row = [0]*(self.MAXROW)
        self.rowPos = [-1]*(self.MAXROW)
        
    # Funkcija, lai ielūkotos backtracking objekta iekšējā stāvoklī
    def debugState(self): 
        print('rowPos={}, row={}, leftDiag={}, rightDiag={}'.format(self.rowPos, self.row, self.leftDiag, self.rightDiag))

    # Pielabo apdraudējumu datu struktūras pēc dāmas uzlikšanas/novākšanas
    def setPosition(self, rowNo, colNo, status):
        self.row[rowNo] = status
        self.leftDiag[rowNo+colNo] = status
        self.rightDiag[rowNo - colNo + self.MAXROW - 1] = status

    # Vai var dāmu uzlikt uz galdiņa?
    # "move" te nozīmē jaunas dāmas uzlikšanu. 
    def valid(self, level, move):
        rowNo = move
        colNo = level
        # visiem apdraudējumiem jābūt 0
        result = (self.row[rowNo] == 0) and (self.leftDiag[rowNo + colNo] == 0) and (self.rightDiag[rowNo - colNo + self.MAXROW - 1] == 0)
        return result

    # Vai visas dāmas jau izvietotas (vai n-polimonds sekmīgi noslēdzis vienkāršo lauzto līniju)?
    def done(self, level):
        return (level + 1 >= self.MAXROW)

    # Pievienojam esošo gājienu
    def record(self, level, move):
        rowNo = move
        colNo = level
        self.rowPos[colNo] = rowNo
        self.setPosition(rowNo, colNo, 1)

    # Parāpjamies atpakaļ, ja bija sasniegts strupceļš
    def undo(self, level, move):
        rowNo = move
        colNo = level
        self.rowPos[colNo] = 0
        self.setPosition(rowNo, colNo, 0)


    # Izvada risinājumu kompaktā formā
    def display(self):
        # for i in range(1, self.MAXROW+1):
        #     for j in range(1, self.MAXROW + 1):
        #         if self.rowPos[j] == i:
        #             print("1", end=" ")
        #         else:
        #             print("0", end=" ")
        #     print()
        print('rowPos={}'.format(self.rowPos))

    # Atgriež iteratoru ar iespējamiem gājieniem: 
    # Kārtējā kolonnā dāmu mēģina nolikt jebkurā rindiņā (1...n), algoritms pats izlaidīs apdraudētās pozīcijas.
    # Polimondu pasaulē iteratoram būtu jāatgriež četri iespējamie gājieni, kā polimondu no dotā punkta var turpināt. 
    def moves(self, level):
        return self.QueenEnumeration(self)


    # Iekšēja klase (Inner class) - QueenEnumeration dzīvo QueenPosition vēderā un 
    # var piekļūt visiem tās globālajiem mainīgajiem. 
    # Pieejas smukums ir tāds, ka "QueenEnumeration" ir tādi objekti, kuriem nav 
    # jēgas ārpus "QueenPosition" - tāpēc neviens cits tiem objektiem netiek klāt un nevar neko nobojāt, 
    # bet paši šie objekti tiek klāt tam, ko viņiem vajag. 

    # Polimondu gadījumā - var uztaisīt līdzīgu iteratoru, kurš atgriež nevis visas iespējamās rindas, 
    # bet relatīvos (vai varbūt absolūtos?) virzienus. Piemēram: 
    # "ass pagrieziens pa kreisi" - bruņurupucis pagriežas par +120 grādiem    
    # "nedaudz pa kreisi" - bruņurupucis pagriežas par +60 grādiem
    # "nedaudz pa labi" - bruņurupucis pagriežas par -60 grādiem
    # "ass pagrieziens pa labi" - bruņurupucis pagriežas par -120 grādiem
    class QueenEnumeration:
        cursor = -1
        outer_instance = None

        def __init__(self, outer_instance):
            # self.cursor = -1
            self.outer_instance = outer_instance

        # Laikam var atstāt šādi: Iterators atgriež pats savu tekošo objektu        
        def __iter__(self):
            # self.cursor = -1
            return self
    
        #def hasMoreElements(self):
        #    return (self.cursor < self.outer_instance.MAXROW+1)
        

        def __next__(self):
            self.cursor += 1
            if self.cursor < self.outer_instance.MAXROW:
                return self.cursor
            raise StopIteration



def main():
    q = QueenProblem(4)
    b = Backtrack(q)
    if b.attempt(0):
        q.display()

if __name__ == '__main__':
    main()




