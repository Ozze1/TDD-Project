
from app.day_02_part_01 import run_intcode
def test_run_intcode():
    assert run_intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert run_intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert run_intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert run_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
