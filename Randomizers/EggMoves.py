from Utils import List
import random

def randomize(tree):
    moves = List.getMoves()
    movesLength = len(moves)
    for tama in tree["Data"]:
        # First one is dummy data without wazaNo items
        if tama["wazaNo"]:
            tamaLength = len(tama["wazaNo"])
            rMoves = random.sample(range(0, movesLength), tamaLength)
            for i in range(0, tamaLength):
                tama["wazaNo"][i] = rMoves[i]
                    