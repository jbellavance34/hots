# idea : api for hots that return 3 choices for brawl style random but in custom games

# script to generate the json api data and writes do file named data.json
import json


def random_choices():
    # building the list of HOTS heroes
    # different list for all the types
    Bruisers = ['Artanis', 'Chen', 'DVa', 'Deathwing', 'Dehaka', 'Imperius', 'Leoric', 'Malthael', 'Ragnaros',
                 'Rexxar', 'Sonya', 'Thrall', 'Varian', 'Xul', 'Yrel']
    Healers = ['Alexstrasza', 'Ana', 'Anduin', 'Auriel', 'Brightwing', 'Deckard', 'Kharazim', 'LiLi', 'Morales',
                'Malfurion', 'Rehgar', 'Stukov', 'Tyrande', 'Uther', 'Whitemane', 'Lucio']
    Melee_Assasins = ['Alarak', 'Gazlowe', 'Illidan', 'Kerrigan', 'Maiev', 'Murky', 'Qhira', 'Samuro', 'Butcher',
                       'Valeera', 'Zeratul']
    Range_Assassins = ['Azmodan', 'Cassia', 'Chromie', 'Falstad', 'Fenix', 'Gall', 'Genji', 'Greymane', 'Guldan',
                        'Hanzo', 'Jaina', 'Junkrat', 'Kaelthas', 'KelThuzad', 'LiMing', 'Lunara', 'Mephisto',
                        'Nazeebo', 'Nova', 'Orphea', 'Probius', 'Raynor', 'Hammer', 'Sylvanas', 'Tracer',
                        'Tychus', 'Valla', 'Zagara', 'Zuljin']
    Supports = ['Abathur', 'Medivh', 'Tassadar', 'Vikings', 'Zarya']

    Tanks = ['Anubarak', 'Arthas', 'Blaze', 'Cho', 'Diablo', 'etc', 'Garrosh', 'Johanna', 'MalGanis', 'Muradin',
              'Stitches', 'Tyrael']




    # building all_heroes list with hero type
    all_heroes = []

    for bruiser in Bruisers:
        all_heroes.append(['bruiser', bruiser])
    for healer in Healers:
        all_heroes.append(['healer', healer])
    for melee_assasin in Melee_Assasins:
        all_heroes.append(['melee_assasin', melee_assasin])
    for range_assassin in Range_Assassins:
        all_heroes.append(['range_assassin', range_assassin])
    for support in Supports:
        all_heroes.append(['support', support])
    for tank in Tanks:
        all_heroes.append(['tank', tank])

    # adding information in the list
    # example https://www.hotsnerd.com/images/abathur.png

    output = []
    for hero in all_heroes:
        hero_type, hero_name = hero
        image_link = 'https://www.hotsnerd.com/images/' + hero_name.lower() + '.png'
        output.append(
            {
                'Name': hero_name,
                'Picture': image_link,
                'Type': hero_type
            }

        )

    return json.dumps(output)


if __name__ == "__main__":
    json_data = random_choices()
    # Writing to data.json
    with open("data.json", "w") as outfile:
        outfile.write(json_data)