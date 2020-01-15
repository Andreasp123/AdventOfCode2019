

def read_input():
    with open('input_day2.txt', 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]

def loop_opcodes():
    intcodes = read_input()
    copy = intcodes
    position = 0
    while position <= len(intcodes):
        if intcodes[position] == 1:
            intcodes[position +3] = intcodes[position + 1] + intcodes[position + 2]
        if intcodes[position] == 2:
            intcodes[position + 3] = intcodes[position + 1] * intcodes[position + 2]
if __name__ == '__main__':
    read_input()