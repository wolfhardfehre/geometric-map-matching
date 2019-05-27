import unittest
from shapely.geometry import Point
from app.edge import Edge

ID = 1
FROM_LAT = 0.0
FROM_LON = 0.0
TO_LAT = 0.0
TO_LON = 1.0


class TestEdge(unittest.TestCase):

    def test_edge_has_instance_variables(self):
        edge = Edge(ID, FROM_LAT, FROM_LON, TO_LAT, TO_LON)

        self.assertSequenceEqual(
            [edge.id, edge.from_lat, edge.from_lon, edge.to_lat, edge.to_lon],
            [ID, FROM_LAT, FROM_LON, TO_LAT, TO_LON]
        )

    def test_project_point(self):
        edge = Edge(ID, FROM_LAT, FROM_LON, TO_LAT, TO_LON)
        point = edge.project_point(Point(0.5, 0.5))

        self.assertSequenceEqual(
            [point.x, point.y],
            [0.5, 0.0]
        )
