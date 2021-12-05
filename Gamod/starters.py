from Utils import File
from Randomizers import Starters
from os import path, getcwd

filePath = "mods\\exefs"

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
english_dp_scenario1 = -5307844841844767521
french_dp_scenario1 = -6796560385969472121
path_list = [english_dp_scenario1, french_dp_scenario1]

# Found in nso folder
Param_Starters = {
    "dBuildID": "D9E96FB92878E3458AAE7E8D31AB32A9",
    "pBuildID": "3C70CAE153DF0B4F8A7B24C60FD8D0E7",
    "dStarter1": "{:08X}".format(0x01FEAB28),
    "dStarter2": "{:08X}".format(0x01FEABB4),
    "dStarter3": "{:08X}".format(0x01FEABB8),
    "dRival1": "{:08X}".format(0x01FEAEA8),
    "dRival2": "{:08X}".format(0x01FEAF34),
    "dRival3": "{:08X}".format(0x01FEAF38),
    "pStarter1": "{:08X}".format(0x0238DEC8),
    "pStarter2": "{:08X}".format(0x0238DF54),
    "pStarter3": "{:08X}".format(0x0238DF58),
    "pRival1": "{:08X}".format(0x0238E248),
    "pRival2": "{:08X}".format(0x0238E2D4),
    "pRival3": "{:08X}".format(0x0238E2D8),
    "patch": {}
}

def save(console, patch):
    cwd = getcwd() 
    outputPath = path.join(cwd, filePath)
    File.gotoDir(outputPath)
    
    with open("diamondStarter.pchtxt", "w") as f:
        for e in patch["d"]:
            f.write(e + "\n")
    console.append(" ⮨ 'diamondStarter.pchtxt' saved.")

    with open("pearlStarter.pchtxt", "w") as f:
        for e in patch["p"]:
            f.write(e + "\n")
    console.append(" ⮨ 'pearlStarter.pchtxt' saved.")

    File.gotoDir(cwd)

def proceed(console, envs, p):
    console.append(" - Randomizing Starters.")
    Param_Starters["patch"] = Starters.randomize(Param_Starters, p)
    console.append(" - Starters randomized.")

    incorrect_path = True
    for env in envs: 
        if env:
            for obj in env.objects:
                if obj.path_id in path_list:
                    tree = obj.read_typetree()
                    if tree['m_Name'] == "french_dp_scenario1":
                        console.append("- Patching starter french message")
                        Starters.patchFrenchMessage(tree, Param_Starters["patch"]["m"])
                        obj.save_typetree(tree)
                        console.append("- Starter french message patched")

                        incorrect_path = False
                        continue
                    elif tree['m_Name'] == "english_dp_scenario1":
                        console.append("- Patching starter english message")
                        Starters.patchEnglishMessage(tree, Param_Starters["patch"]["m"])
                        obj.save_typetree(tree)
                        console.append("- Starter english message patched")
                        incorrect_path = False
                        continue

            if incorrect_path:
                console.append("ERROR: messages use different path ids")
                continue   

    return Param_Starters["patch"]    
                    