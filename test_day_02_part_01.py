
def run_intcode(intcode):
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if opcode == 99:
            return intcode
        elif opcode == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        elif opcode == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        else:
            raise ValueError(f'Invalid opcode: {opcode}')
    return intcode

def test_run_intcode():
    assert run_intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert run_intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert run_intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert run_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
