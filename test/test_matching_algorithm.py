import unittest

from shapely.geometry import Point

from edge import Edge
from matchingalgorithm import MatchingAlgorithm
from waypoint import Waypoint


class TestMatchingAlgorithm(unittest.TestCase):

    def test_snap_to_closest(self):
        close_edge = Edge(0, 0.0, 0.0, 0.0, 1.0)
        far_away_edge = Edge(0, 1.0, 0.0, 1.0, 1.0)
        point = Waypoint(0, 0.1, 0.0)

        matcher = MatchingAlgorithm([point], [close_edge, far_away_edge])
        projected = matcher.snap_to_closest(point)

        self.assertEqual(projected, Point(0.0, 0.0))

    def test_best_match(self):
        close_edge = Edge(0, 0.0, 0.0, 0.0, 1.0)
        far_away_edge = Edge(0, 1.0, 0.0, 1.0, 1.0)
        previous = Waypoint(0, -0.3, 0.5)
        current = Waypoint(0, 0.4, 0.9)
        next = Waypoint(0, -0.3, 1.5)
        window = [previous, current, next]

        matcher = MatchingAlgorithm([current], [close_edge, far_away_edge])
        matched_point = matcher.best_match(window)

        expected = Point(0.9, 0.0)
        self.assertEqual(matched_point, expected)

    def test_match(self):
        close_edge = Edge(0, 0.0, 0.0, 0.0, 1.0)
        far_away_edge = Edge(0, 1.0, 0.0, 1.0, 1.0)
        previous = Waypoint(0, -0.3, 0.5)
        current = Waypoint(0, 0.4, 0.9)
        next = Waypoint(0, -0.3, 1.5)
        window = [previous, current, next]

        matcher = MatchingAlgorithm([current], [close_edge, far_away_edge])
        matched_point = matcher.best_match(window)

        expected = Point(0.9, 0.0)
        self.assertEqual(matched_point, expected)
