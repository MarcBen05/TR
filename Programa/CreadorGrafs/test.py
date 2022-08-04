import geocoder
from geopy.geocoders import Nominatim
import geotiler

"""
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("Sagrada Familia")
y = getLoc.latitude
x = getLoc.longitude

gc = geocoder.ip('me')
y,x = gc.latlng
#"""
"""
bbox = 2.1728,41.4051,2.1962,41.3905

#
# download map using OpenStreetMap
#

mm = geotiler.Map(extent=bbox, size=(1006, 749))
img = geotiler.render_map(mm)

#
# save map image as PNG file
#
img.save('ex-geocoder.png')
"""

Nomi_locator = Nominatim(user_agent="My App")

my_location= geocoder.ip('me')

#my latitude and longitude coordinates
latitude= my_location.geojson['features'][0]['properties']['lat']
longitude = my_location.geojson['features'][0]['properties']['lng']

#get the location
location = Nomi_locator.reverse(f"{latitude}, {longitude}")
print("Your Current IP location is", location)