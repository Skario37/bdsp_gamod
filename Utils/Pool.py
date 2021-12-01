from . import List

def Pool(g):
    pool = {
        "mon": [],
        "leg": []
    }
    for i in g:
        if i == 1: 
            pool["mon"].extend(List.getMons(1))
            pool["leg"].extend(List.getLegendaries(1))
        if i == 2:
            pool["mon"].extend(List.getMons(2))
            pool["leg"].extend(List.getLegendaries(2))
        if i == 3:
            pool["mon"].extend(List.getMons(3))
            pool["leg"].extend(List.getLegendaries(3))
        if i == 4:
            pool["mon"].extend(List.getMons(4))
            pool["leg"].extend(List.getLegendaries(4))    
    return pool

def Exclude(l, el):
    nl = []
    for i in l:
        if i in el:continue
        else: nl.append(i)
    return nl

def getUsefullHeldItems():
    berries = List.getItems(4)
    pouch = List.getItems(5)

    for i in range(164, 183+1): # poffin / ev's
        if i in berries: berries.remove(i)
    
    for item in pouch:
        if item < 112: pouch.remove(item)
        elif item > 112 and item < 135: pouch.remove(item)
        elif item > 136 and item < 213: pouch.remove(item)
        elif item > 288 and item < 295: pouch.remove(item)
        elif item > 313: pouch.remove(item)
    
    return [*berries, *pouch]

def getUsefullItems():
    medicine = List.getItems(1)
    fight = List.getItems(3)
    berries = List.getItems(4)

    for item in medicine:
        if item > 134: medicine.remove(item)

    for item in berries: # poffin / ev's / divide dmg
        if item > 164 and item < 201: berries.remove(item)
        elif item > 210: berries.remove(item)

    return [*medicine, *fight, *berries]