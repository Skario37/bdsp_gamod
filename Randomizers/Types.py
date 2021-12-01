from pathlib import Path
import UnityPy
import random
import os

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Pml"
yuzuModPath = "StreamingAssets\\AssetAssistant\\Pml"
PersonalTable = 6925071152922426992
pathList = [PersonalTable]

def Type(p, romFSPath):
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

    RandomizeTypes(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'personal_masterdatas' saved.")
    os.chdir(cwd)
    return
    
def RandomizeTypes(p, env):
    print(" - Randomizing Pokémon types.")
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree["m_Name"] == "PersonalTable":
                    for personal in tree["Personal"]:
                        personal["type1"] = random.randint(0, 16)
                        personal["type2"] = random.randint(0, 16)
                    obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")
    print(" - Pokémon types randomized.")
    return