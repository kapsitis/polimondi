# Šeit pārveidojam jocīgās Dekarta koordinātes par burtu kodējumu.

SEQUENCE_A = [
[[0,17], [16,-8], [0, 15], [14, -7], [-13, -6.5], [0, -12], [-11, 5.5], [0,-10], [-9, 4.5], [-8, -4], [0, 7], [6, -3], [0, 5], [4, -2], [0, -3], [2, 1], [-1, 0.5]],
[[0,25], [24, -12], [0, 23], [22, -11], [0,21], [20, -10], [-19, -9.5], [0, -18], [-17, 8.5], [0, -16], [-15, 7.5], [0, -14], [-13, 6.5], [0,-12], [-11, 5.5], [-10, -5], [0, 9], [8, -4], [0, 7], [6, -3], [0, 5], [4, -2], [0, -3], [2, 1], [-1, 0.5]],
[[0,33], [32, -16], [0,31], [30, -15], [0, 29], [28, -14], [0,27], [26,-13], [-25, -12.5], [0,-24], [-23, 11.5], [0,-22], [-21, 10.5], [0,-20], [-19, 9.5], [0, -18], [-17, 8.5], [0,-16], [-15, 7.5], [0, -14], [-13, 6.5], [-12, -6], [0, 11], [10, -5], [0, 9], [8, -4], [0, 7], [6, -3], [0, 5], [4, -2], [0, -3], [2, 1], [-1, 0.5]],
[[0,1]],

[[0, 17], [16, -8], [15, 7.5], [14, -7], [0, -13], [-12, -6], [0, 11], [-10, 5], [-9, -4.5], [0, -8], [-7, 3.5], [-6, -3], [-5, 2.5], [0, 4], [3, 1.5], [0, -2], [1, -0.5]],
[[0, 25], [24, -12], [23, 11.5], [22, -11], [21, 10.5], [20, -10], [0, -19], [-18, -9], [0, 17], [-16, 8], [-15, -7.5], [-14, 7], [-13, -6.5], [0, -12], [-11, 5.5], [-10, -5], [-9, 4.5], [-8, -4], [-7, 3.5], [0, 6], [5, 2.5], [0, -4], [3, -1.5], [2, 1], [1, -.5]],
[[0, 33], [32, -16], [31, 15.5], [30, -15], [29, 14.5], [28, -14], [27, 13.5], [26, -13], [0, -25], [-24, -12], [0, 23], [-22, 11], [-21, -10.5], [-20, 10], [-19, -9.5], [-18, 9], [-17, -8.5], [0, -16], [-15, 7.5], [-14, -7], [-13, 6.5], [-12, -6], [-11, 5.5], [-10, -5], [-9, 4.5], [0, 8], [7, 3.5], [0, -6], [5, -2.5], [4, 2], [3, -1.5], [2, 1], [1, -.5]],
]

def main(): 
    for seq in SEQUENCE_A:
        decoded = [] 
        for pair in seq: 
            a = pair[0]
            b = pair[1]
            if a == 0 and b > 0:
                decoded.append('A')
            elif a == 0 and b < 0:
                decoded.append('D')
            elif a > 0 and b > 0: 
                decoded.append('B')
            elif a < 0 and b < 0:
                decoded.append('E')
            elif a > 0 and b < 0: 
                decoded.append('C')
            else: 
                decoded.append('F')
        print(decoded)

if __name__ == '__main__': 
    main()