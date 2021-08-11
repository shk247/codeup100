n = int(input())
random = list(map(int, input().split()))

for i in reversed(range(n)):
    print(random[i], end=' ')