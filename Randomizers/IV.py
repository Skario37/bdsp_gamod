from pathlib import Path
import UnityPy
import random
import os

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Dpr"
yuzuModPath = "StreamingAssets\\AssetAssistant\\Dpr"
Trainer_Table = 676024375065692598
Tower_Trainer_Table = 7477832855307302314
pathList = [Trainer_Table,Tower_Trainer_Table]

def IV(p, romFSPath):
    cwd = os.getcwd()

    src = "masterdatas"

    outputPath = os.path.join(cwd, modPath)

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
    else: 
        print("ERROR: 'masterdatas' not found")
        return

    print(" ➥ 'masterdatas' loaded.")

    SetIV(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'masterdatas' saved.")
    os.chdir(cwd)
    return

def SetIV(p, env):
    print(" - Randomizing trainers IV's.")
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree["m_Name"] == "TrainerTable":
                for mon in tree["TrainerPoke"]:
                    for n in range(1, 7):
                        level = mon["P"f"{n}Level"]
                        if level > 0:
                            if p["r"]["trainer_iv"] == "1":
                                mon["P"f"{n}TalentHp"] = random.randint(0,31)
                                mon["P"f"{n}TalentAtk"] = random.randint(0,31)
                                mon["P"f"{n}TalentDef"] = random.randint(0,31)
                                mon["P"f"{n}TalentSpAtk"] = random.randint(0,31)
                                mon["P"f"{n}TalentSpDef"] = random.randint(0,31)
                                mon["P"f"{n}TalentAgi"] = random.randint(0,31)
                            elif p["r"]["trainer_iv"] == "2":
                                mon["P"f"{n}TalentHp"] = 31
                                mon["P"f"{n}TalentAtk"] = 31
                                mon["P"f"{n}TalentDef"] = 31
                                mon["P"f"{n}TalentSpAtk"] = 31
                                mon["P"f"{n}TalentSpDef"] = 31
                                mon["P"f"{n}TalentAgi"] = 31
                obj.save_typetree(tree)
            elif tree["m_Name"] == "TowerTrainerTable":
                for mon in tree["TrainerPoke"]:
                    if p["r"]["trainer_iv"] == "1":
                        mon["TalentHp"] = random.randint(0,31)
                        mon["TalentAtk"] = random.randint(0,31)
                        mon["TalentDef"] = random.randint(0,31)
                        mon["TalentSpAtk"] = random.randint(0,31)
                        mon["TalentSpDef"] = random.randint(0,31)
                        mon["TalentAgi"] = random.randint(0,31)
                    elif p["r"]["trainer_iv"] == "2":
                        mon["TalentHp"] = 31
                        mon["TalentAtk"] = 31
                        mon["TalentDef"] = 31
                        mon["TalentSpAtk"] = 31
                        mon["TalentSpDef"] = 31
                        mon["TalentAgi"] = 31
                obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")
    print(" - Trainers IV's randomized.")
    return 