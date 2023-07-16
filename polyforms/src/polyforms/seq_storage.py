from ..core.perfect_seq import *

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
        return self.all_sequences.keys

    def get_sequence(self, name):
        if name in self.all_sequences:
            return self.all_sequences[name]
        else:
            return None
