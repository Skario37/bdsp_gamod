import random

def alterEncounters(tree, p):
    for area in tree["table"]:
        for key in area.keys():
            if type(area[key]) == list:
                for mon in area[key]:
                    if (type(mon) == dict):
                        if mon["monsNo"] > 0:
                            mon["maxlv"] = setLevel(mon["maxlv"], p)
                            mon["minlv"] = setLevel(mon["minlv"], p)
                            if mon["minlv"] > mon["maxlv"]:
                                mon["minlv"] = mon["maxlv"]

def alterTrainers(tree, p):
    for mon in tree["TrainerPoke"]:
        for no in range(1, 7):
            level = mon["P"f"{no}Level"]
            if level > 0:
                mon["P"f"{no}Level"] = setLevel(mon["P"f"{no}Level"], p)

def alterUnderground(tree, p):
    for level in tree["Data"]:
        level["MaxLv"] = setLevel(level["MaxLv"], p)
        level["MinLv"] = setLevel(level["MinLv"], p)
        if mon["MinLv"] > mon["MaxLv"]:
            mon["MinLv"] = mon["MaxLv"]

def setLevel(lvl, p):
    if p["level"]["modifier"] == 0:
        if p["level"]["decrease"] == 0 and p["level"]["increase"] > 0:
            return min(lvl + p["level"]["increase"], p["level"]["maximum"])
        elif p["level"]["decrease"] > 0 and p["level"]["increase"] == 0:
            return max(lvl + p["level"]["decrease"], p["level"]["minimum"])
        else:
            mini = max(lvl - p["level"]["decrease"], p["level"]["minimum"])
            maxi = min(lvl + p["level"]["increase"], p["level"]["maximum"])
    elif p["level"]["modifier"] == 1:
        if p["level"]["decrease"] == 0 and p["level"]["increase"] > 0:
            return min(int(lvl * (1 + p["level"]["increase"] / 100)), p["level"]["maximum"])
        elif p["level"]["decrease"] > 0 and p["level"]["increase"] == 0:
            return max(int(lvl * (1 - p["level"]["decrease"] / 100)), p["level"]["minimum"])
        else:
            mini = max(int(lvl * (1 - p["level"]["decrease"] / 100)), p["level"]["minimum"])
            maxi = min(int(lvl * (1 + p["level"]["increase"] / 100)), p["level"]["maximum"])

    if mini > maxi: 
        tmp = maxi
        maxi = mini
        mini = tmp
    return lvl