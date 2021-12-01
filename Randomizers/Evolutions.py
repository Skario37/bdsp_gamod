from pathlib import Path
import UnityPy
import random
import os

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Pml"
yuzuModPath = "StreamingAssets\\AssetAssistant\\Pml"
evolveTable = 5139195221601552760
pathList = [evolveTable]

def Evolution(p, romFSPath):
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

    RandomizeEvolution(p, env)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
    os.chdir(outputPath)
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    print(" ⮨ 'personal_masterdatas' saved.")
    os.chdir(cwd)
    return

def RandomizeEvolution(p, env):
    print(" - Randomizing evolutions.")
    r1 = random.sample(range(1,561), 560)
    r2 = random.sample(range(1,561), 560)
    i = 0
    
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree['m_Name'] == "EvolveTable":
                for mon in tree['Evolve']:
                    mon["id"] = r1[i]
                    if mon["ar"]:
                        l = len(mon["ar"])
                        for j in range(2,l,5):
                            mon["ar"][j] = r2[i]
                    i += 1
                obj.save_typetree(tree)
            else:
                print("ERROR: Use different path_id")

    print(" - Evolutions randomized.")
    return