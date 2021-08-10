a, m, d, n = map(int,input().split())

num = a
for i in range(2,n+1):
    num = num*m + d

print(num)