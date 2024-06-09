n=int(input())
b=[]
for i in range(1,n+1):
    
    a=int(input())
    b.append(a)
    print(f"Enter element {i}:",a)
s=b[1]
l=b[1]
for i in range(0,n):
    
    if(b[i]<s):
        s=b[i]
    if(b[i]>l):
        l=b[i]
print("Largest element:",l)
print("Smallest element:",s)
            
  
    
    

