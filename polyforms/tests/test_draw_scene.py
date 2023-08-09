import os
from polyforms.draw_scene import *
from polyforms.seq_storage import *

import numpy as np

TH = np.sqrt(3)/2


def test_dummy():
    assert 2*2 == 4


# def test_generate_sequence_4_3_a():
#     scene = draw_scene(-4, -8, 80, 80, '#999999', 'solid', 0.25)
#     scene.draw_seq(seq_storage.SEQUENCE_4_3_A[0], 'b', [0.0,0.0])
#     scene.draw_seq(seq_storage.SEQUENCE_4_3_A[1], 'b', [25.0,0.0])
#     scene.draw_seq(seq_storage.SEQUENCE_4_3_A[2], 'b', [50.0,0.0])
#     scene.create_grid('SEQUENCE_4_3_A.svg')
#     scene.insertOption("SEQUENCE_4_3_A.svg")
#     # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')
