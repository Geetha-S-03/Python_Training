
a=input()
b=list(a)
l=len(a)

for i in range(0,l-1):
    for j in range(i+1,l):
        if(b[i]>b[j]):
            temp=b[i]
            b[i]=b[j] 
            b[j]=temp
  
c=''.join(b)
print("Sorted array:",c)
   

