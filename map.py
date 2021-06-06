import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"]) 
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer():
    elevation = 0
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[lat, lon],zoom_start=20,tiles= "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat,lon,elev):       # zip()-- returns both of the values in opposite side(i.e it distributes the items none by one )
    fgv.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup =str(el)+" mtr",
    fill_color = color_producer(el), color='grey',fill=True, fill_opacity= 0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-08-sig'),
style_function=lambda x: {'fill_color':'green' if x['properties']['POP2005']<10000000
else 'orange' if 1000000 <= x['properties']['POP2001'] <2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map.html")
