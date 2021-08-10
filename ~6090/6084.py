h, b, c, s = map(int, input().split())

print(format(h*b*c*s/1024/1024/8, ".1f"), "MB")