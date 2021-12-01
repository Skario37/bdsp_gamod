from pathlib import Path
from Utils import Pool
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

def HeldItem(p, romFSPath):
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

    RandomizeHeldItems(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'masterdatas' saved.")
    os.chdir(cwd)
    return

def RandomizeHeldItems(p, env):
    print(" - Randomizing trainers held items.")
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree["m_Name"] == "TrainerTable":
                for mon in tree["TrainerPoke"]:
                    for n in range(1, 7):
                        level = mon["P"f"{n}Level"]
                        if level > 0:
                            mon["P"f"{n}Item"] = random.choice(Pool.getUsefullHeldItems())
                obj.save_typetree(tree)
            elif tree["m_Name"] == "TowerTrainerTable":
                for mon in tree["TrainerPoke"]:
                    mon["Item"] = random.choice(Pool.getUsefullHeldItems())
                obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")
    print(" - Trainers held items randomized.")
    return