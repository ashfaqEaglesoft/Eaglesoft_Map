from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource,MapMarker



class Eaglesoft_Map(App):


    def build(self):
        self.title="Eaglesoft Map"
        print(MapSource.providers.keys())
        box_layout=BoxLayout()
        map_view=MapView(lat=30.005630,lon=73.257950,zoom=8)
        map_view.map_source="osm"
        map_marker=MapMarker()
        map_marker.lat=30.005630
        map_marker.lon=73.257950
        map_marker.source="map-marker.png"
        map_view.add_widget(map_marker)
        box_layout.add_widget(map_view)
        return box_layout
if __name__ =='__main__':
    Eaglesoft_Map().run()
