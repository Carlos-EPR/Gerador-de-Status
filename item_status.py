from status_generator import status_generator

def item_status():

    stat = status_generator()

    if stat <= 80:
        rarity = "Bronze"
        stt = stat
    elif stat <= 130:
        rarity = "Silver"
        stt = stat
    elif stat <= 180:
        rarity = "Gold"
        stt = stat
    elif stat <= 220:
        rarity = "Emerald"
        stt = stat
    elif stat <= 260:
        rarity = "Diamond"
        stt = stat
    elif stat <= 300:
        rarity = "Ruby"
        stt = stat
    elif stat <= 350:
        rarity = "Obsidian"
        stt = stat
    else:
        rarity = "Opal"
        stt = stat

    return rarity, stt
       
'''effects = ["Raio", "Trovão", "Veneno", "Gelo", "Fogo", "Divino", "Mágico", "Sombras",
               "Arco-Íris", "Terra", "Plasma", "Tempestade", "Estelar", "Arcano"]'''