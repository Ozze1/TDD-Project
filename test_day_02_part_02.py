
def run_intcode(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
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

def find_output(intcode, output):
    for noun in range(100):
        for verb in range(100):
            intcode_copy = intcode.copy()
            result = run_intcode(intcode_copy, noun, verb)
            if result[0] == output:
                return 100 * noun + verb
    return -1
