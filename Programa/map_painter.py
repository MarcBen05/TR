import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

class MapPainter:
    def __init__(self):
        self.points = []
        self.image = Image.open('map.png', 'r')

        #Al index 0, aquestes son les coordenades del punt superior esquerra de l'imatge
        self.lat = [41.4051,41.3905]
        self.lon = [2.1728,2.1962]

    def coord_to_img(self, x, y):
        #https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set/33445
        x_conv = abs(((x-self.lat[0])/(self.lat[1]-self.lat[0]))*(self.image.size[0]))
        y_conv = ((y-self.lon[0])/(self.lon[1]-self.lon[0]))*(self.image.size[1])

        print(f"Latitud: {x}; Longitud: {y} -> x: {x_conv}, y: {y_conv}")

        return x_conv, y_conv

    def img_to_coord(self, x, y):
        #https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set/33445
        #Result := ((Input - InputLow) / (InputHigh - InputLow)) * (OutputHigh - OutputLow) + OutputLow;
        
        x_conv = abs(((x-0)/(1006-0))*(self.lat[1]-self.lat[0])+self.lat[0])
        y_conv = ((y-0)/(749-0))*(self.lon[1]-self.lon[0])+self.lon[0]

        print(f"x: {x}; y: {y} -> Latitud: {x_conv}, Longitud: {y_conv}")

        return x_conv, y_conv

    def insert_into_route(self, x, y):
        self.points.append(self.coord_to_img(x, y))

    def paint_map(self):
        draw = ImageDraw.Draw(self.image)
        draw.line(self.points, fill=(255, 0, 0), width=2)
        self.image.save('result_Map.png')