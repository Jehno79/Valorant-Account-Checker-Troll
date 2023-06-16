import time, random, os

ranksettings = True
levelsettings = True

choice = ["locked", "bronze", "silver", "gold", "platine", "diamond", "immortal", "radiant"]

rank = {'locked': 0, 'bronze': 0, 'silver': 0, 'gold': 0, 'platine': 0, 'diamond': 0, 'immortal': 0, 'radiant': 0}

level = {'0-20': 0, '20-40': 0, '40-60': 0, '60-80': 0, '100-max': 0}

case = input("Valorant Fake checker\n\n[1] Start Checking\n[2] Checker Settings\n> ")

if case == "1" and ranksettings == True:
  while True:
    time.sleep(1)
    choice1 = random.choice(choice)
    os.system('clear')
    rank[choice1] = rank[choice1] + 1
    case = rank["locked"]
    case2 = rank["bronze"]
    case3 = rank["silver"]
    case4 = rank["gold"]
    case5 = rank["platine"]
    case6 = rank["diamond"]
    case7 = rank["immortal"]
    case8 = rank["radiant"]
    f = open("account.txt", "w")
    f.write(f"Locked [{case}]    Gold      [{case4}]    Immortal [{case7}]\nBronze [{case2}]    platinium [{case5}]    Radiant  [{case8}]\nSilver [{case3}]    Diamond   [{case6}]")
    f.close()
    print(f"Locked [{case}]    Gold      [{case4}]    Immortal [{case7}]\nBronze [{case2}]    platinium [{case5}]    Radiant  [{case8}]\nSilver [{case3}]    Diamond   [{case6}]")
