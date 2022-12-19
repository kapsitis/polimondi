import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import math

import dict_stuff


def rotate(point, angle):
    x0 = point[0]
    y0 = point[1]
    x1 = math.cos(angle)*x0 - math.sin(angle)*y0
    y1 = math.sin(angle)*x0 + math.cos(angle)*y0
    return [x1,y1]

def getXY(point):
    unit_h = math.sqrt(3) / 2
    alpha = point.x
    beta = point.y
    x = alpha + 0.5*beta
    y = -unit_h * beta
    return [x,y]


def getColor(N):
    if N == 1:
        return 'red'
    elif N == 2:
        return 'gold'
    elif N == 3:
        return 'limegreen'
    elif N == 4:
        return 'deepskyblue'
    elif N == 5:
        return 'mediumorchid'
    else:
        return 'black'

fig, ax = plt.subplots()

plt.gcf().set_size_inches(10, 8)

# Uzvelk ārējo sešstūri
vertX = []
vertY = []
for i in range(0, 7):
    vertX.append(21*math.cos(2*math.pi*i/6))
    vertY.append(21 * math.sin(2*math.pi*i/ 6))
plt.plot(vertX, vertY)

# Uz X un Y asīm uzliek vienādu mērogu
ax.axis('equal')

unit_h = math.sqrt(3) / 2
for i in range(0,21):
    x1_A, y1_A = -(42 - i)/2, i*unit_h
    x2_A, y2_A = (42 - i)/2, i*unit_h
    [x1_B, y1_B] = rotate([x1_A,y1_A], math.pi/3)
    [x2_B, y2_B] = rotate([x2_A, y2_A], math.pi / 3)
    [x1_C, y1_C] = rotate([x1_A,y1_A], 2*math.pi/3)
    [x2_C, y2_C] = rotate([x2_A, y2_A], 2*math.pi / 3)
    plt.plot([x1_A,x2_A], [y1_A, y2_A], color='black', linestyle='dashed', linewidth=0.5)
    plt.plot([x1_B, x2_B], [y1_B, y2_B], color='black', linestyle='dashed', linewidth=0.5)
    plt.plot([x1_C, x2_C], [y1_C, y2_C], color='black', linestyle='dashed', linewidth=0.5)
for i in range(-20,0):
    x1_A, y1_A = -(42 + i)/2, i*unit_h
    x2_A, y2_A = (42 + i)/2, i*unit_h
    [x1_B, y1_B] = rotate([x1_A,y1_A], math.pi/3)
    [x2_B, y2_B] = rotate([x2_A, y2_A], math.pi / 3)
    [x1_C, y1_C] = rotate([x1_A,y1_A], 2*math.pi/3)
    [x2_C, y2_C] = rotate([x2_A, y2_A], 2*math.pi / 3)
    plt.plot([x1_A,x2_A], [y1_A, y2_A], color='black', linestyle='dashed', linewidth=0.5)
    plt.plot([x1_B, x2_B], [y1_B, y2_B], color='black', linestyle='dashed', linewidth=0.5)
    plt.plot([x1_C, x2_C], [y1_C, y2_C], color='black', linestyle='dashed', linewidth=0.5)





pointX = []
pointY = []
pointC = []
size_set = set()
for key in dict_stuff.dictionary.keys():
    [x,y] = getXY(key)
    pointX.append(x)
    pointY.append(y)
    pointC.append(getColor(len(dict_stuff.dictionary[key])))
    #pointC.append(len(dict_stuff.dictionary[key]))
    size_set.add(len(dict_stuff.dictionary[key]))

print('size_set = {}'.format(size_set))

plt.scatter(pointX, pointY, c=pointC)

#plt.plot(x, y, color='black', linestyle='dashed', linewidth=0.5)

cmap = plt.cm.rainbow

plt.axis('off')

fig.savefig('matplotlib_hexagon.png', dpi = 300)

plt.show()

