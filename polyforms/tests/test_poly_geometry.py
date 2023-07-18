from polyforms.poly_geometry import PolyGeometry

def test_bounding_hexagon():
    p1 = PolyGeometry([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    result = p1.get_bounding_hexagon()
    assert result == (-4, 0, -5, 1, 0, 5)

def test_bounding_box():
    p1 = PolyGeometry([(5,'A'), (4,'C'), (3,'E'), (2,'D'), (1,'F')])
    bounds = p1.get_bounding_sizes()
    # print('bounds = {}'.format(bounds))
    assert bounds == (4, 6, 5)

def test_direction_counts():
    p1 = PolyGeometry([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    counts = p1.get_direction_counts()
    # print('bounds = {}'.format(bounds))
    assert counts == (7, 3, 5)

