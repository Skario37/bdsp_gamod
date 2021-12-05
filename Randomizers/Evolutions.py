from Utils import List, Pool
import random

def randomize(tree, p):
    legList = List.getLegendaries()
    length = len(tree['Evolve'])
    # Randomize base Pokémon and Pokémon to evolve without change evolution method
    rMon = random.sample(range(1,length + 1), length)
    rMonar = random.sample(range(1,length + 1), length)
    if p["leg"]:
        rMon = Pool.Exclude(rMon, legList)
        rMonar = Pool.Exclude(rMonar, legList)

    i = 0
    for mon in tree['Evolve']:
        # If Keep Legendaries
        # Don't evolve legendaries or evolve to legendary
        if p["leg"] and mon["id"] in legList: continue # Skip base legendary
        
        mon["id"] = rMon[i]
        
        if mon["ar"]:
            l = len(mon["ar"])
            for j in range(2,l,5):
                if p["leg"] and mon["ar"][j] in legList: continue # Skip base evolve to legendary
                
                mon["ar"][j] = rMonar[i]
        i += 1