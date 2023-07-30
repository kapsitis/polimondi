from math import sqrt
from scipy.spatial import ConvexHull, distance_matrix
import numpy as np

##########################################################
## This contains some real-valued 2D geometry utilities.
## No references to PointTg or any triangle geometry here.
#############################################################

# Measure the Euclidean (L2) distance between points p1 = (x1,y1) and p2 = (x2, y2)
def L2_dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the diameter of a set of points
def set_diameter(pt_set):
    # create a convex hull object
    hull = ConvexHull(pt_set)

    # get the vertices of the convex hull
    convex_vertices = pt_set[hull.vertices]

    # compute all pairwise distances in convex_vertices
    dist_mat = distance_matrix(convex_vertices, convex_vertices)

    # return the maximum pairwise distance
    return np.max(dist_mat)