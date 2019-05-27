import unittest

from app.Edge import Edge

ID = 1
FROM_LAT = 2.0
FROM_LON = 3.14
TO_LAT = 5.0
TO_LON = 4.14


class EdgeTest(unittest.TestCase):

    def test_edge_has_instance_variables(self):
        edge = Edge(ID, FROM_LAT, FROM_LON, TO_LAT, TO_LON)

        self.assertSequenceEqual(
            [edge.id, edge.from_lat, edge.from_lon, edge.to_lat, edge.to_lon],
            [ID, FROM_LAT, FROM_LON, TO_LAT, TO_LON]
        )
