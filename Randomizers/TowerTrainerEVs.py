from Utils import List
import random

def randomize(tree, p):
    for mon in tree["TrainerPoke"]:
        if p["r"]["trainers"]["ev"] == 1: # randomize
            values = List.getValuesInThreshold(510, 252, 6)
        elif p["r"]["trainers"]["ev"] == 2: # optimize
            values = List.getMaximizedValuesInThreshold(510, 252, 6)

        random.shuffle(values)
        mon["EffortHp"] = values[0]
        mon["EffortAtk"] = values[1]
        mon["EffortDef"] = values[2]
        mon["EffortSpAtk"] = values[3]
        mon["EffortSpDef"] = values[4]
        mon["EffortAgi"] = values[5]