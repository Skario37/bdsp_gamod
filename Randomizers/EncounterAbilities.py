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

def Ability(p, romFSPath):
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

    RandomizeAbilities(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'personal_masterdatas' saved.")
    os.chdir(cwd)
    return
    
def RandomizeAbilities(p, env):
    print(" - Randomizing encounters abilities.")
    for obj in env.objects:
        
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree["m_Name"] == "PersonalTable":
                for mon in tree["Personal"]:
                    r = random.sample(range(1, 256+1), 3)
                    if mon["tokusei1"] == mon["tokusei2"]: r[1] = r[0]
                    if mon["tokusei1"] == mon["tokusei3"]: r[2] = r[0]
                    for i in range(1,4):
                        mon["tokusei"f"{i}"] = r[i-1]
                obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")
    print(" - Encounters abilities randomized.")
    return