import os
from konstrukcijas.inductive_drawings.draw_scene import *
import numpy as np

TH = np.sqrt(3)/2


def test_generate_sequence_4_3_a():
    scene = draw_scene(-4, -8, 80, 80, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_4_3_A[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_4_3_A[1], 'b', [25.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_4_3_A[2], 'b', [50.0,0.0])
    scene.create_grid('SEQUENCE_4_3_A.svg')
    scene.insertOption("SEQUENCE_4_3_A.svg")
    # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')

def test_generate_sequence_4_3_b():
    scene = draw_scene(-10, -14, 130, 130, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_4_3_B[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_4_3_B[1], 'b', [40.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_4_3_B[2], 'b', [80.0,0.0])
    scene.create_grid('SEQUENCE_4_3_B.svg')
    scene.insertOption("SEQUENCE_4_3_B.svg")

def test_generate_sequence_4_1_a():
    scene = draw_scene(-16, -16, 130, 130, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_4_1_A[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_4_1_A[1], 'b', [40.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_4_1_A[2], 'b', [80.0,0.0])
    scene.create_grid('SEQUENCE_4_1_A.svg')
    scene.insertOption("SEQUENCE_4_1_A.svg")

def test_generate_sequence_8_7_a():
    scene = draw_scene(-10, -16, 160, 80, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_7_A[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_7_A[1], 'b', [40.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_7_A[2], 'b', [120.0,0.0])
    scene.create_grid('SEQUENCE_8_7_A.svg')
    scene.insertOption("SEQUENCE_8_7_A.svg")

def test_generate_sequence_8_7_b():
    scene = draw_scene(-10, -24, 160, 220, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_7_B[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_7_B[1], 'b', [50.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_7_B[2], 'b', [100.0,0.0])
    scene.create_grid('SEQUENCE_8_7_B.svg')
    scene.insertOption("SEQUENCE_8_7_B.svg")

def test_generate_sequence_8_7_c():
    scene = draw_scene(-10, -24, 160, 220, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_7_C[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_7_C[1], 'b', [50.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_7_C[2], 'b', [100.0,0.0])
    scene.create_grid('SEQUENCE_8_7_C.svg')
    scene.insertOption("SEQUENCE_8_7_C.svg")

def test_generate_sequence_8_7_d():
    scene = draw_scene(-10, -24, 200, 220, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_7_D[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_7_D[1], 'b', [60.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_7_D[2], 'b', [120.0,0.0])
    scene.create_grid('SEQUENCE_8_7_D.svg')
    scene.insertOption("SEQUENCE_8_7_D.svg")


def test_generate_sequence_8_5_a():
    scene = draw_scene(-10, -10, 140, 80, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_5_A[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_5_A[1], 'b', [40.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_5_A[2], 'b', [80.0,0.0])
    scene.create_grid('SEQUENCE_8_5_A.svg')
    scene.insertOption("SEQUENCE_8_5_A.svg")

def test_generate_sequence_8_5_b():
    scene = draw_scene(-16, -36, 220, 300, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_5_B[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_5_B[1], 'b', [70.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_5_B[2], 'b', [140.0,0.0])
    scene.create_grid('SEQUENCE_8_5_B.svg')
    scene.insertOption("SEQUENCE_8_5_B.svg")

def test_generate_sequence_8_3_a():
    scene = draw_scene(-10, -20, 180, 160,  '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_3_A[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_A[1], 'b', [40.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_A[2], 'b', [110.0,0.0])
    scene.create_grid('SEQUENCE_8_3_A.svg')
    scene.insertOption("SEQUENCE_8_3_A.svg")

def test_generate_sequence_8_3_b():
    scene = draw_scene(-10, -10, 160, 100, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_3_B[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_B[1], 'b', [50.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_B[1], 'b', [100.0,0.0])
    scene.create_grid('SEQUENCE_8_3_B.svg')
    scene.insertOption("SEQUENCE_8_3_B.svg")

def test_generate_sequence_8_3_c():
    scene = draw_scene(-10, -24, 160, 180,  '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_3_C[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_C[1], 'b', [50.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_C[2], 'b', [100.0,0.0])
    scene.create_grid('SEQUENCE_8_3_C.svg')
    scene.insertOption("SEQUENCE_8_3_C.svg")

def test_generate_sequence_8_3_d():
    scene = draw_scene(-10, -24, 160, 180,  '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_3_D[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_D[1], 'b', [50.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_D[2], 'b', [100.0,0.0])
    scene.create_grid('SEQUENCE_8_3_D.svg')
    scene.insertOption("SEQUENCE_8_3_D.svg")

def test_generate_sequence_8_3_e():
    scene = draw_scene(-10, -24, 160, 180,  '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_3_E[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_E[1], 'b', [50.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_3_E[2], 'b', [100.0,0.0])
    scene.create_grid('SEQUENCE_8_3_E.svg')
    scene.insertOption("SEQUENCE_8_3_E.svg")

def test_generate_sequence_8_1_a():
    scene = draw_scene(-10, -40, 220, 180,  '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_1_A[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_1_A[1], 'b', [50.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_1_A[2], 'b', [120.0,0.0])
    scene.create_grid('SEQUENCE_8_1_A.svg')
    scene.insertOption("SEQUENCE_8_1_A.svg")

def test_generate_sequence_8_1_b():
    scene = draw_scene(-20, -24, 200, 240, '#999999', 'solid', 0.25)
    scene.draw_seq(poly_seq.SEQUENCE_8_1_B[0], 'b', [0.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_1_B[1], 'b', [60.0,0.0])
    scene.draw_seq(poly_seq.SEQUENCE_8_1_B[2], 'b', [120.0,0.0])
    scene.create_grid('SEQUENCE_8_1_B.svg')
    scene.insertOption("SEQUENCE_8_1_B.svg")


