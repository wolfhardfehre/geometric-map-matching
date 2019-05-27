import numpy as np
from shapely.geometry import Point
from shapely.geometry import LineString


class Edge:
    def __init__(self, id, from_lat, from_lon, to_lat, to_lon):
        self.id = int(id)
        self.from_lat = float(from_lat)
        self.from_lon = float(from_lon)
        self.to_lat = float(to_lat)
        self.to_lon = float(to_lon)
        start_point = Point(self.from_lon, self.from_lat)
        end_point = Point(self.to_lon, self.to_lat)
        self.geom = LineString([start_point, end_point])

    def project_point(self, point):
        line = self.geom.coords
        x = np.array(point.coords[0])
        u = np.array(line[0])
        v = np.array(line[len(line) - 1])
        n = v - u
        n /= np.linalg.norm(n, 2)
        p = u + n * np.dot(x - u, n)
        return Point(p[0], p[1])
