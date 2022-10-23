import geocoder
import geotiler
import geopy
from PIL import Image, ImageDraw

ip = geocoder.ip('me')
print(ip.city)
print(ip.latlng)

coord = (ip.latlng[1], ip.latlng[0])

map = geotiler.Map(center=coord, size=(1006,746), zoom=15)

img = geotiler.render_map(map)
img.save('map_i_got.png')