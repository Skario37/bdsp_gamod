from Utils import File
from os import path, getcwd

filePath = "mods\\romfs\\Data\\StreamingAssets\\AssetAssistant\\Message"
ModPath = "StreamingAssets\\AssetAssistant\\Message"
SRC = "english"

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