from os import path, makedirs, chdir
import UnityPy
import os

def load(inputPath, src):
    if path.exists(path.join(inputPath)) and path.isfile(path.join(inputPath, src)):
        return UnityPy.load(path.join(inputPath, src))
    else: return False

def write(src, env):
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))

def gotoDir(outputPath):
    if not path.exists(outputPath):
        makedirs(outputPath, 0o666)
    chdir(outputPath)