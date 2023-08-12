import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Triangle height
TH = np.sqrt(3)/2

class DrawScene:

    def __init__(self, left, bottom, width, height, lcolor, lstyle, lwidth):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
        self.lcolor = lcolor
        self.lstyle = lstyle
        self.lwidth = lwidth
        self.polygons = dict()

        plt.figure()
        self.fig, self.ax = plt.subplots()
        self.ax.axis('equal')
        self.ax.axis('off')
        plt.margins(x=0)
        plt.margins(y=0)



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

    # "offset" is given in "modified Descartes" coordinates:
    # Namely, it is prior to multiplying "y" coordinate with the unit triangle height.
    # Normally we do not draw rectangles around polyiamonds
    # May be used if they do not pack neatly.
    def draw_polyiamond(self, label, poly, color = 'k', linewidth=0.8, offset = (0.0, 0.0), bound_box = False):
        self.polygons[label] = (poly, offset)
        vert2d = poly.get_mod_descartes()
        x = [vv[0] + offset[0] for vv in vert2d]
        x.append(x[0])
        y = [vv[1] + offset[1] for vv in vert2d]
        y.append(y[0])
        y = [yy * TH for yy in y]
        self.ax.plot(x,y,'-', color=color, linewidth=0.8)
        if bound_box:
            (xmin, xmax, ymin, ymax) = poly.get_rect_box()
            x1 = [xmin, xmax, xmax, xmin, xmin]
            y1 = [ymin, ymin, ymax, ymax, ymin]
            x1 = [offset[0] + xx for xx in x1]
            y1 = [(offset[1] + yy) * TH for yy in y1]
            self.ax.plot(x1, y1, '-', color='#ff0000', linewidth=0.8)


    # Draw some highlighted "sides" in a polyiamond that is already drawn
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



    def set_size_in(self, width, height):
        self.fig.set_size_inches(width, height)



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