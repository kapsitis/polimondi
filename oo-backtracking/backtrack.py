# Šis ir universāls "backtrack" algoritmu darbinatājs.
# Tajā var ievietot jebkuru objektu, kurš māk ar sevi veikt backtrack darbības.

# To izsauc šādi:
# myBacktracker = SomeBacktrackerObject(...)
# b = Backtrack(myBacktracker)
# if b.attempt(0):  # start backtracking at level = 0
#      q.display()  # display the first solution

class Backtrack:
    # Backtracker objekts (queens.QueenProblem, NSturis.NSturisProblem vai līdzīgs)
    b = None

    # Konstruktors iekopē padoto backtracker objektu
    def __init__(self, b):
        self.b = b

    # Mēģina risināt uzdevumu, atrodoties koka līmenī "level" un
    # sākumstāvoklī, kurā novietotas kaut kādas dāmas, turpina DFS apstaigāšanu
    # un atgriež "True" tad un tikai tad, ja izdodas atrast jaunu atrisinājumu.
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
