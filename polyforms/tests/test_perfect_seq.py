import pytest
from polyforms.perfect_seq import *


@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup code
    seq_storage = PerfectSeq()
    yield seq_storage  # This is where the testing happens
    # Teardown code
    # seq_storage.close()

# def test_get_name_size(setup_teardown):
#    assert len(setup_teardown.get_names()) >= 17
#
# def test_seq_start(setup_teardown):
#     seq1 = setup_teardown.get_series('SEQ_4_3_A')[0]
#     assert list(seq1[:3]) == ['A', 'C', 'B']

def test_sequence_4_3_A(setup_teardown):
    seq1 = PSequence(
        'ACB.DFE.DFE.AC.',
        [['C.', 'F.', 'F.', 'B.'], ['B.', 'E.', 'E.', 'C.']]
    )
    assert seq1.get(0) == SEQ_4_3_A[0]
    assert seq1.get(1) == SEQ_4_3_A[1]
    assert seq1.get(2) == SEQ_4_3_A[2]
    assert seq1.get(3) == SEQ_4_3_A[3]

def test_sequence_4_3_B(setup_teardown):
    seq1 = PSequence(
        'ABCB.DEFE.DEFE.ABC.',
        [['C.', 'F.', 'F.', 'B.'], ['B.', 'E.', 'E.', 'C.']]
    )
    assert seq1.get(0) == SEQ_4_3_B[0]
    assert seq1.get(1) == SEQ_4_3_B[1]
    assert seq1.get(2) == SEQ_4_3_B[2]
    assert seq1.get(3) == SEQ_4_3_B[3]

def test_sequence_4_1_A(setup_teardown):
    seq1 = PSequence(
        'ACBC.DEAEF.DFEF.ABDB.',
        [['B.', 'E.', 'E.', 'C.'], ['C.', 'F.', 'F.', 'B.']]
    )
    assert seq1.get(0) == SEQ_4_1_A[0]
    assert seq1.get(1) == SEQ_4_1_A[1]
    assert seq1.get(2) == SEQ_4_1_A[2]
    assert seq1.get(3) == SEQ_4_1_A[3]


def test_sequence_8_7_A(setup_teardown):
    seq1 = PSequence(
        'ACD..EF.AC.',
        [['CD.', 'FA.', 'AF.', 'DC.']]
    )
    assert seq1.get(0) == SEQ_8_7_A[0]
    assert seq1.get(1) == SEQ_8_7_A[1]
    assert seq1.get(2) == SEQ_8_7_A[2]
    assert seq1.get(3) == SEQ_8_7_A[3]

def test_sequence_8_7_B(setup_teardown):
    seq1 = PSequence(
        'ACBC.DEFE.AEFE.ACB.',
        [['BC.', 'FE.', 'FE.', 'CB.']]
    )
    assert seq1.get(0) == SEQ_8_7_B[0]
    assert seq1.get(1) == SEQ_8_7_B[1]
    assert seq1.get(2) == SEQ_8_7_B[2]
    assert seq1.get(3) == SEQ_8_7_B[3]


def test_sequence_8_7_C(setup_teardown):
    seq1 = PSequence(
        'ACBC.DFEF.DFEF.ACB.',
        [['BC.', 'EF.', 'EF.', 'CB.']]
    )
    assert seq1.get(0) == SEQ_8_7_C[0]
    assert seq1.get(1) == SEQ_8_7_C[1]
    assert seq1.get(2) == SEQ_8_7_C[2]
    assert seq1.get(3) == SEQ_8_7_C[3]

def test_sequence_8_7_D(setup_teardown):
    seq1 = PSequence(
        'ABCB.DEFE.DEFE.ABC.',
        [['CB.', 'FE.', 'FE.', 'BC.']]
    )
    assert seq1.get(0) == SEQ_8_7_D[0]
    assert seq1.get(1) == SEQ_8_7_D[1]
    assert seq1.get(2) == SEQ_8_7_D[2]
    assert seq1.get(3) == SEQ_8_7_D[3]



def test_sequence_8_5_A(setup_teardown):
    seq1 = PSequence(
        'ACAC.D.EFDFD.FA.B',
        [['AC.', 'FD.', 'FD.', 'CA.']]
    )
    assert seq1.get(0) == SEQ_8_5_A[0]
    assert seq1.get(1) == SEQ_8_5_A[1]
    assert seq1.get(2) == SEQ_8_5_A[2]

def test_sequence_8_5_B(setup_teardown):
    seq1 = PSequence(
        'ABCBC.DEAEFE.DEFEF.ABDBC.',
        [['BC.', 'FE.', 'EF.', 'BC.']]
    )
    assert seq1.get(0) == SEQ_8_5_B[0]
    assert seq1.get(1) == SEQ_8_5_B[1]
    assert seq1.get(2) == SEQ_8_5_B[2]

def test_sequence_8_3_A(setup_teardown):
    seq1 = PSequence(
        'ABDBD.CEAE.FDFDFA.FBDB.',
        [['BD.', 'AE.', 'EA.', 'DB.']]
    )
    assert seq1.get(0) == SEQ_8_3_A[1]
    assert seq1.get(1) == SEQ_8_3_A[2]
    assert seq1.get(2) == SEQ_8_3_A[3]


