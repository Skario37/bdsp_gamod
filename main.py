from Randomizers import Encounters, EncounterMoves, EncounterAbilities, UndergroundEncounters, Evolutions, Trainers, IV, EV, TrainerMoves, TrainerAbilities, TrainerHeldItems, EncounterHeldItems, Types, TrainerItems#Levels, Shop, TM, Starters
from Utils import Pool
import sys

romFSPath = sys.argv[1]

paramList = {
    "v": False, # Latest
    "g": [],
    "pool": {},
    "r": {
        "s": {
            "leg": False
        },
        "starter": False,
        "encount": False,
        "underground_encount": False,
        "trainer_poke": False,
        "trainer_iv": False,
        "trainer_ev": False,
        
        "trainer_abilities": False,
        "evolutions": False,
        "moves": False,
        "abilities": False,
        "type": False,
        "held_items": False,
        "trainer_items": False
    },
    "u": {}
}

def letsGo():
    if paramList["r"]["encount"]:
        Encounters.Encount(paramList, romFSPath)
    if paramList["r"]["underground_encount"]:
        UndergroundEncounters.Encount(paramList, romFSPath)
    
    if paramList["r"]["trainer_poke"]:
        Trainers.Trainer(paramList, romFSPath)
    if paramList["r"]["trainer_iv"]:
        IV.IV(paramList, romFSPath)
    if paramList["r"]["trainer_ev"]:
        EV.EV(paramList, romFSPath)

    if paramList["r"]["evolutions"]:
        Evolutions.Evolution(paramList, romFSPath)

    if paramList["r"]["moves"] == "1" or paramList["r"]["moves"] == "3":
        EncounterMoves.Move(paramList, romFSPath)
    if paramList["r"]["moves"] == "2" or paramList["r"]["moves"] == "3":
        TrainerMoves.Move(paramList, romFSPath)

    if paramList["r"]["abilities"] == "1" or paramList["r"]["abilities"] == "3":
        EncounterAbilities.Ability(paramList, romFSPath)
    if paramList["r"]["abilities"] == "2" or paramList["r"]["abilities"] == "3":
        TrainerAbilities.Ability(paramList, romFSPath)

    if paramList["r"]["types"] == "1":
        Types.Type(paramList, romFSPath)
    
    if paramList["r"]["held_items"] == "1" or paramList["r"]["held_items"] == "3":
        EncounterHeldItems.HeldItem(paramList, romFSPath)
    if paramList["r"]["held_items"] == "2" or paramList["r"]["held_items"] == "3":
        TrainerHeldItems.HeldItem(paramList, romFSPath)

    if paramList["r"]["trainer_items"]:
        TrainerItems.Item(paramList, romFSPath)

    return

def user_confirm(m):
    if input(m) in ["y", "Y", "yes", "Yes", "YES"]: return True
    else: return False

def user_choice(m,c):
    a = input(m)
    if a in c: return a
    else: return False 


paramList["v"] = user_choice("Select Version\n ➥ 0 - Latest default\n ➥ 1 - 1.0.0 (not tested)\n ➥ 2 - 1.1.0 (not tested)\n : ", ["1","2"])

print("Choose generations:")
if user_confirm(" ➥ All (y/n): "):
    paramList["g"].append(1)
    paramList["g"].append(2)
    paramList["g"].append(3)
    paramList["g"].append(4)
else:
    if user_confirm(" ➥ Generation 1 (y/n): "): paramList["g"].append(1)
    if user_confirm(" ➥ Generation 2 (y/n): "): paramList["g"].append(2)
    if user_confirm(" ➥ Generation 3 (y/n): "): paramList["g"].append(3)
    if user_confirm(" ➥ Generation 4 (y/n): "): paramList["g"].append(4)
paramList["pool"] = Pool.Pool(paramList["g"])

print("Randomize Pokémon:")
paramList["r"]["s"]["leg"] = user_confirm(" ➥ Keep legendaries as legendaries (y/n): ")
paramList["r"]["encount"] = user_confirm(" ➥ Encounters (y/n): ")
paramList["r"]["underground_encount"] = user_confirm(" ➥ Underground (y/n): ")
paramList["r"]["trainer_poke"] = user_confirm(" ➥ Trainers (y/n): ")
paramList["r"]["trainer_iv"] =  user_choice("   ➥ 0 - default\n   ➥ 1 - Randomize IV's\n   ➥ 2 - Maximize IV's\n   : ", ["1", "2"])
paramList["r"]["trainer_ev"] = user_choice("   ➥ 0 - default\n   ➥ 1 - Randomize EV's\n   ➥ 2 - Maximize EV's\n   : ", ["1", "2"])
paramList["r"]["evolutions"] = user_confirm("Randomize evolutions (y/n): ")
paramList["r"]["moves"] = user_choice("Randomize moves:\n ➥ 0 - default\n ➥ 1 - Only encounters\n ➥ 2 - Only trainers\n ➥ 3 - Both encounters and trainers\n : ", ["1", "2","3"])
paramList["r"]["abilities"] = user_choice("Randomize abilities:\n ➥ 0 - default\n ➥ 1 - Only encounters\n ➥ 2 - Only trainers\n ➥ 3 - Both encounters and trainers\n : ", ["1", "2","3"])
paramList["r"]["types"] = user_choice("Pokémon types:\n ➥ 0 - default\n ➥ 1 - Randomize\n ➥ 2 - Coming soon\n : ", ["1"])
paramList["r"]["held_items"] = user_choice("Randomize held items:\n ➥ 0 - default\n ➥ 1 - Only encounters\n ➥ 2 - Only trainers\n ➥ 3 - Both encounters and trainers\n : ", ["1", "2","3"])
paramList["r"]["trainer_items"] = user_confirm("Randomize items that trainers can use (y/n): ")

letsGo()