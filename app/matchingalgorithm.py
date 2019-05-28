# pick points in window
# compute candidates
# compute length of candidates
# pick min length candidate
# go to next


class Candidate:

    def __init__(self, window, projected):
        self.prev, _, self.next = window
        self.projected = projected

    @property
    def length(self):
        return self.prev.distance(self.projected) + self.projected.distance(self.next)

    def __lt__(self, other):
        return self.length < other.length


class MatchingAlgorithm:

    def __init__(self, waypoints, edges):
        self.waypoints = waypoints
        self.edges = edges
        self.window_size = 3

    def match(self):
        previous_waypoint = self.snap_to_closest(self.waypoints[0])
        matched_points = [previous_waypoint]

        next_waypoint = None
        for idx, waypoint in enumerate(self.waypoints[1:]):
            next_waypoint = self.snap_to_closest(self.waypoints[idx + 1])
            window = [previous_waypoint, waypoint, next_waypoint]
            snapped = self.best_match(window)
            matched_points.append(snapped)
            previous_waypoint = snapped

        matched_points.append(next_waypoint)
        return matched_points

    def snap_to_closest(self, waypoint):
        distances = []
        for edge in self.edges:
            projected_point = edge.project_point(waypoint)
            distances.append((waypoint.distance(projected_point), projected_point))
        return min(distances)[1]

    def best_match(self, window):
        current = window[1]
        candidates = [Candidate(window, edge.project_point(current)) for edge in self.edges]
        return min(candidates).projected
