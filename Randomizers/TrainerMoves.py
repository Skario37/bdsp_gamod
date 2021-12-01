from pathlib import Path
from Utils import List
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

def Move(p, romFSPath):
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

    randomizeMoves(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'masterdatas' saved.")
    os.chdir(cwd)
    return

def randomizeMoves(p, env):
    print(" - Randomizing trainers moves.")
    moves = List.getMoves()
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree["m_Name"] == "TrainerTable":
                for mon in tree["TrainerPoke"]:
                    for n in range(1, 7):
                        level = mon["P"f"{n}Level"]
                        if level > 0:
                            r = random.sample(range(1, len(moves)), 4)
                            for i in range(1,5):
                                if mon["P"f"{n}Waza"f"{i}"]: mon["P"f"{n}Waza"f"{i}"] = r[i-1]
                obj.save_typetree(tree)
            elif tree["m_Name"] == "TowerTrainerTable":
                for mon in tree["TrainerPoke"]:
                    r = random.sample(range(1, len(moves)), 4)
                    for i in range(1,5):
                        if mon["Waza"f"{i}"]: mon["Waza"f"{i}"] = r[i-1]
                obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")
    print(" - Trainers moves randomized.")
    return