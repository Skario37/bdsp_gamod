from Utils import Pool
import random

def randomize(tree):
    items = Pool.getUsefullHeldItems()
    for mon in tree["TrainerPoke"]:
        mon["Item"] = random.choice(items)