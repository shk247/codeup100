
board = [[0]*19 for _ in range(19)]

for i in range(19):
    n = list(map(int, input().split()))
    board[i] = n 

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        board[x-1][j] = int(not bool(board[x-1][j]))
    for k in range(19):
        board[k][y-1] = int(not bool(board[k][y-1]))

for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    print()



