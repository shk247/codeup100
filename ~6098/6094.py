n = int(input())
k = list(map(int,input().split()))

#print(sorted(k)[0])

min=k[0]
for i in range(1,n):
    if(min>k[i]):
        min = k[i]

print(min)
