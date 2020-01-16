def loop_opcodes():
    intcodes = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 10, 23, 1, 23, 6, 27, 1, 6, 27, 31,
                1, 13, 31, 35, 1, 13, 35, 39, 1, 39, 13, 43, 2, 43, 9, 47, 2, 6, 47, 51, 1, 51, 9, 55, 1, 55, 9, 59, 1,
                59, 6, 63, 1, 9, 63, 67, 2, 67, 10, 71, 2, 71, 13, 75, 1, 10, 75, 79, 2, 10, 79, 83, 1, 83, 6, 87, 2,
                87, 10, 91, 1, 91, 6, 95, 1, 95, 13, 99, 1, 99, 13, 103, 2, 103, 9, 107, 2, 107, 10, 111, 1, 5, 111,
                115, 2, 115, 9, 119, 1, 5, 119, 123, 1, 123, 9, 127, 1, 127, 2, 131, 1, 5, 131, 0, 99, 2, 0, 14, 0]
    intcodes[1], intcodes[2] = 12, 2
    computer = []
    position = 0
    while position <= len(intcodes):
        if intcodes[position] == 1:
            output_position = intcodes[position + 3]  # For readability
            intcodes[output_position] = intcodes[intcodes[position + 1]] + intcodes[intcodes[position + 2]]
        if intcodes[position] == 2:
            output_position = intcodes[position + 3]
            intcodes[output_position] = intcodes[intcodes[position + 1]] * intcodes[intcodes[position + 2]]
        if intcodes[position] == 99:
            for val in intcodes:
                computer.append(val)
                if val == 99:
                    break
            break
        position += 4
    print(f'Response is {computer[0]}')


loop_opcodes()
