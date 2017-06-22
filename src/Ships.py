Sclass = ['Scout', 'Frigate', 'Crusier', 'Carrier', 'Destroyer', 'BattleCrusier', 'Battleship']
ShipInfo = {}


def init():
    for ship in Sclass:
        ShipInfo[ship] = {"Desc": "This is a ship... with stats in it! It the ship of wisdom!"
                                  "Just in time for the islamic golden age!", "Resources": {'Ores': 50, 'Energy': 10}}
    print('Finished ShipsInit')
