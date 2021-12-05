from Utils import Pool
import random

def randomize(tree):
    items = Pool.getUsefullItems()
    for trainer in tree["TrainerData"]:
        for n in range(1, 5):
            trainer["UseItem"f"{n}"] = random.choice(items)