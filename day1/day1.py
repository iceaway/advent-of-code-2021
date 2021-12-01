with open("input.txt") as f:
    # Part one
    data = f.readlines()
    inc = 0
    pnum = -1;
    data_arr = [] 
    for d in data:
        num = int(d)
        data_arr.append(num)
        if (pnum == -1):
            pnum = num;
        else:
            if (num > pnum):
                inc += 1

        pnum = num;
    print("Part one: %d" % (inc))

    # Part two
    cnt = 0
    i = 0
    inc = 0
    while True:
        if (i > (len(data_arr) - 4)):
            break
        sum_a = data_arr[i] + data_arr[i+1] + data_arr[i+2]
        sum_b = data_arr[i+1] + data_arr[i+2] + data_arr[i+3]
        if (sum_b > sum_a):
            inc += 1
        i += 1
    print("Part two: %d" % (inc))
        


