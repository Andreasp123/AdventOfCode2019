
def calculate_fuel():
    input = read_input()
    required_fuel = sum([int(module / 3 - 2) for module in input])
    print(required_fuel)  # 3323874 - part 1
    actual_required_fuel = sum([int(calculate_additional_fuel(module)) for module in input])
    print(f'Actual required fuel: {actual_required_fuel}')  # 4982961 - part2


def calculate_additional_fuel(fuel):
    additional_fuel = 0
    while fuel > 0:
        fuel = int(fuel / 3 - 2)
        additional_fuel += fuel if fuel > 0 else 0
    return additional_fuel


def read_input():
    with open('input_day1.txt', 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]


if __name__ == '__main__':

    calculate_fuel()