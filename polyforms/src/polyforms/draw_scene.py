import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


# from konstrukcijas.inductive_drawings import poly_seq

# Triangle height
TH = np.sqrt(3)/2

def direction_to_vector(d):
    if d == 'A':
        return np.array([1, 0])
    elif d == 'B':
        return np.array([1/2, np.sqrt(3)/2])
    elif d == 'C':
        return np.array([-1/2, np.sqrt(3)/2])
    elif d == 'D':
        return np.array([-1, 0])
    elif d == 'E':
        return np.array([-1/2, -np.sqrt(3)/2])
    elif d == 'F':
        return np.array([1/2, -np.sqrt(3)/2])

def trim_svg_whitespace(file_path):
    # Parse SVG file
    with open(file_path, 'r') as input_file:
        tree = ET.parse(input_file)

    root = tree.getroot()

    # Find the first group element <g>
    group = root.find(".//{http://www.w3.org/2000/svg}g")

    # Find the viewBox attribute in the SVG root element
    viewBox = root.attrib["viewBox"]
    viewBox_values = [float(value) for value in viewBox.split()]

    # Calculate the new viewBox values without extra padding
    new_viewBox_values = [
        viewBox_values[0] + group.attrib["transform"].translate.x,
        viewBox_values[1] + group.attrib["transform"].translate.y,
        viewBox_values[2] - group.attrib["transform"].translate.x,
        viewBox_values[3] - group.attrib["transform"].translate.y,
    ]

    # Update the viewBox attribute with the new values
    root.attrib["viewBox"] = " ".join(str(value) for value in new_viewBox_values)

    # Write the modified SVG back to the same file
    with open(file_path, "wb") as output_file:
        tree.write(output_file)





class DrawScene:

    def __init__(self, left, bottom, width, height, lcolor, lstyle, lwidth):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
        self.lcolor = lcolor
        self.lstyle = lstyle
        self.lwidth = lwidth

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

    def draw_seq(self, seq, color, dd):
        # Draw polyline
        x, y = [0 + dd[0]], [dd[1]]
        for i, d in enumerate(seq):
            v = direction_to_vector(d)
            x.append(x[-1] + (len(seq) - i) * v[0])
            y.append(y[-1] + (len(seq) - i) * v[1])

        self.ax.plot(x, y, '{}-'.format(color), linewidth=0.8)



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