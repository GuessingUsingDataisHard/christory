from data import Game
import pandas as pd
import numpy as np

class TurnHandler:
    pass


class CivInitializer:
    def generate_spawn_position(self):
        while True:
            civ_total = len(Game.civs.index)
            spawns_x = np.sort(np.random.randint(0, 800, size=civ_total))
            spawns_y = np.sort(np.random.randint(0, 400, size=civ_total))
            #TEst this plsss my uhh whats it called umm VS didnt work for some reason have 2 reinstall LOL!
            SpawnHolder = {
                "X": spawns_x,
                "Y": spawns_y
            }
            spawns = pd.DataFrame(SpawnHolder)
            #Thsi makes a new uhh wastrhey called thingy thingy SHEET thats what its called but uhh it works (: also idk might delete stuff oh Im going through a tunnel goodbye
            #Also uhh change this name IDK what the files called (:
            with pd.ExcelWriter('Christory.xlsx',mode='a') as writer:  
                spawns.to_excel(writer, sheet_name='Spawns')

        return spawns

