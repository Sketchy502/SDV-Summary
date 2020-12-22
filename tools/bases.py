import os

from tools.renderTiles import TileMap

base_path = os.getcwd() + os.path.join(os.path.sep, "sdv", "assets")


def generateBase(assets, mapData, season, type):
    tileMap = TileMap(mapData)
    tileMap.processData()
    dest = os.path.join("base", type, season)
    tileMap.renderData(os.path.join(base_path, dest), season)
    if season == "spring":
        tileMap.renderMinimap(os.path.join(base_path, dest), type)


def generateBases():
    types = ["Combat", "Fishing", "Foraging", "Mining", "default", "FourCorners"]

    seasons = ["spring", "summer", "fall", "winter"]

    for season in seasons:
        for type in types:
            print(type, season)
            if type == "default":
                farm = "Farm.tbin"
            else:
                farm = "Farm_{0}.tbin".format(type)
            dataLoc = os.getcwd() + os.path.join(os.path.sep, "assets", "Maps", farm)
            generateBase(None, dataLoc, season, type)


if __name__ == "__main__":
    generateBases()
