n=int(input())
b=[]
c=0
for i in range(0,n):
    a=int(input())
    b.append(a)
for i in range(0,n):
    for j in range(i+1,n):
        if(b[i]==b[j]):
            c=c+1
if(c==0):
    print("No repetative element")
    
else:
    for i in range(n):
        for j in range(i+1,n):
            if(b[i]==b[j]):
                print(b[i])
