from matchingalgorithm import MatchingAlgorithm
from loader import get_waypoints
from loader import get_edges
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


if __name__ == "__main__":
    waypoints = get_waypoints("../data/waypoints.csv")
    edges = get_edges("../data/edges.csv")
    matcher = MatchingAlgorithm(waypoints, edges)
    matched_points = matcher.match()

    fig, ax = plt.subplots(1, 1)
    for edge in edges:
        coords = edge.coords
        l = mlines.Line2D([coords[0][0], coords[1][0]], [coords[0][1],coords[1][1]])
        ax.add_line(l)
    ax.scatter([w.x for w in waypoints], [w.y for w in waypoints], color='red')
    ax.scatter([m.x for m in matched_points], [m.y for m in matched_points], color='green')
    ax.plot()
    ax.set_xlim([-1, 3])
    ax.set_ylim([-1, 2])
    plt.show()
