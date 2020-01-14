from PIL import Image
import os
import sys
import webcolors
import matplotlib.pyplot as plt

class Photo:

    PATH = "img\\"

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.colors = {}
        self.img = self.setImage()
        self.pixels = self.getPixels()

    def setImage(self):
        return Image.open(self.PATH + self.name, "r")

    def getPixels(self):
        if self.img == None:
            return None
        return list(self.img.getdata())

    def getColors(self):
        i = 0
        for pixel in self.pixels:
            color = self.getColorName(pixel)[1] if self.getColorName(pixel)[0] == None else self.getColorName(pixel)[1]  
            if color in self.colors.keys():
                self.colors[color] += 1
            else:
                self.colors[color] = 0
            i += 1
            print(round(i / len(self.pixels) * 100), '% effectués')
            
    def closestColor(self, pixel):
        min_colours = {}
        for key, name in webcolors.css3_hex_to_names.items():
            r, g, b = webcolors.hex_to_rgb(key)
            rd = (r - pixel[0]) ** 2
            gd = (g - pixel[1]) ** 2
            bd = (b - pixel[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    def getColorName(self, pixel):
        try:
            closest_name = actual_name = webcolors.rgb_to_name(pixel)
        except ValueError:
            closest_name = self.closestColor(pixel)
            actual_name = None
        return actual_name, closest_name

    def renderGraph(self):
        labels = self.colors.keys()
        sizes = self.colors.values()
        colors = self.colors.keys()
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()




path = '' #C:\\Users\\{username}\\...
photos = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            photos.append(Photo(file))

for photo in photos:
    photo.getColors()
    photo.renderGraph()
    sys.exit()
