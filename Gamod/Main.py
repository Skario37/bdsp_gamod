from Gamod import personal_masterdatas, gamesettings, masterdatas, ugdata, starters
from Gamod.message import french, english
from Randomizers import Evolutions, Types, EggMoves, EggGroups, EncounterMoves, EncounterAbilities

# PathIDs inside Unity
# DO NOT CHANGE UNLESS GAME IS UPDATED
def Main(console, p):
    pm_env = getPersonalMasterdatasEnv(console, p)
    gs_env = getGameSettingsEnv(console, p)
    md_env = getMasterDatasEnv(console, p)
    ug_env = getUndergroundDataEnv(console, p)
    msg_envs = getMessageEnvs(console, p)

    if pm_env: 
        personal_masterdatas.proceed(console, pm_env, p)
        personal_masterdatas.save(console, pm_env)
    if gs_env: 
        gamesettings.proceed(console, gs_env, p)
        gamesettings.save(console, gs_env)
    if md_env: 
        masterdatas.proceed(console, md_env, p)
        masterdatas.save(console, md_env)
    if ug_env: 
        ugdata.proceed(console, ug_env, p)
        ugdata.save(console, ug_env)

    if msg_envs: 
        starter_patch = starters.proceed(console, msg_envs, p)
        starters.save(console, starter_patch)
        if msg_envs[0]: english.save(console, msg_envs[0])
        if msg_envs[1]: french.save(console, msg_envs[1])

    return

def getPersonalMasterdatasEnv(console, p):
    if p["r"]["evolutions"] or p["r"]["types"] or p["r"]["eggmoves"] or p["r"]["egggroups"] or p["r"]["moves"]["enc"] or p["r"]["abilities"]["enc"] or p["r"]["helditems"]["enc"]:
        return personal_masterdatas.load(console, p["romfspath"])
    return False

def getGameSettingsEnv(console, p):
    if p["r"]["enc"]["field"] or p["r"]["enc"]["safari"] or p["level"]["decrease"] != 0 or ["level"]["increase"] != 0 or p["level"]["minimum"] != 1 or p["level"]["maximum"] != 100:
        return gamesettings.load(console, p["romfspath"])
    return False

def getMasterDatasEnv(console, p):
    if p["r"]["trainers"]["items"] or p["r"]["trainers"]["field"] or p["r"]["trainers"]["tower"] or p["r"]["trainers"]["iv"] != 0 or p["r"]["trainers"]["ev"] != 0 or p["r"]["moves"]["trainers"] or p["r"]["moves"]["tower"] or p["r"]["abilities"]["trainers"] or p["r"]["abilities"]["tower"] or p["r"]["helditems"]["trainers"] or p["r"]["helditems"]["tower"] or p["scaling"] != 0 or p["level"]["decrease"] != 0 or ["level"]["increase"] != 0 or p["level"]["minimum"] != 1 or p["level"]["maximum"] != 100:
        return masterdatas.load(console, p["romfspath"])
    return False

def getUndergroundDataEnv(console, p):
    if p["r"]["enc"]["underground"] or p["level"]["decrease"] != 0 or ["level"]["increase"] != 0 or p["level"]["minimum"] != 1 or p["level"]["maximum"] != 100:
        return gamesettings.load(console, p["romfspath"])
    return False

def getMessageEnvs(console, p):
    if p["r"]["starters"]:
        envs = []
        envs.append(english.load(console, p["romfspath"])) 
        envs.append(french.load(console, p["romfspath"])) 

        return envs
    return False