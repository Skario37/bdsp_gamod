from Utils import List
import random

def randomize(tree, p):
    for mon in tree["TrainerPoke"]:
        for n in range(1, 7):
            level = mon["P"f"{n}Level"]
            if level > 0:
                if p["r"]["trainers"]["ev"] == 1: # randomize
                    values = List.getValuesInThreshold(510, 252, 6)
                elif p["r"]["trainers"]["ev"] == 2: # optimize
                    values = List.getMaximizedValuesInThreshold(510, 252, 6)
                    
                random.shuffle(values)
                mon["P"f"{n}EffortHp"] = values[0]
                mon["P"f"{n}EffortAtk"] = values[1]
                mon["P"f"{n}EffortDef"] = values[2]
                mon["P"f"{n}EffortSpAtk"] = values[3]
                mon["P"f"{n}EffortSpDef"] = values[4]
                mon["P"f"{n}EffortAgi"] = values[5]