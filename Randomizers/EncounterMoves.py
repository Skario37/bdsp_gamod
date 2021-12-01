from pathlib import Path
from Utils import List
import UnityPy
import random
import os

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Pml"
yuzuModPath = "StreamingAssets\\AssetAssistant\\Pml"
WazaOboeTable = 1345203096983357567
pathList = [WazaOboeTable]

def Move(p, romFSPath):
    cwd = os.getcwd()

    src = "personal_masterdatas"

    outputPath = os.path.join(cwd, modPath)

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
    else: 
        print("ERROR: 'personal_masterdatas' not found")
        return

    print(" ➥ 'personal_masterdatas' loaded.")

    RandomizeMoves(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'personal_masterdatas' saved.")
    os.chdir(cwd)
    return
    
def RandomizeMoves(p, env):
    print(" - Randomizing encounters moves.")
    moves = List.getMoves()
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree["m_Name"] == "WazaOboeTable":
                for waza in tree["WazaOboe"]:
                    if waza["ar"]:
                        l = len(waza["ar"])
                        r = random.sample(range(1, len(moves)+1), l)
                        for i in range(1,l,2):
                            waza["ar"][i] = r[i-1]
                obj.save_typetree(tree)
            elif tree["m_Name"] == "TamagoWazaTable":
                for waza in tree["Data"]:
                    if waza["wazaNo"]:
                        l = len(waza["wazaNo"])
                        r = random.sample(range(1, len(moves)+1), l)
                        for i in range(0,l):
                            waza["wazaNo"][i] = r[i]
                obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")
    print(" - Encounters moves randomized.")
    return