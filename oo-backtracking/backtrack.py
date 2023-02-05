# Universāls "backtrack" algoritmu darbinatājs.
# Tajā var ievietot jebkuru objektu, kurš māk ar sevi veikt backtrack darbības.
# Lietojuma paraugs
# -------------------
# myBacktracker = SomeBacktrackerObject(...)
# b = Backtrack(myBacktracker)
# if b.attempt(0):  # sāk backtrack koka saknē, kur level = 0
#      q.display()  # izdrukā/saglabā uzdevuma atrisinājujmu.

class Backtrack:
    # Backtracker uzdevuma objekts (queens.QueenProblem, NSturis.NSturisProblem utml.)
    b = None

    # Konstruktors iekopē padoto backtracker uzdevuma objektu
    def __init__(self, b):
        self.b = b

    # Meklē risinājumus, atrodoties līmenī "level" backtrack kokā.
    # Uzdevums "b" (ja level > 0) jau satur kaut kādu (nepabeigtu) atrisinājuma mēģinājumu. 
    # Funkcija atgriež "True" tad un tikai tad, ja zem šī stāvokļa var atrast jaunu atrisinājumu.
    def attempt(self, level):
        successful = False
        move_iterator = self.b.moves(level)
        for move in move_iterator:
            if self.b.valid(level, move):
                self.b.record(level, move)
                if self.b.done(level):
                    successful = True
                else:
                    successful = self.attempt(level+1)
                    if not successful:
                        self.b.undo(level, move)
            if successful:
                break
        return successful
