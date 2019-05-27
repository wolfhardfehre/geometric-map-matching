from shapely.geometry import Point


class Waypoint(Point):
    def __init__(self, id, lat, lon):
        super().__init__(float(lon), float(lat))
        self.id = int(id)
