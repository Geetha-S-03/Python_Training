n=int(input())
a=[]
for i in range (0,n):
    l=int(input())
    a.append(l)
print("Orginal array:",a)
l=len(a)
temp=0
for i in range(0,l):
    for j in range(i+1,l):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j] 
            a[j]=temp
print("Sorted array:")         
for i in range(0,l):
    print(a[i],end=" ")
   


