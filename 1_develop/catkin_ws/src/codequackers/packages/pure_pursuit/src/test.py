import numpy as np

def find_point_closest_to_lookahead_distance(points, lookahead_dist):
    # TODO: only consider points that are forward from the current robot position!
    lookahead_mag = lookahead_dist ** 2
    distances = points[:, 0] ** 2 + points[:, 1] ** 2
    distances_from_lookahead_mag = np.abs(distances - lookahead_dist)
    min_index = np.argmin(distances_from_lookahead_mag, axis=0)
    best_point = points[min_index]
    return best_point


points = np.array([
    [1.0, 0.0, 1231],
    # [0.0, 0.0, 1232],
    # [1.0, 1.1, 1233],
])

p_closest = find_point_closest_to_lookahead_distance(points, lookahead_dist=1.0)
print(p_closest)