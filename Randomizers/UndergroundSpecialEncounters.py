from Utils import List, Pool
import random

def randomize(tree, p):
    legList = List.getLegendaries()
    monsPool = Pool.getMons(p["gen"])
    monsNoLeg = Pool.Exclude(monsPool["mon"], monsPool["leg"])

    for mon in tree["Sheet1"]:
        if mon["monsNo"] != 0:
            if p["leg"]: mon["monsno"] = random.choice(monsNoLeg)
            else: mon["monsno"] = random.choice(monsPool["mon"])