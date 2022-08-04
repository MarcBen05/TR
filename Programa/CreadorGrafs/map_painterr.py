from PIL import Image, ImageDraw
import math

class MapPainter:
    def __init__(self, map_path='map.png'):
        self.points = []
        self.image = Image.open(map_path, 'r')

        #Al index 0, aquestes son les coordenades del punt superior esquerra de l'imatge
        self.lat = [41.4070,41.3888]
        self.lon = [2.1636,2.1974]

    def set_map(self, map_path):
        self.image = Image.open(map_path, 'r')

    def coord_to_img(self, x: float, y:float ) -> tuple[float,float]:
        #https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set/33445
        #x_conv = abs(((x-self.lat[0])/(self.lat[1]-self.lat[0]))*(self.image.size[0]))
        x_conv = (x-self.lat[1])/(self.lat[0]-self.lat[1])*self.image.size[0]
        y_conv = ((y-self.lon[0])/(self.lon[1]-self.lon[0]))*(self.image.size[1])

        return x_conv, y_conv

    def img_to_coord(self, x: float, y: float) -> tuple[float,float]:
        #https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set/33445
        #Result := ((Input - InputLow) / (InputHigh - InputLow)) * (OutputHigh - OutputLow) + OutputLow;
        
        x_conv = ((x-0)/(1006-0))*(self.lat[0]-self.lat[1])+self.lat[1]
        y_conv = ((y-0)/(749-0))*(self.lon[1]-self.lon[0])+self.lon[0]

        return x_conv, y_conv

    def insert_into_route_coord(self, x: float, y: float):
        self.points.append(self.coord_to_img(x, y))

    def insert_into_route(self, x: float, y: float):
        self.points.append((x,y))

    def set_route(self, route):
        self.points = route

    def paint_map(self, save_path='result_Map.png', color=(255,0,0)):
        draw = ImageDraw.Draw(self.image)
        draw.line(self.points, fill=color, width=2)
        lastP = self.points.pop()
        scndToLast = self.points.pop()
        ###
        x0, y0 = scndToLast
        x1, y1 = lastP
        # Now we can work out the x,y coordinates of the bottom of the arrowhead triangle
        xb = 0.8*(x1-x0)+x0
        yb = 0.8*(y1-y0)+y0

        # Work out the other two vertices of the triangle
        # Check if line is vertical
        if x0==x1:
            vtx0 = (xb-5, yb)
            vtx1 = (xb+5, yb)
        # Check if line is horizontal
        elif y0==y1:
            vtx0 = (xb, yb+5)
            vtx1 = (xb, yb-5)
        else:
            alpha = math.atan2(y1-y0,x1-x0)-90*math.pi/180
            a = 8*math.cos(alpha)
            b = 8*math.sin(alpha)
            vtx0 = (xb+a, yb+b)
            vtx1 = (xb-a, yb-b)
        draw.polygon([vtx0, vtx1, lastP], fill=color)
        ###
        self.image.save(save_path)

    def paint_map_route(self, route):
        draw = ImageDraw.Draw(self.image)
        i = 0
        for p in route:
            draw.line(p, fill=(255,0,0), width=2)
            i += 1
        
        self.image.save(f"result_Map.png")

    
    def paint_points(self, pos: tuple[float,float], r: int):
        x,y = pos
        draw = ImageDraw.Draw(self.image)
        draw.ellipse((x-r,y-r,x+r,y+r),fill="blue")
        self.image.save('test_map.png')

"""
p = MapPainter()

for i in range(0, 14):
    if i == 11:
        continue

    x, y = p.img_to_coord(130+i*69, 7)
    p.insert_into_route(x, y)

p.paint_map()
"""