from Utils import List
import random

def randomize(tree):
    moves = List.getMoves()
    movesLength = len(moves)
    for waza in tree["WazaOboe"]:
        if waza["ar"]:
            wazaLength = len(waza["ar"])
            rMoves = random.sample(range(0, movesLength), wazaLength)
            for i in range(1, wazaLength, 2):
                waza["ar"][i] = rMoves[i-1]
                    