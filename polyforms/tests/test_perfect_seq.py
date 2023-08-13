import pytest
from polyforms.perfect_seq import *


@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup code
    seq_storage = PerfectSeq()
    yield seq_storage  # This is where the testing happens
    # Teardown code
    # seq_storage.close()

def test_get_name_size(setup_teardown):
   assert len(setup_teardown.get_names()) >= 17

def test_seq_start(setup_teardown):
    seq1 = setup_teardown.get_series('SEQ_4_3_A')[0]
    assert list(seq1[:3]) == ['A', 'C', 'B']

