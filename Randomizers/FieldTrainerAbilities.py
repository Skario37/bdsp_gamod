from Utils import List
import random

def randomize(tree):
    abilities = List.getAbilities()

    for mon in tree["TrainerPoke"]:
        for n in range(1, 7):
            level = mon["P"f"{n}Level"]
            if level > 0:
                mon["P"f"{n}Tokusei"] = random.choice(abilities)