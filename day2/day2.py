with open("input.txt") as f:
    data = f.readlines()
    vert = 0
    horz = 0

    for line in data:
        direction = line.split()[0]
        change = int(line.split()[1])
        if direction == "forward":
            horz += change
        elif direction == "down":
            vert += change
        elif direction == "up":
            vert -= change
        else:
            print("Invalid movement")
    print("Part 1: Horizontal position: %d, vertical position: %d, sum: %d" % (horz, vert, horz*vert))
    
    aim = 0
    vert = 0
    horz = 0
    for line in data:
        direction = line.split()[0]
        change = int(line.split()[1])
        if direction == "forward":
            horz += change
            vert += change * aim
        elif direction == "down":
            aim += change 
        elif direction == "up":
            aim -= change
        else:
            print("Invalid movement")
        
    print("Part 2: Horizontal position: %d, vertical position: %d, sum: %d" % (horz, vert, horz*vert))

