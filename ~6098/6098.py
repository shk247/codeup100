board = [[0]*10 for _ in range(10)]

for i in range(10):
    x = list(map(int, input().split()))
    board[i] = x

y = 1
for i in range(1,10):
    for j in range(y,10):
        if board[i][j] == 0:
            board[i][j] = 9 
            continue
        if board[i][j] == 1:
            y=j-1
            break
        if board[i][j] == 2:
            break
    if board[i][j] == 2:
        board[i][j] = 9
        break

for i in range(10):
    for j in range(10):
        print(board[i][j],end=' ')
    print()