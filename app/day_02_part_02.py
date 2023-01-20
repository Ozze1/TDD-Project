
from test_day_02_part_02 import find_output

def main():
    with open('input_day_02_part_01_02') as f:
        intcode = list(map(int, f.read().strip().split(',')))
    result = find_output(intcode, 19690720)
    print(result)


if __name__ == '__main__':
    main()
