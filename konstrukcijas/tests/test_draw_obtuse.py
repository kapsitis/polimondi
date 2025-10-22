import os
from konstrukcijas.inductive_drawings.draw_scene import *
import numpy as np

TH = np.sqrt(3)/2


def generate_obtuse12():
    scene = draw_scene(-12, -6, 30, 30, '#999999', 'solid', 0.25)
    scene.draw_seq(list("ABCDEDEFAFAB"), 'b', [0.0,0.0])
    scene.create_grid("docs/perfect_obtuse", "MAX_OBTUSE_12.svg")
    scene.insertOption("docs/sequences.html", "MAX_OBTUSE_12.svg")
    # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')

def generate_obtuse18():
    scene = draw_scene(-6, -36, 60, 60, '#999999', 'solid', 0.25)
    scene.draw_seq(list("ABAFEDEDEDCBCBCBAB"), 'b', [0.0,0.0])
    scene.create_grid("docs/perfect_obtuse", "MAX_OBTUSE_18.svg")
    scene.insertOption("docs/sequences.html", "MAX_OBTUSE_18.svg")
    # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')

def generate_obtuse24():
    scene = draw_scene(-24, -78, 100, 110, '#999999', 'solid', 0.25)
    scene.draw_seq(list("ABAFEFEDEDCDCBCDCBABABAB"), 'b', [0.0,0.0])
    scene.create_grid("docs/perfect_obtuse", "MAX_OBTUSE_24.svg")
    scene.insertOption("docs/sequences.html", "MAX_OBTUSE_24.svg")
    # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')

def generate_obtuse30():
    scene = draw_scene(-24, -120, 170, 160, '#999999', 'solid', 0.25)
    scene.draw_seq(list("ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF"), 'b', [0.0,0.0])
    scene.create_grid("docs/perfect_obtuse", "MAX_OBTUSE_30.svg")
    scene.insertOption("docs/sequences.html", "MAX_OBTUSE_30.svg")
    # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')

def generate_obtuse36():
    scene = draw_scene(-80, -20, 200, 250, '#999999', 'solid', 0.25)
    scene.draw_seq(list("ABABCBCDCDCDEDEFEFEFEFEFAFAFAFABABCB"), 'b', [0.0,0.0])
    scene.create_grid("docs/perfect_obtuse", "MAX_OBTUSE_36.svg")
    scene.insertOption("docs/sequences.html", "MAX_OBTUSE_36.svg")
    # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')

def generate_obtuse42():
    scene = draw_scene(-120, -50, 270, 350, '#999999', 'solid', 0.25)
    scene.draw_seq(list("ABABCBCBCDCDEDEDEDEFEFEFEFAFAFAFAFAFABABCB"), 'b', [0.0,0.0])
    scene.create_grid("docs/perfect_obtuse", "MAX_OBTUSE_42.svg")
    scene.insertOption("docs/sequences.html", "MAX_OBTUSE_42.svg")
    # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')

def generate_obtuse48():
    scene = draw_scene(-210, -50, 380, 480, '#999999', 'solid', 0.25)
    scene.draw_seq(list("ABABCBCDCDCDCDEDEDEFEFEFEFAFAFAFAFAFABABABAFABCB"), 'b', [0.0,0.0])
    scene.create_grid("docs/perfect_obtuse", "MAX_OBTUSE_48.svg")
    scene.insertOption("docs/sequences.html", "MAX_OBTUSE_48.svg")
    # trim_svg_whitespace2('data/SEQUENCE_4_3_A.svg')

def main():
    generate_obtuse12()
    generate_obtuse18()
    generate_obtuse24()
    generate_obtuse30()
    generate_obtuse36()
    generate_obtuse42()
    generate_obtuse48()

if __name__=='__main__':
    main()