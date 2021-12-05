from Utils import List
import random

def randomize(tree, p):
    legList = List.getLegendaries(0)
    for mons in tree["Personal"]:
        if p["leg"] and mons["monsno"] in legList: continue # Because we don't want to breed legendaries
        mons["egg_group1"] = random.randint(0, 15)
        mons["egg_group2"] = random.randint(0, 15)