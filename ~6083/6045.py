x, y, z = input().split()

x = int(x)
y = int(y)
z = int(z)

sum = x+y+z
#avg = round(sum/3, 3)
avg = format(sum/3,".2f")

print(sum, avg)