from pathlib import Path
from Utils import Pool, List
import UnityPy
import random
import os

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Dpr\\scriptableobjects"
yuzuModPath = "StreamingAssets\\AssetAssistant\\Dpr\\scriptableobjects"
diamondEncount = 361824127573837173
pearlEncount = -9035030829162387677
pathList = [diamondEncount,pearlEncount]

def Encount(p, romFSPath):
    cwd = os.getcwd()

    src = "gamesettings"

    outputPath = os.path.join(cwd, modPath)

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
    else: 
        print("ERROR: 'gamesettings' not found")
        return

    print(" ➥ 'gamesettings' loaded.")

    RandomizeEncount(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'gamesettings' saved.")
    os.chdir(cwd)
    return

def RandomizeEncount(p, env):
    print(" - Randomizing encounters.")
    for obj in env.objects:
        
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree["m_Name"] == "FieldEncountTable_d" or tree["m_Name"] == "FieldEncountTable_p":
                # FieldEncountTable_d (diamond) FieldEncountTable_p (pearl)
                for area in tree["table"]:
                    for key in area.keys():
                        if type(area[key]) != int:
                            if type(area[key][0]) == dict:
                                for mon in area[key]:
                                    if mon["monsNo"] != 0:
                                        if p["r"]["s"]["leg"]:
                                            for legsNo in List.getLegendaries(0):
                                                if mon["monsNo"] == legsNo:
                                                    mon["monsNo"] = random.choice(p["pool"]["leg"])
                                                else:
                                                    mon["monsNo"] = random.choice(Pool.Exclude(p["pool"]["mon"], p["pool"]["leg"]))
                                        else:
                                            mon["monsNo"] = random.choice(p["pool"]["mon"])
                obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")
    print(" - Encounters randomized.")
    return