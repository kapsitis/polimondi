from polyforms.point_tg import *

def test_matrix():
    assert abs(T2D_MATRIX[0][0] - 1.0) < 1E-7
    assert abs(T2D_MATRIX[0][1] - 0.5) < 1E-7
    assert abs(T2D_MATRIX[1][0] - 0.0) < 1E-7
    assert abs(T2D_MATRIX[1][1] - (-0.86602540)) < 1E-7

def test_get_xy():
    pt = PointTg(5, -4, -1)
    (res_x, res_y) = pt.get_xy()
    assert abs(res_x - 3.0) < 1E-7
    assert abs(res_y - 3.4641016151377544) < 1E-7