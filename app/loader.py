import csv

from edge import Edge
from waypoint import Waypoint


def get_waypoints(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [Waypoint(row["id"], row["lat"], row["lon"]) for row in csv_reader]


def get_edges(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [Edge(row["id"], row["from_lat"], row["from_lon"], row["to_lat"], row["to_lon"])
                for row in csv_reader]
