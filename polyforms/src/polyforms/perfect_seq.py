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

SEQ_4_3_A = [
    'ACBDFEDFEAC',
    'ACBCDFEFDFEFACB',
    'ACBCBDFEFEDFEFEACBC',
    'ACBCBCDFEFEFDFEFEFACBCB',
    'ACBCBCBDFEFEFEDFEFEFEACBCBC',
    'ACBCBCBCDFEFEFEFDFEFEFEFACBCBCB'
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

SEQ_4_3_B = [
    'ABCBDEFEDEFEABC',
    'ABCBCDEFEFDEFEFABCB',
    'ABCBCBDEFEFEDEFEFEABCBC',
    'ABCBCBCDEFEFEFDEFEFEFABCBCB',
    'ABCBCBCBDEFEFEFEDEFEFEFEABCBCBC'
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

SEQ_4_1_A = [
    'ACBCDEAEFDFEFABDB',
    'ACBCBDEAEFEDFEFEABDBC',
    'ACBCBCDEAEFEFDFEFEFABDBCB',
    'ACBCBCBDEAEFEFEDFEFEFEABDBCBC',
    'ACBCBCBCDEAEFEFEFDFEFEFEFABDBCBCB',
    'ACBCBCBCBDEAEFEFEFEDFEFEFEFEABDBCBCBC'
]

# k --> k+8 (where k mod 8 = 7)
# 7, 15, 23, 31, ...
SEQUENCE_8_7_A = [
    ['A', 'C', 'D', 'E', 'F', 'A', 'C'],
    ['A', 'C', 'D', 'C', 'D', 'F', 'A', 'E', 'F', 'A', 'F', 'A', 'C', 'D', 'C'],
    ['A', 'C', 'D', 'C', 'D', 'C', 'D', 'F', 'A', 'F', 'A', 'E', 'F', 'A', 'F', 'A', 'F', 'A', 'C', 'D', 'C', 'D', 'C'],
    ['A', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'F', 'A', 'F', 'A', 'F', 'A', 'E', 'F', 'A', 'F', 'A', 'F', 'A', 'F', 'A', 'C', 'D', 'C', 'D', 'C', 'D', 'C']
]

SEQ_8_7_A = [
    'ACDEFAC',
    'ACDCDFAEFAFACDC',
    'ACDCDCDFAFAEFAFAFACDCDC',
    'ACDCDCDCDFAFAFAEFAFAFAFACDCDCDC'
]

# k --> k+8 (where k mod 8 = 7)
# 7, 15, 23, ...
SEQUENCE_8_7_B = [
    ['A', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'A', 'E', 'F', 'E', 'A', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B', 'C', 'B']
]

SEQ_8_7_B = [
    'ACBCDEFEAEFEACB',
    'ACBCBCDEFEFEAEFEFEACBCB',
    'ACBCBCBCDEFEFEFEAEFEFEFEACBCBCB'
]

# k --> k+8 (where k mod 8 = 7)
# 7, 15, 23, ...
SEQUENCE_8_7_C = [
    ['A', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'A', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B', 'C', 'B']
]

SEQ_8_7_C = [
    'ACBCDFEFDFEFACB',
    'ACBCBCDFEFEFDFEFEFACBCB',
    'ACBCBCBCDFEFEFEFDFEFEFEFACBCBCB'
]

# k --> k+8 (where k mod 8 = 7)
# 7, 15, 23, ...
SEQUENCE_8_7_D = [
    ['A', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'A', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C', 'B', 'C']
]

SEQ_8_7_D = [
    'ABCBDEFEDEFEABC',
    'ABCBCBDEFEFEDEFEFEABCBC',
    'ABCBCBCBDEFEFEFEDEFEFEFEABCBCBC'
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

SEQ_8_5_A = [
    'ACEDF',
    'ACACDEFDFDFAB',
    'ACACACDFDEFDFDFDFACAB',
    'ACACACACDFDFDEFDFDFDFDFACACAB'
]

# k --> k+8 (where k mod 8 = 5)
# 21, 29, 37
SEQUENCE_8_5_B = [
    ['A', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'B', 'C', 'B', 'C', 'B', 'C']
]

SEQ_8_5_B = [
    'ABCBCDEAEFEDEFEFABDBC',
    'ABCBCBCDEAEFEFEDEFEFEFABDBCBC',
    'ABCBCBCBCDEAEFEFEFEDEFEFEFEFABDBCBCBC'
]

# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_A = [
    ['A', 'B', 'D', 'C', 'E', 'F', 'D', 'E', 'A', 'F', 'B'],
    ['A', 'B', 'D', 'B', 'D', 'C', 'E', 'A', 'E', 'F', 'D', 'F', 'D', 'F', 'A', 'F', 'B', 'D', 'B'],
    ['A', 'B', 'D', 'B', 'D', 'B', 'D', 'C', 'E', 'A', 'E', 'A', 'E', 'F', 'D', 'F', 'D', 'F', 'A', 'E', 'A', 'F', 'B', 'D', 'B', 'D', 'B'],
    ['A', 'B', 'D', 'B', 'D', 'B', 'D', 'B', 'D', 'C', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'F', 'D', 'F', 'D', 'F', 'A', 'E', 'A', 'E', 'A', 'F', 'B', 'D', 'B', 'D', 'B', 'D', 'B']
]

SEQ_8_3_A = [
    'ABDCEFDEAFB',
    'ABDBDCEAEFDFDFAFBDB',
    'ABDBDBDCEAEAEFDFDFAEAFBDBDB',
    'ABDBDBDBDCEAEAEAEFDFDFAEAEAFBDBDBDB'
]

# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_B = [
    ['A', 'B', 'C', 'D', 'F', 'E', 'D', 'E', 'F', 'A', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'C', 'B', 'C', 'B', 'C', 'B', 'C']
]

SEQ_8_3_B = [
    'ABCDFEDEFAC',
    'ABCBCDFEFEDEFEFACBC',
    'ABCBCBCDFEFEFEDEFEFEFACBCBC',
    'ABCBCBCBCDFEFEFEFEDEFEFEFEFACBCBCBC'
]


# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_C = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'D', 'F', 'E', 'A', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B', 'C'],
    ['A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'C', 'B', 'C', 'B', 'C', 'B', 'C']
]

SEQ_8_3_C = [
    'ABCDEFDFEAC',
    'ABCBCDEFEFDFEFEACBC',
    'ABCBCBCDEFEFEFDFEFEFEACBCBC',
    'ABCBCBCBCDEFEFEFEFDFEFEFEFEACBCBCBC'
]

# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_D = [
    ['A', 'C', 'B', 'D', 'F', 'E', 'D', 'E', 'F', 'A', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'A', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
]

SEQ_8_3_D = [
    'ACBDFEDEFAB',
    'ACBCBDFEFEDEFEFABCB',
    'ACBCBCBDFEFEFEDEFEFEFABCBCB',
    'ACBCBCBCBDFEFEFEFEDEFEFEFEFABCBCBCB'
]

# k --> k+8 (where k mod 8 = 3)
# 11, 19, 27, 35
SEQUENCE_8_3_E = [
    ['A', 'C', 'B', 'D', 'E', 'F', 'D', 'F', 'E', 'A', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C', 'B'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'E', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
]

SEQ_8_3_E = [
    'ACBDEFDFEAB',
    'ACBCBDEFEFDFEFEABCB',
    'ACBCBCBDEFEFEFDFEFEFEABCBCB',
    'ACBCBCBCBDEFEFEFEFDFEFEFEFEABCBCBCB'
]

# k --> k+8 (where k mod 8 = 1)
SEQUENCE_8_1_A = [
    ['A', 'C', 'A', 'C', 'E', 'D', 'F', 'D', 'F', 'E', 'A', 'C', 'A', 'C', 'D', 'B', 'F'],
    ['A', 'C', 'A', 'C', 'A', 'C', 'E', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'E', 'A', 'C', 'A', 'C', 'A', 'C', 'D', 'B', 'F'],
    ['A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'E', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'D', 'F', 'E', 'A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'D', 'B', 'F']
]

SEQ_8_1_A = [
    'ACACEDFDFEACACDBF',
    'ACACACEDFDFDFDFEACACACDBF',
    'ACACACACEDFDFDFDFDFDFEACACACACDBF'
]

# k --> k+8 (where k mod 8 = 1)
SEQUENCE_8_1_B = [
    ['A', 'C', 'B', 'C', 'D', 'E', 'A', 'F', 'E', 'D', 'F', 'E', 'F', 'A', 'B', 'D', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'C', 'B', 'C'],
    ['A', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'D', 'E', 'A', 'F', 'E', 'F', 'E', 'F', 'E', 'D', 'F', 'E', 'F', 'E', 'F', 'E', 'F', 'A', 'B', 'D', 'C', 'B', 'C', 'B', 'C']
]

SEQ_8_1_B = [
    'ACBCDEAFEDFEFABDC',
    'ACBCBCDEAFEFEDFEFEFABDCBC',
    'ACBCBCBCDEAFEFEFEDFEFEFEFABDCBCBC'
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

SEQ_6_5_A = [
    'ACBACBDFEDFEDFEDFEACBAC',
    'ABCBACBDFEDFEDEFEDEFEACBACACB',
    'ACBACBACBDFEDFEDFEDFEDFEDFEACBACBAC',
    'ABCBACBACBDFEDFEDFEDEFEDEFEDFEACBACBACACB',
    'ACBACBACBACBDFEDFEDFEDFEDFEDFEDFEDFEACBACBACBAC'
]

# k --> k+6 (where k mod 6 = 5)
SEQUENCE_6_5_B = [
    ['A', 'C', 'B', 'A', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'A', 'C', 'B', 'A', 'C'],
    ['A', 'C', 'B', 'A', 'B', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'E', 'F', 'E', 'A', 'C', 'B', 'F', 'C', 'F', 'C'],
    ['A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'D', 'F', 'E', 'D', 'F', 'D', 'E', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'D', 'F', 'E', 'A', 'C', 'B', 'A', 'C', 'F', 'B', 'C']
]

SEQ_6_5_B = [
    'ACBACBDFEDFEDFEDFEACBAC',
    'ACBABCBDFEDFDFEDFEDEFEACBACAC',
    'ACBACBACBDFEDFDEFEDFEDFEDFEACBACFBC'
]

# Blue color: 2D9BF0
# Green color: 8FD14E


class PerfectSeq:
    all_sequences = None

    @classmethod
    def dict_init(cls):
        if not cls.all_sequences:
            cls.all_sequences = {}
            cls.all_sequences['SEQ_4_3_A'] = SEQ_4_3_A
            cls.all_sequences['SEQ_4_3_B'] = SEQ_4_3_B
            cls.all_sequences['SEQ_4_1_A'] = SEQ_4_1_A
            cls.all_sequences['SEQ_8_7_A'] = SEQ_8_7_A
            cls.all_sequences['SEQ_8_7_B'] = SEQ_8_7_B
            cls.all_sequences['SEQ_8_7_C'] = SEQ_8_7_C
            cls.all_sequences['SEQ_8_7_D'] = SEQ_8_7_D
            cls.all_sequences['SEQ_8_5_A'] = SEQ_8_5_A
            cls.all_sequences['SEQ_8_5_B'] = SEQ_8_5_B
            cls.all_sequences['SEQ_8_3_A'] = SEQ_8_3_A
            cls.all_sequences['SEQ_8_3_B'] = SEQ_8_3_B
            cls.all_sequences['SEQ_8_3_C'] = SEQ_8_3_C
            cls.all_sequences['SEQ_8_3_D'] = SEQ_8_3_D
            cls.all_sequences['SEQ_8_3_E'] = SEQ_8_3_E
            cls.all_sequences['SEQ_8_1_A'] = SEQ_8_1_A
            cls.all_sequences['SEQ_8_1_B'] = SEQ_8_1_B
            cls.all_sequences['SEQ_6_5_A'] = SEQ_6_5_A
            cls.all_sequences['SEQ_6_5_B'] = SEQ_6_5_B


    def __init__(self):
        self.dict_init()

    def get_names(self):
        return self.all_sequences.keys()

    def get_sequence(self, name):
        if name in self.all_sequences:
            return self.all_sequences[name]
        else:
            return None
