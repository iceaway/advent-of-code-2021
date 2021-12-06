def frequency(data, cols):
    rows = 2
    freq = [[0 for i in range(cols)] for j in range(rows)]
    for line in data:
        if len(line) >= digit_count:
            stripped = line.rstrip()
            for i in range(digit_count):
                if stripped[i] == '1':
                    freq[1][i] += 1
                elif stripped[i] == '0':
                    freq[0][i] += 1
                else:
                    print("Invalid input")
        else:
            print("Invalid line length")

    return freq

with open("input.txt") as f:
    data = f.readlines()
    digit_count = len(data[0].rstrip())
    freq = frequency(data, digit_count)

    gamma_rate = 0
    for i in range(digit_count):
        if (freq[1][i] > freq[0][i]):
            gamma_rate = gamma_rate | (1 << (digit_count - 1 - i))

    epsilon_rate = gamma_rate ^ (2 ** digit_count - 1)
    pc = gamma_rate * epsilon_rate
    print("==== Part 1 ====")
    print("Gamma rate: %d, epsilon rate: %d, power consumtion: %d" % 
            (gamma_rate, epsilon_rate, pc))

    
    kept_lines = data
    for i in range(digit_count):
        tmp = []
        for line in kept_lines:
            line = line.rstrip()
            if len(line) >= digit_count:
                if (freq[1][i] >= freq[0][i]):
                    if line[i] == '1':
                        tmp.append(line)
                else:
                    if line[i] == '0':
                        tmp.append(line)
        kept_lines = tmp
        freq = frequency(kept_lines, digit_count)
        if len(kept_lines) == 1:
            break

    oxygen_gen_rating = 0
    for i in range(len(kept_lines[0])):
        if kept_lines[0][i] == '1':
            oxygen_gen_rating = oxygen_gen_rating | (1 << (digit_count - 1 - i))
    print("==== Part 2 ====")
    print("Oxygen generator rating: %d" % oxygen_gen_rating)

    kept_lines = data
    for i in range(digit_count):
        tmp = []
        for line in kept_lines:
            line = line.rstrip()
            if len(line) >= digit_count:
                if (freq[0][i] <= freq[1][i]):
                    if line[i] == '0':
                        tmp.append(line)
                else:
                    if line[i] == '1':
                        tmp.append(line)
        kept_lines = tmp
        freq = frequency(kept_lines, digit_count)
        if len(kept_lines) == 1:
            break

    co2_scrub_rating = 0
    for i in range(len(kept_lines[0])):
        if kept_lines[0][i] == '1':
            co2_scrub_rating = co2_scrub_rating | (1 << (digit_count - 1 - i))

    print("CO2 scrub rating: %d" % co2_scrub_rating)
    print("Life support rating: %d" % (co2_scrub_rating * oxygen_gen_rating))
    
