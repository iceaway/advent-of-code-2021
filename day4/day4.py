def check_board(board):
    # Check horizontal bingo
    for r in range(len(board)):
        count = 0
        for c in range(len(board[r])):
            if board[r][c] == 'X':
                count += 1

            if count == 5:
                return True
                
    # Check vertical bingo
    for c in range(len(board[0])):
        count = 0
        for r in range(len(board)):
            if board[r][c] == 'X':
                count += 1

            if count == 5:
                return True
                
    return False
    
with open("input.txt") as f:
    data = f.readlines()
    numbers = data[0].rstrip().split(',')
    del data[0]
    del data[0]
    index = 0
    boards = []
    tmp = []
    for line in data:
        if (len(line) > 2):
            tmp.append(line.rstrip().split())
            index += 1

        if index >= 5:
            index = 0
            boards.append(tmp)
            tmp = []
    print("Boards: %d" % len(boards))

    ln = -1
    wb = -1
    for n in numbers:
        for b in range(len(boards)):
            for r in range(len(boards[b])):
                for c in range(len(boards[b][r])):
                    if n == boards[b][r][c]:
                        boards[b][r][c] = 'X'

        for b in range(len(boards)):
            if check_board(boards[b]) == True:
                print("Board %d bingo!" % (b+1))
                print("Last number called: %s" % n)
                ln = int(n)
                wb = int(b)
                break
        else:
            continue
        break

    if wb == -1 or ln == -1:
        print("No winner!")
    else:

        sum = 0
        for r in boards[wb]:
            print(r)
            for c in r:
                if c != 'X':
                    sum += int(c)
        print("Board sum: %d" % (sum * ln))
                            
