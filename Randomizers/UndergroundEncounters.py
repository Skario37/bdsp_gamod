from pathlib import Path
from Utils import Pool
import UnityPy
import random
import os

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\UnderGround\\data"
yuzuModPath = "StreamingAssets\\AssetAssistant\\UnderGround\\data"
UgEncount_02 = 2921998521783056987
UgEncount_03 = 3120829428501700040
UgEncount_04 = 8994974075820978024
UgEncount_05 = 554439615776598099
UgEncount_06 = 1749855953384930022
UgEncount_07 = -233820855963829723
UgEncount_08 = -8064315274480865434
UgEncount_09 = 6067500095907821527
UgEncount_10 = -6533677965289877687
UgEncount_11 = -117713607888148647
UgEncount_12 = -4148679105701947902
pathList = [UgEncount_02, UgEncount_03, UgEncount_04, UgEncount_05, UgEncount_06, UgEncount_07, UgEncount_08, UgEncount_09, UgEncount_10, UgEncount_11, UgEncount_12]

def Encount(p, romFSPath):
    cwd = os.getcwd()

    src = "ugdata"

    outputPath = os.path.join(cwd, modPath)

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
    else: 
        print("ERROR: 'ugdata' not found")
        return

    print(" ➥ 'ugdata' loaded.")

    RandomizeEncount(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'ugdata' saved.")
    os.chdir(cwd)
    return

def RandomizeEncount(p, env):
    print(" - Randomizing Underground encounters.")
    for obj in env.objects:
        
        if obj.path_id in pathList:
            tree = obj.read_typetree()

            if tree['m_Name'][:10] == "UgEncount_":
                for mon in tree["table"]:
                    if p["r"]["s"]["leg"]:
                        mon["monsno"] = random.choice(Pool.Exclude(p["pool"]["mon"], p["pool"]["leg"]))
                    else:
                        mon["monsno"] = random.choice(p["pool"]["mon"])
                obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")

    print(" - Underground encounters randomized.")
    return