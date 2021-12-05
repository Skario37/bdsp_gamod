from Utils import List
import random

def randomize(tree):
    moves = List.getMoves()
    movesLength = len(moves)
    for mon in tree["TrainerPoke"]:
        for n in range(1, 7):
            level = mon["P"f"{n}Level"]
            if level > 0:
                rMovesID = random.sample(range(0, movesLength), 4)
                for i in range(1,5):
                    if mon["P"f"{n}Waza"f"{i}"]: mon["P"f"{n}Waza"f"{i}"] = moves[rMovesID[i - 1]]