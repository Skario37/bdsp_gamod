from Utils import File
from Randomizers import FieldEncounters, SafariEncounters
from Modifiers import Level
from os import path, getcwd

filePath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Dpr\\scriptableobjects"
ModPath = "StreamingAssets\\AssetAssistant\\Dpr\\scriptableobjects"
SRC = "gamesettings"

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
FieldEncountTable_d = 361824127573837173
FieldEncountTable_p = -9035030829162387677
path_list = [FieldEncountTable_d, FieldEncountTable_p]

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
            if tree["m_Name"] == "FieldEncountTable_d" or tree["m_Name"] == "FieldEncountTable_p":
                if p["r"]["enc"]["field"]:
                    console.append(" - Randomizing field encounters.")
                    FieldEncounters.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Field encounters randomized.")

                if p["r"]["enc"]["safari"]:
                    console.append(" - Randomizing safari encounters.")
                    SafariEncounters.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Safari encounters randomized.")

                if p["level"]["decrease"] != 0 or p["level"]["increase"] != 0 or p["level"]["minimum"] != 1 or p["level"]["maximum"] != 100:
                    console.append(" - Altering encounters level.")
                    Level.alterEncounters(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Encounters level altered.")
                
                continue
            else:
                console.append("ERROR: 'gamesettings' use different path ids")
                continue