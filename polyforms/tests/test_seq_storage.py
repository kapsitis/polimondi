import pytest
from polyforms.seq_storage import *


@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup code
    seq_storage = SeqStorage()
    yield seq_storage  # This is where the testing happens
    # Teardown code
    # seq_storage.close()

def test_get_name_size(setup_teardown):
   assert len(setup_teardown.get_names()) >= 17

def test_seq_start(setup_teardown):
    seq1 = setup_teardown.get_sequence('SEQUENCE_4_3_A')[0]
    assert seq1[:3] == ['A', 'C', 'B']

