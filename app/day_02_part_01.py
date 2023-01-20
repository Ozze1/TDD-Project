
from test_day_02_part_01 import run_intcode

def main():
    with open('input_day_02_part_01_02') as f:
        intcode = list(map(int, f.read().strip().split(',')))
    intcode[1] = 12
    intcode[2] = 2
    intcode = run_intcode(intcode)
    print(intcode[0])

if __name__ == '__main__':
    main()



