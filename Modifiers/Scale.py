import random

def alter(tree, p):
    for mon in tree["Catalog"]:
        if p["scaling"] == 1:
            mon["BattleScale"] = 1.0
            mon["ContestScale"] = 1.0
            mon["FieldScale"] = 1.0
            mon["FieldChikaScale"] = 1.0
            mon["FieldWalkingScale"] = 1.0
            mon["FieldFureaiScale"] = 1.0
            mon["DistributionScale"] = 1.0
        elif p["scaling"] == 2:
            mon["BattleScale"] = randomize(mon["CompareScale"], mon["BattleScale"])
            mon["ContestScale"] = randomize(mon["CompareScale"], mon["ContestScale"])
            mon["FieldScale"] = randomize(mon["CompareScale"], mon["FieldScale"])
            mon["FieldChikaScale"] = randomize(mon["CompareScale"], mon["FieldChikaScale"])
            mon["FieldWalkingScale"] = randomize(mon["CompareScale"], mon["FieldWalkingScale"])
            mon["FieldFureaiScale"] = randomize(mon["CompareScale"], mon["FieldFureaiScale"])
            mon["DistributionScale"] = randomize(mon["CompareScale"], mon["DistributionScale"])

def randomize(init, size):
    if size < init:
        return round(random.uniform(size, size + 1), 2)
    else:
        return round(random.uniform(size - 1, size), 2)