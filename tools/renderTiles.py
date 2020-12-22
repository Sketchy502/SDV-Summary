""" All credit to this code goes to Joel Teichroeb (klusark) on Github, https://github.com/klusark/"""

from PIL import Image
from PIL.ImageChops import offset
import os
from math import floor


def cropImg(img, location, size, tileSize):
    y = (location // size[0]) * tileSize[1]
    x = (location % size[0]) * tileSize[0]
    return offset(img, -x, -y).crop((0, 0, tileSize[0], tileSize[1]))


def pasteImg(img, tile, location, size, tileSize):
    y = (location // size[0]) * tileSize[1]
    x = (location % size[0]) * tileSize[0]
    img.paste(tile, (x, y))


def weighted_average(array, sensitivity=1):
    s = 0
    for i in range(len(array)):
        s += i * array[i]
    if sum(array) != 0:
        s /= sum(array)
        s = floor(s / sensitivity) * sensitivity
        return floor(s)
    else:
        return 0


class TileMap:
    def __init__(self, mapName):
        self.mapPath = mapName

    def readInt(self, buf):
        return int.from_bytes(buf.read(4), byteorder="little")

    def readByte(self, buf):
        data = buf.read(1)
        return int.from_bytes(data, byteorder="little")

    def readString(self, buf):
        length = self.readInt(buf)
        return buf.read(length).decode("utf-8")

    def readCustomSections(self, buf):
        numCustomSections = self.readInt(buf)

        for j in range(numCustomSections):
            sectionName = self.readString(buf)
            sectionType = self.readByte(buf)
            if sectionType == 0:
                sectionValye = self.readByte(buf)
            elif sectionType == 3:
                sectionValue = self.readString(buf)
            else:
                pass

    def getTile(self, buf, isAnim=False):
        tileType = self.readByte(buf)
        if tileType == ord("N"):
            skip = self.readInt(buf)
            self.pos += skip
        elif tileType == ord("S"):
            tile = self.readInt(buf)
            self.tiles.append(
                {"tileset": self.currentTileset, "tile": tile, "pos": self.pos}
            )
            unk = self.readByte(buf)  # ?
            if isAnim:
                if self.animationFramesLeft == 0:
                    self.readInt(buf)
            self.readCustomSections(buf)
            if self.animationFramesLeft != 0:
                self.animationFramesLeft -= 1
                self.getTile(buf, True)
            if not isAnim:
                self.pos += 1
        elif tileType == ord("T"):
            self.currentTileset = self.readString(buf)
        elif tileType == ord("A"):
            frameDelay = self.readInt(buf)
            animFrames = self.readInt(buf)
            self.animationFramesLeft = animFrames - 1
            return False
        else:
            pass
        return True

    def processData(self):
        buf = open(self.mapPath, "rb")
        tBIN10 = buf.read(6)
        name = self.readString(buf)
        self.readInt(buf)  # ?
        self.readCustomSections(buf)

        self.tilesets = {}

        numTilesets = self.readInt(buf)
        for i in range(numTilesets):
            tilesetName = self.readString(buf)

            self.readInt(buf)  # ?
            sheetName = self.readString(buf)

            # num tiles
            tilesWide = self.readInt(buf)
            tilesHigh = self.readInt(buf)

            # size of each tile
            tileWidth = self.readInt(buf)
            tileHeight = self.readInt(buf)

            marginX = self.readInt(buf)  # ?
            marginY = self.readInt(buf)  # ?

            spacingX = self.readInt(buf)  # ?
            spacingY = self.readInt(buf)  # ?

            self.readCustomSections(buf)

            self.tilesets[tilesetName] = {
                "width": tilesWide,
                "height": tilesHigh,
                "tileWidth": tileWidth,
                "tileHeight": tileHeight,
                "sheetName": sheetName,
                "tileCache": {},
            }

        self.layers = []
        self.currentTileset = ""
        numLayers = self.readInt(buf)
        for i in range(numLayers):
            layerName = self.readString(buf)
            self.readInt(buf)  # ?
            self.readByte(buf)  # ?
            layerWidth = self.readInt(buf)
            layerHeight = self.readInt(buf)
            tileWidth = self.readInt(buf)
            tileHeight = self.readInt(buf)

            self.readCustomSections(buf)

            self.pos = 0
            self.tiles = []

            self.animationFramesLeft = 0
            while self.pos < layerWidth * layerHeight:

                while self.pos < layerWidth * layerHeight:
                    ret = self.getTile(buf)
                    if not ret:
                        break
            self.layers.append(
                {
                    "name": layerName,
                    "width": layerWidth,
                    "height": layerHeight,
                    "tileWidth": tileWidth,
                    "tileHeight": tileHeight,
                    "tiles": self.tiles,
                }
            )

    def renderData(self, outdir, seasonName):
        tilesetDir = os.path.dirname(self.mapPath)
        for layer in self.layers:
            print("\tRendering layer", layer["name"])
            img = Image.new(
                "RGBA",
                (
                    layer["width"] * layer["tileWidth"],
                    layer["height"] * layer["tileHeight"],
                ),
            )
            for tile in layer["tiles"]:
                tileset = self.tilesets[tile["tileset"]]
                if not "img" in tileset:
                    sheetName = tileset["sheetName"]
                    if seasonName:
                        sheetName = sheetName.replace("spring", seasonName)
                    tileset["img"] = Image.open(
                        os.path.join(tilesetDir, sheetName + ".png")
                    )

                if not tile["tile"] in tileset["tileCache"]:
                    tileImg = cropImg(
                        tileset["img"],
                        tile["tile"],
                        (tileset["width"], tileset["height"]),
                        (16, 16),
                    )
                    tileset["tileCache"][tile["tile"]] = tileImg
                else:
                    tileImg = tileset["tileCache"][tile["tile"]]
                pasteImg(
                    img,
                    tileImg,
                    tile["pos"],
                    (layer["width"], layer["height"]),
                    (16, 16),
                )
            img.save(os.path.join(outdir, layer["name"] + ".png"))

    def renderMinimap(self, outdir, name):
        tiles = []

        src_location = os.getcwd() + os.path.join(
            os.path.sep, "assets", "spring_outdoorsTileSheet.png"
        )
        assets = Image.open(src_location)
        assets.crop((336, 784, 352, 800))
        colour_pallet = Image.open("sample.png")

        # Flatten layers as miniamp only has base
        for layer in self.layers:
            for tile in layer["tiles"]:
                tiles.append(tile)

        # Count frequency of used tiles and rough colouring of tiles
        img = Image.new("RGB", (layer["width"], layer["height"]))
        i = img.load()
        for tile in tiles:
            x = int(tile["pos"]) % int(layer["width"])
            y = int(tile["pos"]) / int(layer["width"])
            pallet_x = int(tile["tile"] % 25)
            pallet_y = int(tile["tile"] / 25)
            i[x, y] = colour_pallet.getpixel((pallet_x, pallet_y))
        img.resize((layer["width"] * 8, layer["height"] * 8)).save(name + ".png")
