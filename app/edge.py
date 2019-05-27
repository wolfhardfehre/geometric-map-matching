import numpy as np
from shapely.geometry import Point
from shapely.geometry import LineString


class Edge(LineString):
    def __init__(self, id, from_lat, from_lon, to_lat, to_lon):
        super().__init__([(float(from_lon), float(from_lat)), (float(to_lon), float(to_lat))])
        self.id = int(id)

    def project_point(self, point):
        line = self.coords
        x = np.array(point.coords[0])
        u = np.array(line[0])
        v = np.array(line[len(line) - 1])
        n = v - u
        n /= np.linalg.norm(n, 2)
        p = u + n * np.dot(x - u, n)
        return Point(p[0], p[1])
