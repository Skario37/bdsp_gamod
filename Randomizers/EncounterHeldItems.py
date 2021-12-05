from Utils import Pool
import random

def randomize(tree):
    heldItems = Pool.getUsefullHeldItems()
    for mon in tree["Personal"]:
        for n in range(1,7):
            mon["item"f"{n}"] = random.choice(heldItems)