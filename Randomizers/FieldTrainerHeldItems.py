from Utils import Pool
import random

def randomize(tree):
    items = Pool.getUsefullHeldItems()

    for mon in tree["TrainerPoke"]:
        for n in range(1, 7):
            level = mon["P"f"{n}Level"]
            if level > 0:
                mon["P"f"{n}Item"] = random.choice(items)