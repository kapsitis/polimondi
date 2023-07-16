# Šis ir universāls "backtrack" algoritmu darbinatājs.
# Tajā var ievietot jebkuru objektu, kurš māk ar sevi veikt backtrack darbības.

# To izsauc šādi:
# myBacktracker = SomeBacktrackerObject(...)
# b = Backtrack(myBacktracker)
# if b.attempt(0):  # start backtracking at level = 0
#      q.display()  # display the first solution


class Backtrackk:

    # Backtracker objekts (nepabeigts šaha galdiņš, polimonds vai kas cits)
    b = None

    # Konstruktors tikai iekopē padoto objektu
    def __init__(self, b):
        self.b = b

    # Mēģina risināt uzdevumu, atrodoties koka līmenī "level"
    # level=0 ir pašā augšā - pirms izdarīti "gājieni" (novietotas jebkādas dāmas)
    def attempt(self, level):
        successful = False
        moveIterator = self.b.moves(level)

        # i = 0
        for move in moveIterator:
            successful = False
            #print('btrackk move({}), level({}), i({}) out of {}'.format(move, level, i, moveIterator))
            #i += 1
            if self.b.valid(level, move):
                self.b.record(level, move)
                if self.b.done(level):
                    successful = True
                else:
                    successful = self.attempt(level+1)
                    if not successful:
                        self.b.undo(level, move)
            if successful:
                self.b.display()
                self.b.undo(level, move)
