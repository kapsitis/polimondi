import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
# import math


def rotate(point, angle):
    x0 = point[0]
    y0 = point[1]
    x1 = np.cos(angle)*x0 - np.sin(angle)*y0
    y1 = np.sin(angle)*x0 + np.cos(angle)*y0
    return [x1,y1]



SEQUENCE_A = [
    ['A', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'A', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B', 'C', 'B']
    ]

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


def draw_seq(seq, color,dd):
    # Draw polyline
    x, y = [0+dd[0]], [-44*np.sqrt(3)/2+dd[1]]
    for i, d in enumerate(seq):
        v = direction_to_vector(d)
        x.append(x[-1] + (len(seq) - i) * v[0])
        y.append(y[-1] + (len(seq) - i) * v[1])

    plt.plot(x, y, '{}-'.format(color), linewidth=0.8)

    # Set plot limits and aspect ratio
    
    #plt.xlim(-10, 70)
    #plt.ylim(-10, 70)
    #plt.gca().set_aspect('equal', adjustable='box')

    
    # plt.show()



def draw_grid(SIDE): 
    fig, ax = plt.subplots()

    plt.gcf().set_size_inches(10, 8)

    # Uzvelk ārējo sešstūri
    vertX = []
    vertY = []
    for i in range(0, 7):
        vertX.append(SIDE*np.cos(2*np.pi*i/6))
        vertY.append(SIDE*np.sin(2*np.pi*i/ 6))
    plt.plot(vertX, vertY)

    # Uz X un Y asīm uzliek vienādu mērogu
    ax.axis('equal')

    unit_h = np.sqrt(3) / 2
    for i in range(0,SIDE):
        x1_A, y1_A = -(2*SIDE - i)/2, i*unit_h
        x2_A, y2_A = (2*SIDE - i)/2, i*unit_h
        [x1_B, y1_B] = rotate([x1_A,y1_A], np.pi/3)
        [x2_B, y2_B] = rotate([x2_A, y2_A], np.pi / 3)
        [x1_C, y1_C] = rotate([x1_A,y1_A], 2*np.pi/3)
        [x2_C, y2_C] = rotate([x2_A, y2_A], 2*np.pi / 3)
        plt.plot([x1_A,x2_A], [y1_A, y2_A], color='black', linestyle='solid', linewidth=0.25)
        plt.plot([x1_B, x2_B], [y1_B, y2_B], color='black', linestyle='solid', linewidth=0.25)
        plt.plot([x1_C, x2_C], [y1_C, y2_C], color='black', linestyle='solid', linewidth=0.25)
    for i in range(-SIDE+1,0):
        x1_A, y1_A = -(2*SIDE + i)/2, i*unit_h
        x2_A, y2_A = (2*SIDE + i)/2, i*unit_h
        [x1_B, y1_B] = rotate([x1_A,y1_A], np.pi/3)
        [x2_B, y2_B] = rotate([x2_A, y2_A], np.pi / 3)
        [x1_C, y1_C] = rotate([x1_A,y1_A], 2*np.pi/3)
        [x2_C, y2_C] = rotate([x2_A, y2_A], 2*np.pi / 3)
        plt.plot([x1_A,x2_A], [y1_A, y2_A], color='black', linestyle='solid', linewidth=0.25)
        plt.plot([x1_B, x2_B], [y1_B, y2_B], color='black', linestyle='solid', linewidth=0.25)
        plt.plot([x1_C, x2_C], [y1_C, y2_C], color='black', linestyle='solid', linewidth=0.25)

    plt.axis('off')

    # fig.savefig('matplotlib_hexagon.png', dpi = 100)
    draw_seq(SEQUENCE_A[0], 'r', [0.0,0.0])
    draw_seq(SEQUENCE_A[2], 'b', [0.1,0.1])
    
    
    plt.savefig("inductive_drawing.svg")
    plt.show()




def main(): 
    draw_grid(60)
    # draw_seq(SEQUENCE_A[0], 'r')




if __name__ == '__main__': 
    main()


