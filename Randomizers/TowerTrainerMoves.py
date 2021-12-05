from Utils import List
import random

def randomize(tree):
    moves = List.getMoves()
    movesLength = len(moves)

    for mon in tree["TrainerPoke"]:
        rMovesID = random.sample(range(0, movesLength), 4)
        for i in range(1,5):
            if mon["Waza"f"{i}"]: mon["Waza"f"{i}"] = moves[rMovesID[i - 1]]