import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[lat, lon],zoom_start=20,tiles= "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat,lon):       # zip()-- returns both of the values in opposite side(i.e it distributes the items none by one )
    fg.add_child(folium.Marker(location = [lt,ln], popup ="Work", icon= folium.Icon(color="blue")))
map.add_child(fg)
map.save("map.html")