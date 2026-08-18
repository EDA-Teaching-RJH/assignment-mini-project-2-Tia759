from results import result
from results import result_2
from results import results_3

def test_result():
    assert result(1) == "Computer Win!"
    assert result (2) == "Human Win!"