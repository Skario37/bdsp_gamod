
from Utils import List, Pool
import math
import random

def patchFrenchMessage(tree, mons):
    monsName = List.getPokemonNames("french")
    tree['labelDataArray'][28]['wordDataArray'][2]['str'] = monsName[mons[0]]
    tree['labelDataArray'][29]['wordDataArray'][2]['str'] = monsName[mons[1]]
    tree['labelDataArray'][30]['wordDataArray'][2]['str'] = monsName[mons[2]]

def patchEnglishMessage(tree, mons):
    monsName = List.getPokemonNames("english")
    tree['labelDataArray'][28]['wordDataArray'][0]['str'] = 'Will you choose '
    tree['labelDataArray'][28]['wordDataArray'][2]['str'] = ''
    tree['labelDataArray'][28]['wordDataArray'][6]['str'] = monsName[mons[0]]
    tree['labelDataArray'][29]['wordDataArray'][0]['str'] = 'Will you choose '
    tree['labelDataArray'][29]['wordDataArray'][2]['str'] = ''
    tree['labelDataArray'][29]['wordDataArray'][6]['str'] = monsName[mons[1]]
    tree['labelDataArray'][30]['wordDataArray'][0]['str'] = 'Will you choose '
    tree['labelDataArray'][30]['wordDataArray'][2]['str'] = ''
    tree['labelDataArray'][30]['wordDataArray'][6]['str'] = monsName[mons[2]]

def randomize(ps, p):
    legList = List.getLegendaries()
    monsPool = Pool.getMons(p["gen"])
    monsNoLeg = Pool.Exclude(monsPool["mon"], monsPool["leg"])

    if p["leg"]:
        monLength = len(monsNoLeg)
        rMonID = random.sample(range(1, monLength + 1), 3)
        mon1 = monsNoLeg[rMonID[0]]
        mon2 = monsNoLeg[rMonID[1]]
        mon3 = monsNoLeg[rMonID[2]]
    else:
        monLength = len(monsPool)
        rMonID = random.sample(range(1, monLength + 1), 3)
        mon1 = monsPool[rMonID[0]]
        mon2 = monsPool[rMonID[1]]
        mon3 = monsPool[rMonID[2]]


    bits = 32
    enc1 = 128
    enc2 = 82
    enc3 = 256
    pos1 = 0
    pos2 = 8
    pos3 = 9
    sta1 = [
        (pos1+bits*mon1)%enc3, 
        math.floor((pos1+bits*mon1)/enc3),
        enc1,
        enc2
    ]
    sta2 = [
        (pos2+bits*mon2)%enc3, 
        math.floor((pos2+bits*mon2)/enc3),
        enc1,
        enc2
    ]
    sta3 = [
        (pos3+bits*mon3)%enc3, 
        math.floor((pos3+bits*mon3)/enc3),
        enc1,
        enc2
    ]
    riv1 = [
        (pos1+bits*mon2)%enc3, 
        math.floor((pos1+bits*mon2)/enc3),
        enc1,
        enc2
    ]
    riv2 = [
        (pos2+bits*mon3)%enc3, 
        math.floor((pos2+bits*mon3)/enc3),
        enc1,
        enc2
    ]
    riv3 = [
        (pos3+bits*mon1)%enc3, 
        math.floor((pos3+bits*mon1)/enc3),
        enc1,
        enc2
    ]

    pat1 = "".join(["{:02X}".format(b) for b in sta1])
    pat2 = "".join(["{:02X}".format(b) for b in sta2])
    pat3 = "".join(["{:02X}".format(b) for b in sta3])
    pat4 = "".join(["{:02X}".format(b) for b in riv1])
    pat5 = "".join(["{:02X}".format(b) for b in riv2])
    pat6 = "".join(["{:02X}".format(b) for b in riv3])
    
    dPatch = [
        "@nsobid-{}".format(ps["dBuildID"]),
        "",
        "@enabled",
        "{} {}".format(ps["dStarter1"], pat1),
        "{} {}".format(ps["dStarter2"], pat2),
        "{} {}".format(ps["dStarter3"], pat3),
        "{} {}".format(ps["dRival1"], pat4),
        "{} {}".format(ps["dRival2"], pat5),
        "{} {}".format(ps["dRival3"], pat6),
        ""
    ]

    pPatch = [
        "@nsobid-{}".format(ps["pBuildID"]),
        "",
        "@enabled",
        "{} {}".format(ps["dStarter1"], pat1),
        "{} {}".format(ps["dStarter2"], pat2),
        "{} {}".format(ps["dStarter3"], pat3),
        "{} {}".format(ps["dRival1"], pat4),
        "{} {}".format(ps["dRival2"], pat5),
        "{} {}".format(ps["dRival3"], pat6),
        ""
    ]
    
    return {
        "d": dPatch,
        "p": pPatch,
        "m": [mon1, mon2, mon3]
    }