# -*- coding: utf-8 -*-

# Šis ir universāls "backtrack" algoritmu darbinatājs.
# Tajā var ievietot jebkuru objektu, kurš māk ar sevi veikt backtrack darbības.

# To izsauc šādi:
# myBacktracker = SomeBacktrackerObject(...)
# b = Backtrack(myBacktracker)
# if b.attempt(0):  # start backtracking at level = 0
#      q.display()  # display the first solution



class Backtrack:

    # Backtracker objekts - šaha galdiņš, kuram dažas pirmās kolonnas var būt aizpildītas
    b = None

    # Konstruktors iekopē padoto backtracker objektu
    def __init__(self, b):
        self.b = b

    # Mēģina risināt uzdevumu, atrodoties koka līmenī "level" un
    # sākumstāvoklī, kurā novietotas kaut kādas dāmas, turpina DFS apstaigāšanu
    # un atgriež "True" tad un tikai tad, ja izdodas atrast jaunu atrisinājumu.
    def attempt(self, level):
        self.b.debugState("AAA ")

        successful = False

        # Savāc iteratoru no steka, ja tur ir (vai arī izveido jaunu range(0,n))
        # if len(self.b.rowPos) > level:
        #     moveIterator = self.b.moves(level, self.b.rowPos[level])
        # else:
        #     moveIterator = self.b.moves(level, 0)
        moveIterator = self.b.moves(level)


        # if len(self.b.rowPos) > level:  # skip stuff that was visited earlier
        #     for j in range(self.b.rowPos[level]):
        #         next(moveIterator)
        #         print('  level={}, j={}'.format(level,j))
        #     successful = self.attempt(level+1)

        # else:
        for move in moveIterator:
            if self.b.valid(level, move):
                self.b.record(level, move)   # ALSO Record Move Interator?
                self.b.debugState("BBB ")
                if self.b.done(level):
                    successful= True
                else:
                    successful = self.attempt(level+1)
                    if not successful:
                        self.b.undo(level, move)
            if successful:
                break
        return successful