def test_sequence_8_3_B(setup_teardown):
    seq1 = PSequence(
        'ABC.DFE.DEF.AC.',
        [['BC.', 'FE.', 'EF.', 'BC.']]
    )
    assert seq1.get(0) == SEQ_8_3_B[0]
    assert seq1.get(1) == SEQ_8_3_B[1]
    assert seq1.get(2) == SEQ_8_3_B[2]


def test_sequence_8_3_C(setup_teardown):
    seq1 = PSequence(
        'ABC.DEF.DFE.AC.',
        [['BC.', 'EF.', 'FE.', 'BC.']]
    )
    assert seq1.get(0) == SEQ_8_3_C[0]
    assert seq1.get(1) == SEQ_8_3_C[1]
    assert seq1.get(2) == SEQ_8_3_C[2]


def test_sequence_8_3_D(setup_teardown):
    seq1 = PSequence(
        'ACB.DFE.DEF.AB.',
        [['CB.','FE.','EF.','CB.']]
    )
    assert seq1.get(0) == SEQ_8_3_D[0]
    assert seq1.get(1) == SEQ_8_3_D[1]
    assert seq1.get(2) == SEQ_8_3_D[2]


def test_sequence_8_3_E(setup_teardown):
    seq1 = PSequence(
        'ACB.DEF.DFE.AB.',
        [['CB.', 'EF.', 'FE.', 'CB.']]
    )
    assert seq1.get(0) == SEQ_8_3_E[0]
    assert seq1.get(1) == SEQ_8_3_E[1]
    assert seq1.get(2) == SEQ_8_3_E[2]


def test_sequence_8_1_A(setup_teardown):
    seq1 = PSequence(
        'ACAC.EDFDF.EACAC.DBF',
        [['AC.','DFDF.','AC.']]
    )
    assert seq1.get(0) == SEQ_8_1_A[0]
    assert seq1.get(1) == SEQ_8_1_A[1]
    assert seq1.get(2) == SEQ_8_1_A[2]


# =========== SEQ_8_1_B ===========
# ACBCDEAFEDFEFABDC
# A(CB)CBCDEA(FE)FED(FE)FEFABD(CB)C
# A(CBCB)CBCDEA(FEFE)FED(FEFE)FEFABD(CBCB)C
# A(CBCBCB)CBCDEA(FEFEFE)FED(FEFEFE)FEFABD(CBCBCB)C

def test_sequence_8_1_B(setup_teardown):
    seq1 = PSequence(
        'ACBC.DEAFE.DFEF.ABDC.',
        [['BC.','FE.','EF.','BC.']]
    )
    assert seq1.get(0) == SEQ_8_1_B[0]
    assert seq1.get(1) == SEQ_8_1_B[1]
    assert seq1.get(2) == SEQ_8_1_B[2]











# =========== SEQ_8_1_A ===========
# ACACEDFDFEACACDBF
# (AC)ACACE(DFDF)DFDFE(AC)ACACDBF
# (ACAC)ACACE(DFDFDFDF)DFDFE(ACAC)ACACDBF
# (ACACAC)ACACE(DFDFDFDFDFDF)DFDFE(ACACAC)ACACDBF
# =========== SEQ_8_1_B ===========
# ACBCDEAFEDFEFABDC
# A(CB)CBCDEA(FE)FED(FE)FEFABD(CB)C
# A(CBCB)CBCDEA(FEFE)FED(FEFE)FEFABD(CBCB)C
# A(CBCBCB)CBCDEA(FEFEFE)FED(FEFEFE)FEFABD(CBCBCB)C
# =========== SEQ_6_5_A ===========
# ACBACBDFEDFEDFEDFEACBAC
# A(B)CBACBDFEDFED(E)FED(E)FEACB(AC)AC(B)
# (ACB)ACBACB(DFEDFE)DFEDFEDFEDFE(ACB)ACBAC
# (ABCB)ACBACB(DFEDFE)DFED(E)FED(E)FEDFE(ACB)ACB(AC)AC(B)
# =========== SEQ_6_5_B ===========
# ACBACBDFEDFEDFEDFEACBAC
# ACBA(B)CBDFE(DF)DFEDFED(E)FEACB(AC)AC
# (ACB)ACBACB(DFEDF)D(E)FEDFEDFEDFEACB(AC)A(B)C
# (ACB)A(B)CBACB(DFEDFDFE)DFEDFED(E)FEDFE(ACBAC)ACBAC






def test_sequence_6_5_B(setup_teardown):
    seq1 = PSequence(
        'ACBA.B.CBDFEDFD.FEDFED.E.FEACBACA.C',
        [['.C', 'A', '.E.', '.F', 'D', '.B.'], ['.B.', '.F', 'D', '.E.', '.C', 'A']]
    )
    assert seq1.get(0) == SEQ_6_5_B[1]
    assert seq1.get(1) == SEQ_6_5_B[2]
    assert seq1.get(2) == SEQ_6_5_B[3]
    assert seq1.get(3) == SEQ_6_5_B[4]

