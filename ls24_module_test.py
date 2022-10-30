""""An example of a test module in pytest.""""

from ls24_module import total

def test_total_empty() -> None:
     assert total([]) == 0.0

//test
