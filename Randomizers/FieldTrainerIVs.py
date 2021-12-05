import random

def randomize(tree, p):
    for mon in tree["TrainerPoke"]:
        for n in range(1, 7):
            level = mon["P"f"{n}Level"]
            if level > 0:
                if p["r"]["trainers"]["iv"] == 1: # randomize
                    mon["P"f"{n}TalentHp"] = random.randint(0,31)
                    mon["P"f"{n}TalentAtk"] = random.randint(0,31)
                    mon["P"f"{n}TalentDef"] = random.randint(0,31)
                    mon["P"f"{n}TalentSpAtk"] = random.randint(0,31)
                    mon["P"f"{n}TalentSpDef"] = random.randint(0,31)
                    mon["P"f"{n}TalentAgi"] = random.randint(0,31)
                elif p["r"]["trainers"]["iv"] == 2: # optimize
                    mon["P"f"{n}TalentHp"] = 31
                    mon["P"f"{n}TalentAtk"] = 31
                    mon["P"f"{n}TalentDef"] = 31
                    mon["P"f"{n}TalentSpAtk"] = 31
                    mon["P"f"{n}TalentSpDef"] = 31
                    mon["P"f"{n}TalentAgi"] = 31