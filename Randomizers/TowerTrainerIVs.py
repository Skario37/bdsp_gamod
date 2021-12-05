import random

def randomize(tree, p):
    for mon in tree["TrainerPoke"]:
        if p["r"]["trainers"]["iv"] == 1: # randomize
            mon["TalentHp"] = random.randint(0,31)
            mon["TalentAtk"] = random.randint(0,31)
            mon["TalentDef"] = random.randint(0,31)
            mon["TalentSpAtk"] = random.randint(0,31)
            mon["TalentSpDef"] = random.randint(0,31)
            mon["TalentAgi"] = random.randint(0,31)
        elif p["r"]["trainers"]["iv"] == 2: # optimize
            mon["TalentHp"] = 31
            mon["TalentAtk"] = 31
            mon["TalentDef"] = 31
            mon["TalentSpAtk"] = 31
            mon["TalentSpDef"] = 31
            mon["TalentAgi"] = 31