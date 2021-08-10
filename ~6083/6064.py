a, b, c = map(int, input().split())

result = (a if a<c else c) if a<b else (b if b<c else c)

print(result)