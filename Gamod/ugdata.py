from Utils import File
from Randomizers import UndergroundEncounters, UndergroundSpecialEncounters
from Modifiers import Level
from os import path, getcwd

filePath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\UnderGround\\data"
ModPath = "StreamingAssets\\AssetAssistant\\UnderGround\\data"
SRC = "ugdata"

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
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
UgEncount_20 = -6041552275203926594
UgSpecialPokemon = -220502742419523805
UgEncountLevel = 6066595358870788269
path_list = [UgEncount_02, UgEncount_03, UgEncount_04, UgEncount_05, UgEncount_06, UgEncount_07, UgEncount_08, UgEncount_09, UgEncount_10, UgEncount_11, UgEncount_12, UgEncount_20, UgSpecialPokemon, UgEncountLevel]

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
            if tree['m_Name'][:10] == "UgEncount_":
                if p["r"]["enc"]["underground"]:
                    console.append(" - Randomizing underground encounters.")
                    UndergroundEncounters.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Underground encounters randomized.")

                continue
            elif tree["m_Name"] == "UgSpecialPokemon":
                if p["r"]["enc"]["underground"]:
                    console.append(" - Randomizing underground special encounters.")
                    UndergroundSpecialEncounters.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Underground special encounters randomized.")

                continue

            elif tree["m_Name"] == "UgEncountLevel":
                if p["level"]["decrease"] != 0 or p["level"]["increase"] != 0 or p["level"]["minimum"] != 1 or p["level"]["maximum"] != 100:
                    console.append(" - Altering underground level.")
                    Level.alterUnderground(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Underground level altered.")

                continue
            else:
                console.append("ERROR: 'ugdata' use different path ids")
                continue