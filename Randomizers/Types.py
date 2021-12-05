import random

def randomize(tree):
    for mon in tree["Personal"]:
        # Same index is monotype
        mon["type1"] = random.randint(0, 16)
        mon["type2"] = random.randint(0, 16)