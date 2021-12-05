from Utils import List, Pool
import random

def randomize(tree, p):
    legList = List.getLegendaries()
    monsPool = Pool.getMons(p["gen"])
    monsNoLeg = Pool.Exclude(monsPool["mon"], monsPool["leg"])

    for mon in tree["TrainerPoke"]:
        for n in range(1, 7):
            level = mon["P"f"{n}Level"]
            if level > 0:
                if p["leg"]:
                    if mon["P"f"{n}MonsNo"] in legList:
                        mon["P"f"{n}MonsNo"] = random.choice(monsPool["leg"])
                    else:
                        mon["P"f"{n}MonsNo"] = random.choice(monsNoLeg)
                else:
                    mon["P"f"{n}MonsNo"] = random.choice(monsPool["mon"])