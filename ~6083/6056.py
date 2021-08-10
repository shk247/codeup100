a, b = input().split()

a = bool(int(a))
b = bool(int(b))

#if (a and (not b)) or (not(a) and b):
#    print("True")
#else:
#    print("False")

print((a and (not b)) or (not(a) and b))