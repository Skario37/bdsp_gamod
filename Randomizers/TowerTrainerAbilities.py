from Utils import List
import random

def randomize(tree):
    abilities = List.getAbilities()

    for mon in tree["TrainerPoke"]:
        mon["Tokusei"] = random.choice(abilities)