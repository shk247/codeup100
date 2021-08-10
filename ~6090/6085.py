w, h, b = map(int, input().split())

print(format( (w*h*b)/1024/1024/8,".2f"), "MB")