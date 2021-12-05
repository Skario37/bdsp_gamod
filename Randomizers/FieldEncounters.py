from Utils import List, Pool
import random

def randomize(tree, p):
    legList = List.getLegendaries()
    monsPool = Pool.getMons(p["gen"])
    monsNoLeg = Pool.Exclude(monsPool["mon"], monsPool["leg"])

    for area in tree["table"]:
        for key in area.keys():
            if type(area[key]) != int:
                if type(area[key][0]) == dict:
                    for mon in area[key]:
                        if mon["monsNo"] != 0:
                            if p["leg"]:
                                if mon["monsNo"] in legList:
                                    mon["monsNo"] = random.choice(monsPool["leg"])
                                else:
                                    mon["monsNo"] = random.choice(monsNoLeg)
                            else:
                                mon["monsNo"] = random.choice(monsPool["mon"])
    # Maybe separate below and make them options
    for mon in tree["urayama"]:
        if p["leg"]:
            if mon["monsNo"] in legList:
                mon["monsNo"] = random.choice(monsPool["leg"])
            else:
                mon["monsNo"] = random.choice(monsNoLeg)
        else:
            mon["monsNo"] = random.choice(monsPool["mon"])
    
    for mon in tree["mistu"]:
        if p["leg"]:
            if mon["Normal"] in legList:
                mon["Normal"] = random.choice(monsPool["leg"])
            else:
                mon["Normal"] = random.choice(monsNoLeg)

            if mon["Rare"] in legList:
                mon["Rare"] = random.choice(monsPool["leg"])
            else:
                mon["Rare"] = random.choice(monsNoLeg)

            if mon["SuperRare"] in legList:
                mon["SuperRare"] = random.choice(monsPool["leg"])
            else:
                mon["SuperRare"] = random.choice(monsNoLeg)
        else:
            mon["Normal"] = random.choice(monsPool["mon"])
            mon["Rare"] = random.choice(monsPool["mon"])
            mon["SuperRare"] = random.choice(monsPool["mon"])

    for mon in tree["honeytree"]:
        if p["leg"]:
            if mon["Normal"] in legList:
                mon["Normal"] = random.choice(monsPool["leg"])
            else:
                mon["Normal"] = random.choice(monsNoLeg)

            if mon["Rare"] in legList:
                mon["Rare"] = random.choice(monsPool["leg"])
            else:
                mon["Rare"] = random.choice(monsNoLeg)
        else:
            mon["Normal"] = random.choice(monsPool["mon"])
            mon["Rare"] = random.choice(monsPool["mon"])