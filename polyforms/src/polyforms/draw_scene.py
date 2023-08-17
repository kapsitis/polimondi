import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from enum import Enum
import math
from .point_tg import PointTg

# Triangle height
TH = np.sqrt(3)/2

# Different rules of alignment on a horizontal layout area.
# Align.TOP  means that all polyiamonds have their top sides near the upper part of the image.
# Align.BOTTOM means that all polyiamonds have their bottom sides near the lower part of the image.
# Align.CENTER means that all polyiamonds are centered -- their centers are on the same horizontal line.
# Align.BASELINE means that all polyiamonds (their longer edges) start at the same level.
class Align(Enum):
    TOP = 'top'
    BOTTOM = 'bottom'
    CENTER = 'center'
    BASELINE = 'baseline'


# This class is used to display polyiamonds using Matplotlib.
# Could be used from Jupyter Notebooks, for printable PDFs (ReStructured Text; Python Sphinx), etc.
class DrawScene:

    # "Empty" constructor -- only sets the alignment rule.
    # All meaningful initializations happen in function "pack()".
    def __init__(self, alignment):
        self.align = alignment
        self.left = 0
        self.bottom = 0
        self.width = 0
        self.height = 0
        self.lcolor = '#999999'
        self.lstyle = 'solid'
        self.lwidth = 0.25
        # Redundant `self.labels` (refactor as list of longer tuples?)
        self.polygons = dict()
        self.labels = []
        plt.figure()
        self.fig, self.ax = plt.subplots()
        self.ax.axis('equal')
        self.ax.axis('off')
        plt.margins(x=0)
        plt.margins(y=0)


    # Assign offsets to all the polyiamonds and draw them on Matplotlib canvas.
    # Aligment.BASELINE means that all polyiamonds are aligned by their "origin points"
    # That means -- points where their longest side starts.
    # Offsets offset_x increase for subsequent polyiamonds, but always offset_y==0.
    def pack(self):
        bounding = []
        for label in self.labels:
            nums = self.polygons[label][0].get_rect_box()
            numbers = nums
            bounding.append((numbers[0], numbers[1], numbers[2], numbers[3]))
        self.bottom = int(round(min([item[2] for item in bounding]))) - 1
        if self.bottom % 2 == 1:
            self.bottom -= 1
        self.left = int(round(bounding[0][0]))
        self.width = int(round(sum([item[1] - item[0] for item in bounding]) + 4*len(bounding) - 2))
        self.height = int(round(max([item[3] - item[2] for item in bounding]))) + 3
        if self.height % 2 == 1:
            self.height += 1

        offset_x = 1
        N = len(bounding)
        for idx,label in enumerate(self.labels):
            (off_x, off_y) = self.polygons[label][1]
            self.draw_polyiamond(label, self.polygons[label][0], 'k', offset = (off_x + offset_x, off_y), box = self.polygons[label][2])
            # print("{} = {} + ({} - {})+2".format(offset_x, offset_x, bounding[(idx+1) % N][1], bounding[(idx+1) % N][0]))
            offset_x = offset_x + (bounding[(idx+1) % N][1] - bounding[(idx+1) % N][0])


    # Internally used function - to cut the relevant path out of a triange grid.
    # Triangle grids (as in "show_grid()") are always of rectangular shape.
    # End-user does not need to use this function.
    def create_rectangle_path(self):
        vertices = np.array([
                [self.left, self.bottom],
                [self.left + self.width, self.bottom],
                [self.left + self.width, (self.height + self.bottom) * TH],
                [self.left, (self.height + self.bottom) * TH], [0, 0]
            ])
        codes = [
            mpath.Path.MOVETO, mpath.Path.LINETO, mpath.Path.LINETO, mpath.Path.LINETO,
            mpath.Path.CLOSEPOLY
        ]
        path = mpath.Path(vertices, codes)
        return path


    # User-friendly function to add a new polyiamond.
    # All the relevant drawing is done in `draw_polyiamond()` after `pack()` was called.
    def add_polyiamond(self, label, poly, offset = (0.0, 0.0), box = False):
        self.polygons[label] = (poly, offset, box)
        self.labels.append(label)



    # Typically not called by end-users; use "add_polyiamond" instead.
    # Draw a polyiamond at the given offset (regardless of what else is on the picture)
    # "label" - same label that was used in "add_polyiamond" (to pull data from dictionary).
    # "offset" is given in "modified Descartes" coordinates.
    # E.g. offset = (0.5, 1) moves it higher by one gridline; and shift it by halfside to the right.
    # Normally we do not draw rectangles around polyiamonds (box == False).
    def draw_polyiamond(self, label, poly, color = 'k', offset = (0.0, 0.0), box = False):
        # print('draw_polyiamond({},offset={}'.format(label,offset))
        # Redefine offset
        self.polygons[label] = (poly, offset)
        vert2d = poly.get_mod_descartes()
        x = [vv[0] + offset[0] for vv in vert2d]
        x.append(x[0])
        y = [vv[1] + offset[1] for vv in vert2d]
        y.append(y[0])
        y = [yy * TH for yy in y]
        self.ax.plot(x,y,'-', color=color, linewidth=0.8)
        if box:
            (xmin, xmax, ymin, ymax) = poly.get_rect_box()
            x1 = [xmin, xmax, xmax, xmin, xmin]
            y1 = [ymin, ymin, ymax, ymax, ymin]
            x1 = [offset[0] + xx for xx in x1]
            y1 = [(offset[1] + yy) * TH for yy in y1]
            self.ax.plot(x1, y1, '-', color='#ff0000', linewidth=0.8)


    # Find the current offset of a polygon;
    # May be useful, if we need to add something to the picture).
    def get_offset(self, label):
        if label not in self.polygons:
            return (0,0)
        else:
            return self.polygons[label][1]

    def get_offset_tg(self, label):
        if label not in self.polygons:
            return PointTg(0,0,0)
        else:
            return PointTg(self.polygons[label][1][0], 0, -(self.polygons[label][1][0]))

    # Draw some highlighted/colored "sides" in a polyiamond that is already drawn
    # 'label' is the name of the polygon added to a picture.
    def highlight(self, label, sides, color):
        curr_polygon = self.polygons[label][0]
        (off_x, off_y) = self.polygons[label][1]
        vert2d = curr_polygon.get_mod_descartes()
        N = len(vert2d)
        for side in sides:
            x = [off_x + vert2d[side][0], off_x + vert2d[(side + 1) % N][0]]
            y = [off_y + vert2d[side][1], off_y + vert2d[(side + 1) % N][1]]
            y = [yy * TH for yy in y]
            self.ax.plot(x, y, '-', color=color, linewidth=3)



    # Set polyiamond size width*height in inches.
    # Sometimes Jupyter Notebook prevents too large image sizes (need to experiment).
    def set_size_in(self, width, height):
        self.fig.set_size_inches(width, height)


    # Draw triangle grid in addition to polyiamonds.
    def show_grid(self):
        # self.fig.set_size_inches(round(self.width / 218, 2), round(self.height / 218, 2))
        self.fig.set_size_inches(self.width/10 ,self.height/10)
        self.ax.set_xlim(self.left, self.left + self.width)
        self.ax.set_ylim(self.bottom, self.left+self.height)

        path = self.create_rectangle_path()
        patch = mpatches.PathPatch(path, transform=self.ax.transData)

        # Horizontal lines
        for i in range(0, self.height + 1):
            plus_minus = 0 if i % 2 == 0 else 0.5
            line, = self.ax.plot([self.left + plus_minus, self.left + self.width - plus_minus], [(self.bottom + i) * TH, (self.bottom + i) * TH],
                            color=self.lcolor, linestyle=self.lstyle, linewidth=self.lwidth)
            line.set_clip_path(patch)

        # Slanted-upwards lines
        for i in range(-self.height // 2, self.width + 1):
            line, = self.ax.plot([self.left + i, self.left + i + self.height * TH / np.sqrt(3)], [self.bottom * TH, (self.bottom + self.height) * TH],
                            color=self.lcolor, linestyle=self.lstyle, linewidth=self.lwidth)
            line.set_clip_path(patch)

        # Slanted-downwards lines
        for i in range(0, self.width + self.height // 2 + 1):
            line, = self.ax.plot([self.left + i, self.left + i - self.height * TH / np.sqrt(3)], [self.bottom * TH, (self.bottom + self.height) * TH],
                            color=self.lcolor, linestyle=self.lstyle, linewidth=self.lwidth)
            line.set_clip_path(patch)

        # plt.savefig('../docs/inductive_sequences/{}'.format(output_file), format='svg', bbox_inches='tight', transparent="True", pad_inches=0)

    # TODO: Move this to another module -- responsible for the export to HTML+SVG
    def create_grid(self, output_file):
        # self.fig.set_size_inches(round(self.width / 218, 2), round(self.height / 218, 2))
        self.fig.set_size_inches(self.width/10 ,self.height/10)
        self.ax.set_xlim(self.left, self.left + self.width)
        self.ax.set_ylim(self.bottom, self.left+self.height)

        path = self.create_rectangle_path()
        patch = mpatches.PathPatch(path, transform=self.ax.transData)

        # Horizontal lines
        for i in range(0, self.height + 1):
            plus_minus = 0 if i % 2 == 0 else 0.5
            line, = self.ax.plot([self.left + plus_minus, self.left + self.width - plus_minus], [(self.bottom + i) * TH, (self.bottom + i) * TH],
                            color=self.lcolor, linestyle=self.lstyle, linewidth=self.lwidth)
            line.set_clip_path(patch)

        # Slanted-upwards lines
        for i in range(-self.height // 2, self.width + 1):
            line, = self.ax.plot([self.left + i, self.left + i + self.height * TH / np.sqrt(3)], [self.bottom * TH, (self.bottom + self.height) * TH],
                            color=self.lcolor, linestyle=self.lstyle, linewidth=self.lwidth)
            line.set_clip_path(patch)

        # Slanted-downwards lines
        for i in range(0, self.width + self.height // 2 + 1):
            line, = self.ax.plot([self.left + i, self.left + i - self.height * TH / np.sqrt(3)], [self.bottom * TH, (self.bottom + self.height) * TH],
                            color=self.lcolor, linestyle=self.lstyle, linewidth=self.lwidth)
            line.set_clip_path(patch)

        plt.savefig('../docs/inductive_sequences/{}'.format(output_file), format='svg', bbox_inches='tight', transparent="True", pad_inches=0)


    # TODO: Move this to another module -- responsible for the export to HTML+SVG
    def insertOption(self, key, width = 0, height = 0):
        if width == 0 or height == 0:
            width = round(self.width * 7.2)
            height = round(self.height * 7.2)


        # Read the existing HTML file
        with open("../docs/inductive_sequences.html", "r") as file:
            html_content = file.read()

        # Parse the HTML using Beautiful Soup
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the select element with id "selectSvg"
        select_element = soup.find("select", {"id": "selectSvg"})

        # # Check if an option exists with the given key
        # option = select_element.find("option", {"value": f"{key};{width};{height}"})

        option_found = False
        # children = select_element.findChildren("option", recursive=False)
        for option in select_element.find_all("option"):
            # for child in children:
            print("uu = {}".format(option["value"]))
            if option["value"] and option["value"].startswith(f"{key};"):
                option_found = True
                break

        # If option exists, update its value attribute
        if option_found:
            option["value"] = f"{key};{width};{height}"
        # If option does not exist, create a new option element and insert it
        else:
            new_option = soup.new_tag(
                "option", value=f"{key};{width};{height}"
            )
            # Visible content of OPTION element
            new_option.string = key.split(".")[0]
            select_element.append(new_option)
            # Add a newline after inserting the new OPTION element
            newline = soup.new_string('\n')
            select_element.append(newline)

        # Write the modified HTML back to the file
        with open("../docs/inductive_sequences.html", "w") as file:
            file.write(str(soup))
