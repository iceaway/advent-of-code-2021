with open("input.txt") as f:
    data = f.readlines()
    digit_count = len(data[0].rstrip())
    rows = 2
    cols = digit_count
    freq = [[0 for i in range(cols)] for j in range(rows)]
    for line in data:
        if len(line) >= 11:
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


    gamma_rate = 0
    for i in range(digit_count):
        if (freq[1][i] > freq[0][i]):
            gamma_rate = gamma_rate | (1 << (digit_count - 1 - i))

    epsilon_rate = gamma_rate ^ (2 ** digit_count - 1)
    pc = gamma_rate * epsilon_rate
    print("Part 1: Gamma rate: %d, epsilon rate: %d, power consumtion: %d" % 
            (gamma_rate, epsilon_rate, pc))


    
