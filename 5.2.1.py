n=int(input())
b=[]
for i in range(0,n):
    a=int(input())
    b.append(a)

for i in range(0,n):
    c=0
    for j in range(0,n):
        if(i!=j):
            if(b[i]==b[j]):
                c=c+1
    if(c==0):
        print(b[i])
