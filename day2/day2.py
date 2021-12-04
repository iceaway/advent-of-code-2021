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
    print("Horizontal position: %d, vertical position: %d, sum: %d" % (horz, vert, horz*vert))
    
        

