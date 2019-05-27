import unittest
from shapely.geometry import Point
from app.waypoint import Waypoint

ID = 1
LAT = 2.0
LON = 3.14


class TestWaypoint(unittest.TestCase):

    def test_waypoint_has_instance_variables(self):
        waypoint = Waypoint(ID, LAT, LON)

        self.assertSequenceEqual(
            [waypoint.id, waypoint.y, waypoint.x],
            [ID, LAT, LON]
        )

    def test_distance_to(self):
        waypoint = Waypoint(0, 0.0, 0.0)
        point = Point(3.0, 4.0)

        self.assertEqual(waypoint.distance(point), 5.0)
