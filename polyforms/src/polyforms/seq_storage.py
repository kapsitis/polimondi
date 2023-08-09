# from polyforms.perfect_seq import *



# k --> k+4 (where k mod 4 == 3)
# 11, 15, 19, 23, 27, 31, ...
SEQUENCE_4_3_A = [
    ['A', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'E', 'A', 'C'],
    ['A', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'A', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B', 'C', 'B']
]

# k --> k+4 (where k mod 4 = 3)
# 15, 19, 23, 27, 31, ...
SEQUENCE_4_3_B = [
    ['A', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'A', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'D', 'E', 'F', 'E', 'F', 'A', 'B', 'C', 'B'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'C', 'B', 'C', 'B'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C', 'B', 'C']
]

# k --> k+4 (where k mod 4 = 1)
# 17, 21, 25, 29, 33, 37, ...
SEQUENCE_4_1_A = [
    ['A', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'D', 'F', 'E', 'F', 'A', 'B', 'D', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'D', 'E', 'A', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'A', 'B', 'D', 'B', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'D', 'B', 'C', 'B', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'B', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'D', 'B', 'C', 'B', 'C', 'B', 'C']
]

# k --> k+8 (where k mod 8 = 7)
# 7, 15, 23, 31, ...
SEQUENCE_8_7_A = [
    ['A', 'C', 'D', 'E', 'F', 'A', 'C'],
    ['A', 'C', 'D', 'C', 'D', 'F', 'A', 'E', 'F', 'A', 'F', 'A', 'C', 'D', 'C'],
    ['A', 'C', 'D', 'C', 'D', 'C', 'D', 'F', 'A', 'F', 'A', 'E', 'F', 'A', 'F', 'A', 'F', 'A', 'C', 'D', 'C', 'D', 'C'],
    ['A', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'F', 'A', 'F', 'A', 'F', 'A', 'E', 'F', 'A', 'F', 'A', 'F', 'A', 'F', 'A', 'C', 'D', 'C', 'D', 'C', 'D', 'C']
]

# k --> k+8 (where k mod 8 = 7)
# 7, 15, 23, ...
SEQUENCE_8_7_B = [
    ['A', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'A', 'E', 'F', 'E', 'A', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B', 'C', 'B']
]

# k --> k+8 (where k mod 8 = 7)
# 7, 15, 23, ...
SEQUENCE_8_7_C = [
    ['A', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'A', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B', 'C', 'B']
]

# k --> k+8 (where k mod 8 = 7)
# 7, 15, 23, ...
SEQUENCE_8_7_D = [
    ['A', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'A', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C', 'B', 'C']
]


# k --> k+8 (where k mod 8 = 5)
# 5, 13, 21, ...
SEQUENCE_8_5_A = [
    #['C', 'E', 'A', 'F', 'B'],
    ['A', 'C', 'E', 'D', 'F'],
    ['A', 'C', 'A', 'C', 'D', 'E', 'F', 'D', 'F', 'D', 'F', 'A', 'B'],
    ['A', 'C', 'A', 'C', 'A', 'C', 'D', 'F', 'D', 'E', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'A', 'C', 'A', 'B'],
    ['A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'D', 'F', 'D', 'F', 'D', 'E', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'A', 'C', 'A', 'C', 'A', 'B']
]

# k --> k+8 (where k mod 8 = 5)
# 21, 29, 37
SEQUENCE_8_5_B = [
    ['A', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'B', 'C', 'B', 'C', 'B', 'C']
]

# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_A = [
    ['A', 'B', 'D', 'C', 'E', 'F', 'D', 'E', 'A', 'F', 'B'],
    ['A', 'B', 'D', 'B', 'D', 'C', 'E', 'A', 'E', 'F', 'D', 'F', 'D', 'F', 'A', 'F', 'B', 'D', 'B'],
    ['A', 'B', 'D', 'B', 'D', 'B', 'D', 'C', 'E', 'A', 'E', 'A', 'E', 'F', 'D', 'F', 'D', 'F', 'A', 'E', 'A', 'F', 'B', 'D', 'B', 'D', 'B'],
    ['A', 'B', 'D', 'B', 'D', 'B', 'D', 'B', 'D', 'C', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'F', 'D', 'F', 'D', 'F', 'A', 'E', 'A', 'E', 'A', 'F', 'B', 'D', 'B', 'D', 'B', 'D', 'B']
]

# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_B = [
    ['A', 'B', 'C', 'D', 'F', 'E', 'D', 'E', 'F', 'A', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B', 'C', 'B', 'C']
]


# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_C = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'D', 'F', 'E', 'A', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B', 'C', 'B', 'C']
]

# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_D = [
    ['A', 'C', 'B', 'D', 'F', 'E', 'D', 'E', 'F', 'A', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'A', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
]

# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_E = [
    ['A', 'C', 'B', 'D', 'E', 'F', 'D', 'F', 'E', 'A', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
]

# k --> k+8 (where k mod 8 = 1)
SEQUENCE_8_1_A = [
    ['A', 'C', 'A', 'C', 'E', 'D', 'F', 'D', 'F', 'E', 'A', 'C', 'A', 'C', 'D', 'B', 'F'],
    ['A', 'C', 'A', 'C', 'A', 'C', 'E', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'E', 'A', 'C', 'A', 'C', 'A', 'C', 'D', 'B', 'F'],
    ['A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'E', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'E', 'A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'D', 'B', 'F']
]

# k --> k+8 (where k mod 8 = 1)
SEQUENCE_8_1_B = [
    ['A', 'C', 'B', 'C', 'D', 'E', 'A', 'F', 'E', 'D', 'F', 'E', 'F', 'A', 'B', 'D', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'C', 'B', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'C', 'B', 'C', 'B', 'C']
]

# k --> k+6 (where k mod 6 = 5)
SEQUENCE_6_5_A = [
    ['A', 'C', 'B', 'A', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'A', 'C', 'B', 'A', 'C'],
    ['A', 'B', 'C', 'B', 'A', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'A', 'C', 'B', 'A', 'C', 'A', 'C', 'B'],
    ['A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    ['A', 'B', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'D', 'F', 'E', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'C', 'B'],
    ['A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'A', 'C', 'B', 'A', 'C', 'B', 'A',
    'C', 'B', 'A', 'C']
]



class SeqStorage:
    all_sequences = None

    @classmethod
    def dict_init(cls):
        if not cls.all_sequences:
            cls.all_sequences = {}
            cls.all_sequences['SEQUENCE_4_3_A'] = SEQUENCE_4_3_A
            cls.all_sequences['SEQUENCE_4_3_B'] = SEQUENCE_4_3_B
            cls.all_sequences['SEQUENCE_4_1_A'] = SEQUENCE_4_1_A
            cls.all_sequences['SEQUENCE_8_7_A'] = SEQUENCE_8_7_A
            cls.all_sequences['SEQUENCE_8_7_B'] = SEQUENCE_8_7_B
            cls.all_sequences['SEQUENCE_8_7_C'] = SEQUENCE_8_7_C
            cls.all_sequences['SEQUENCE_8_7_D'] = SEQUENCE_8_7_D
            cls.all_sequences['SEQUENCE_8_5_A'] = SEQUENCE_8_5_A
            cls.all_sequences['SEQUENCE_8_5_B'] = SEQUENCE_8_5_B
            cls.all_sequences['SEQUENCE_8_3_A'] = SEQUENCE_8_3_A
            cls.all_sequences['SEQUENCE_8_3_B'] = SEQUENCE_8_3_B
            cls.all_sequences['SEQUENCE_8_3_C'] = SEQUENCE_8_3_C
            cls.all_sequences['SEQUENCE_8_3_D'] = SEQUENCE_8_3_D
            cls.all_sequences['SEQUENCE_8_3_E'] = SEQUENCE_8_3_E
            cls.all_sequences['SEQUENCE_8_1_A'] = SEQUENCE_8_1_A
            cls.all_sequences['SEQUENCE_8_1_B'] = SEQUENCE_8_1_B
            cls.all_sequences['SEQUENCE_6_5_A'] = SEQUENCE_6_5_A


    def __init__(self):
        self.dict_init()

    def get_names(self):
        return self.all_sequences.keys()

    def get_sequence(self, name):
        if name in self.all_sequences:
            return self.all_sequences[name]
        else:
            return None
