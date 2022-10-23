from xml.etree.ElementTree import parse
from PIL import Image, ImageDraw
from numpy import interp
#import geotiler

def get_bbox(data):
    for b in data.iterfind('bounds'):
        return float(b.attrib['minlon']), float(b.attrib['minlat']), float(b.attrib['maxlon']),float(b.attrib['maxlat'])

def get_map(data):
    bbox = get_bbox(data)
   
    #map = geotiler.Map(extent=bbox, size=(1006,746))

    #img = geotiler.render_map(map)
    #img.save('map.png')

def coord_to_img(x, y, data, image) -> tuple[float,float]:
    bbox = get_bbox(data)
    minLon, minLat, maxLon, maxLat = bbox

    #print(bbox)

    yPixel = interp(y,[minLat,maxLat],[0,image.size[1]])
    xPixel = interp(x,[minLon,maxLon], [0,image.size[0]])

    return xPixel,yPixel

data = parse('map.osm')

ways = [] #LLista de llistes de IDs de nodes

for item in data.iterfind('way'):
    way = []
    for j in item.iterfind('tag'):
        if j.attrib['k'] == 'highway':
            for i in item.iterfind('nd'):
                way.append(i.attrib["ref"])
    ways.append(way)

visited_nodes = {} # id -> bool (visitat)
cross_nodes = [] # llista de nodes que coincideixen en diversos camins

for way in ways:
    for pt in way:
        if int(pt) in visited_nodes.keys():
           cross_nodes.append(int(pt))
        else:
            visited_nodes[int(pt)] = True

cross_coords = []

index = 1

for id in cross_nodes:
    if index > 11:
        break
    for item in data.iterfind('node'):
        if item.attrib['id'] == str(id):
            cross_coords.append((float(item.attrib['lon']),float(item.attrib['lat'])))
            index += 1

r = 5
index = 1

if not cross_coords:
    print("ERROR OCCURED: Coordinate list is empty!")

print("Starting painting crossings...")
img = Image.open('map.png', 'r')

for pos in cross_coords:

    imgPos = coord_to_img(pos[0], pos[1], data, img)
    x,y = imgPos
    print(x,y)

    draw = ImageDraw.Draw(img)
    draw.ellipse((x-r,y-r,x+r,y+r),fill="red")
    img.save('test_map1.png')

    img = Image.open('test_map1.png', 'r')

    if index % 20 == 0:
        print(f"\tJust finished a batch. Number of finished positions: {index}")

    index += 1