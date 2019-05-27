import unittest

import loader
from edge import Edge
from waypoint import Waypoint


class TestLoader(unittest.TestCase):

    def test_load_waypoints(self):
        self.assertEqual(len(loader.get_waypoints("../data/waypoints.csv")), 5)

    def test_load_specific_waypoint(self):
        expected = Waypoint(id=0, lat=0.4, lon=0.0)
        actual = loader.get_waypoints("../data/waypoints.csv")[0]
        self.assertSequenceEqual(
            [expected.id, expected.y, expected.x],
            [actual.id, actual.y, actual.x]
        )

    def test_load_edges(self):
        self.assertEqual(len(loader.get_edges("../data/edges.csv")), 3)

    def test_load_specific_edge(self):
        expected = Edge(0, 0.0, 0.0, 0.0, 1.0)
        actual = loader.get_edges("../data/edges.csv")[0]
        self.assertSequenceEqual(
            [expected.id, expected.from_lat, expected.from_lon, expected.to_lat, expected.to_lon],
            [actual.id, actual.from_lat, actual.from_lon, actual.to_lat, actual.to_lon]
        )
