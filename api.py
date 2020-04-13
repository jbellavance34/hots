# idea : api for hots that return 3 choices for brawl style random but in custom games

from flask import request
from flask_api import FlaskAPI, status
import random
import json
from bs4 import BeautifulSoup
import urllib.request

app = FlaskAPI(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def random_choices():
    # building the list of HOTS heroes
    # different list for all the types
    Bruisers = ['Artanis', 'Chen', 'D.Va', 'Deathwing', 'Dehaka', 'Imperius', 'Leoric', 'Malthael', 'Ragnaros',
                 'Rexxar', 'Sonya', 'Thrall', 'Varian', 'Xul', 'Yrel']
    Healers = ['Alexstrasza', 'Ana', 'Anduin', 'Auriel', 'Brightwing', 'Deckard', 'Kharazim', 'LiLi', 'Lt.Morales',
                'Malfurion', 'Rehgar', 'Stukov', 'Tyrande', 'Uther', 'Whitemane']
                # TODO: Fix 'Lúcio'
    Melee_Assasins = ['Alarak', 'Gazlowe', 'Illidan', 'Kerrigan', 'Maiev', 'Murky', 'Qhira', 'Samuro', 'The Butcher',
                       'Valeera', 'Zeratul']
    Range_Assassins = ['Azmodan', 'Cassia', 'Chromie', 'Falstad', 'Fenix', 'Gall', 'Genji', 'Greymane', 'Guldan',
                        'Hanzo', 'Jaina', 'Junkrat', 'Kael%27thas', 'Kel%27Thuzad', 'Li - Ming', 'Lunara', 'Mephisto',
                        'Nazeebo', 'Nova', 'Orphea', 'Probius', 'Raynor', 'Sgt.Hammer', 'Sylvanas', 'Tracer',
                        'Tychus', 'Valla', 'Zagara', 'Zul%27jin']
    Supports = ['Abathur', 'Medivh', 'Tassadar', 'The Lost Vikings', 'Zarya']

    Tanks = ['Anub%27arak', 'Arthas', 'Blaze', 'Cho', 'Diablo', 'E.T.C.', 'Garrosh', 'Johanna', 'Mal%27Ganis', 'Muradin',
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

    # shuffle the heroes
    random.shuffle(all_heroes)

    # adding information in the list
    # example https://heroesofthestorm.gamepedia.com/File:ArtanisArt.jpg

    output = []
    # we only take 3 firsts
    for hero in all_heroes[:3]:
        hero_type, hero_name = hero

        ArtEnding = 'Art.jpg'

        # fixing bugging names
        if hero_name == 'Li - Ming':
            hero_name = 'Li-Ming'
        if hero_name == 'The Butcher':
            hero_name = 'Butcher'
        if hero_name == 'The Lost Vikings':
            hero_name = 'LostVikings'
        if hero_name == 'D.Va':
            hero_name = 'DVa'
        if hero_name == 'E.T.C.':
            hero_name = 'Etc'
        if hero_name == 'Lt.Morales':
            hero_name = 'Medic'
        if hero == 'Nazeebo':
            hero_name = 'WitchDoctor'
        if hero_name == 'Sgt.Hammer':
            hero_name = 'SgtHammer'
        if hero_name == 'Cho' or hero_name == 'Gall':
            hero_name = 'Cho%27gall'
        if hero_name == 'Kharazim':
            hero_name = 'Monk'
        # fixing Art ending
        if hero_name == 'Qhira':
            ArtEnding = '_artwork.jpg'
        if hero_name == 'Malthael':
            ArtEnding = '.jpg'
        if hero_name == 'Yrel' or hero_name == 'Ragnaros' or hero_name == 'Whitemane' or hero_name == 'Mephisto':
            ArtEnding = 'Art.png'

        url = ('https://heroesofthestorm.gamepedia.com/File:' + hero_name + ArtEnding)
        try:
            response = urllib.request.urlopen(url, timeout=30)
            html_doc = response.read()
        except Exception as E:
            print("Failed to fetch site :" + url + ", error:" + str(E))
        else:
            # parsing the html information
            soup = BeautifulSoup(html_doc, 'html.parser')
            file_list = soup.find_all('div', attrs={"id": "file"})
            all_links = file_list[0].find_all('a', href=True)
            image_link = all_links[0]['href']

            output.append(
                {
                    'Name': hero_name,
                    'Picture': image_link,
                    'Type': hero_type
                }

            )

    return json.dumps(output)




app.run()