h, w = map(int, input().split())
board = [[0]*w for _ in range(h)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int,input().split())
    x = x-1
    y = y-1
    if d == 0:
        for j in range(y, y+l):
            board[x][j] = 1
    elif d==1:
        for j in range(x, x+l):
            board[j][y] = 1

for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()