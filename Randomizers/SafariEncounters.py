from Utils import List, Pool
import random

def randomize(tree, p):
    legList = List.getLegendaries()
    monsPool = Pool.getMons(p["gen"])
    monsNoLeg = Pool.Exclude(monsPool["mon"], monsPool["leg"])

    for mon in tree["safari"]:
        if p["leg"]:
            if mon["MonsNo"] in legList:
                mon["MonsNo"] = random.choice(monsPool["leg"])
            else:
                mon["MonsNo"] = random.choice(monsNoLeg)
        else:
            mon["MonsNo"] = random.choice(monsPool["mon"])