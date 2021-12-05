from Utils import File
from Randomizers import FieldTrainerItems, FieldTrainers, TowerTrainers, FieldTrainerIVs, TowerTrainerIVs, FieldTrainerEVs, TowerTrainerEVs, FieldTrainerMoves, TowerTrainerMoves, FieldTrainerAbilities, TowerTrainerAbilities, FieldTrainerHeldItems, TowerTrainerHeldItems
from Modifiers import Level, Scale
from os import path, getcwd

filePath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Dpr"
ModPath = "StreamingAssets\\AssetAssistant\\Dpr"
SRC = "masterdatas"

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
TrainerTable = 676024375065692598
TowerTrainerTable = 7477832855307302314
PokemonInfo = 3987417216388098002
path_list = [TrainerTable, TowerTrainerTable, PokemonInfo]

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
            if tree["m_Name"] == "TrainerTable":
                if p["r"]["trainers"]["items"]:
                    console.append(" - Randomizing trainer items.")
                    FieldTrainerItems.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Trainer items randomized.")

                if p["r"]["trainers"]["field"]:
                    console.append(" - Randomizing Pokémon for field trainers.")
                    FieldTrainers.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon for field trainers randomized.")

                if p["r"]["trainers"]["iv"] != 0:
                    console.append(" - Randomizing Pokémon IVs for field trainers.")
                    FieldTrainerIVs.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon IVs for field trainers randomized.")

                if p["r"]["trainers"]["ev"] != 0:
                    console.append(" - Randomizing Pokémon EVs for field trainers.")
                    FieldTrainerEVs.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon EVs for field trainers randomized.")

                if p["r"]["moves"]["trainers"]:
                    console.append(" - Randomizing Pokémon moves for field trainers.")
                    FieldTrainerMoves.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon moves for field trainers randomized.")

                if p["r"]["abilities"]["enc"]:
                    console.append(" - Randomizing Pokémon abilities for field trainers.")
                    FieldTrainerAbilities.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon abilities for field trainers randomized.")

                if p["r"]["helditems"]["enc"]:
                    console.append(" - Randomizing Pokémon held items for field trainers.")
                    FieldTrainerHeldItems.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon held items for field trainers randomized.")

                
                if p["level"]["decrease"] != 0 or p["level"]["increase"] != 0 or p["level"]["minimum"] != 1 or p["level"]["maximum"] != 100:
                    console.append(" - Altering trainers level.")
                    Level.alterTrainers(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Trainers level altered.")

                continue

            elif tree["m_Name"] == "TowerTrainerTable":
                if p["r"]["trainers"]["tower"]:
                    console.append(" - Randomizing Pokémon for tower trainers.")
                    TowerTrainers.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon for tower trainers randomized.")
                
                if p["r"]["trainers"]["iv"] != 0:
                    console.append(" - Randomizing Pokémon IVs for tower trainers.")
                    TowerTrainerIVs.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon IVs for tower trainers randomized.")

                if p["r"]["trainers"]["ev"] != 0:
                    console.append(" - Randomizing Pokémon EVs for tower trainers.")
                    TowerTrainerEVs.randomize(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon EVs for tower trainers randomized.")

                if p["r"]["moves"]["tower"]:
                    console.append(" - Randomizing Pokémon moves for tower trainers.")
                    TowerTrainerMoves.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon moves for tower trainers randomized.")

                if p["r"]["abilities"]["tower"]:
                    console.append(" - Randomizing Pokémon abilities for tower trainers.")
                    TowerTrainerAbilities.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon abilities for tower trainers randomized.")

                if p["r"]["helditems"]["tower"]:
                    console.append(" - Randomizing Pokémon held items for tower trainers.")
                    TowerTrainerHeldItems.randomize(tree)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon held items for tower trainers randomized.")

                continue

            elif tree["m_Name"] == "PokemonInfo":
                if p["scaling"] != 0:
                    console.append(" - Altering Pokémon size.")
                    Scale.alter(tree, p)
                    obj.save_typetree(tree)
                    console.append(" - Pokémon size altered.")
                continue
            else:
                console.append("ERROR: 'masterdatas' use different path ids")
                continue