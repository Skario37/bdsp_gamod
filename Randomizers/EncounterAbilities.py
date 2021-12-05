from Utils import List
import random

def randomize(tree):
    abilities = List.getAbilities()
    abilitiesLength = len(abilities)
    for mon in tree["Personal"]:
        rAbilitiesID = random.sample(range(0, abilitiesLength), 3)
        if mon["tokusei1"] == mon["tokusei2"]: rAbilitiesID[1] = rAbilitiesID[0]
        if mon["tokusei1"] == mon["tokusei3"]: rAbilitiesID[2] = rAbilitiesID[0]
        for i in range(1, 4):
            mon["tokusei"f"{i}"] = abilities[rAbilitiesID[i - 1]]