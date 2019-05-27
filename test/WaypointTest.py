import unittest

from app.Waypoint import Waypoint

ID = 1
LAT = 2.0
LON = 3.14


class WaypointTest(unittest.TestCase):

    def test_waypoint_has_instance_variables(self):
        waypoint = Waypoint(ID, LAT, LON)

        self.assertSequenceEqual(
            [waypoint.id, waypoint.lat, waypoint.lon],
            [ID, LAT, LON]
        )
