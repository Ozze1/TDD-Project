from app.day_02_part_02 import find_output, run_intcode

def test_find_output():
    assert find_output([1,0,0,0,99], 2) == 0

def test_run_intcode():
    assert run_intcode([99, 1, 2, 3], 1, 2) == [99,1,2,3]


