n=int(input())
b=[]
d=[]
for i in range(0,n):
    a=int(input())
    b.append(a)
    
for i in range(0,n):
    c=int(input())
    d.append(c)

if (len(b) != len(d)):
    print("Arrays are not equal.")
else:
    b.sort()
    d.sort()
    for i in range(len(b)):
        if (b[i] != d[i]):
            print("Arrays are not equal.")
            break
    else:
        print("Arrays are equal.")
    
        
