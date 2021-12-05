from Utils import File
from Randomizers import EggGroups, EggMoves, EncounterAbilities, EncounterHeldItems, EncounterMoves, Evolutions, Types
from os import path, getcwd

filePath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Pml"
ModPath = "StreamingAssets\\AssetAssistant\\Pml"
SRC = "personal_masterdatas"

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
PersonalTable = 6925071152922426992
TamagoWazaTable = 1670399578319621162
WazaOboeTable = 1345203096983357567
EvolveTable = 5139195221601552760
path_list = [PersonalTable, TamagoWazaTable, WazaOboeTable, EvolveTable]

def load(console, romfspath):
    cwd = getcwd()
    inputPath = path.join(romfspath, ModPath)
    outputPath = path.join(cwd, filePath)
    env = File.load(inputPath, SRC)
    if not env: 
        console.append("ERROR: '"f"{path.join(inputPath, SRC)}' not found ")
        return False
    else: 
        console.append(" ➥ '"f"{SRC}' loaded.")
        return env
    
def save(console, env):
    cwd = getcwd() 
    outputPath = path.join(cwd, filePath)
    File.gotoDir(outputPath)
    File.write(SRC, env)
    console.append(" ⮨ '"f"{SRC}' saved.")
    File.gotoDir(cwd)

def proceed(console, env, p):
    for obj in env.objects:
        if obj.path_id in path_list:
            tree = obj.read_typetree()
            if tree["m_Name"] == "PersonalTable":
                if p["r"]["egggroups"]:
                    console.append(" - Randomizing egg groups.")
                    EggGroups.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Egg groups randomized.")

                if p["r"]["abilities"]["enc"]:
                    console.append(" - Randomizing encounter abilities.")
                    EncounterAbilities.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Encounter abilities randomized.")

                if p["r"]["helditems"]["enc"]:
                    console.append(" - Randomizing encounter held items.")
                    EncounterHeldItems.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Encounter held items randomized.")

                if p["r"]["types"]:
                    console.append(" - Randomizing types.")
                    Types.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Types randomized.")
                
                continue

            elif tree["m_Name"] == "TamagoWazaTable":
                if p["r"]["eggmoves"]:
                    console.append(" - Randomizing egg moves.")
                    EggMoves.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Egg moves randomized.")
                continue

            elif tree["m_Name"] == "WazaOboeTable":
                if p["r"]["moves"]["enc"]:
                    console.append(" - Randomizing encounter moves.")
                    EncounterMoves.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Encounter moves randomized.")

                continue
    
            elif tree['m_Name'] == "EvolveTable":
                if p["r"]["evolutions"]:
                    console.append(" - Randomizing evolutions.")
                    Evolutions.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Evolutions randomized.")

                continue
            else:
                console.append("ERROR: 'personal_masterdatas' use different path ids")
                continue