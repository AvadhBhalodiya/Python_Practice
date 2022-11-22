l1=[1,2,3,4]
l2=['a','b']
c=[]
n=0

for x in l1:
    c.append(x)
    for y in l2[n]:
        c.append(y)
    n=n+1

for z in l2:
    if z not in c:
        c.append(z)
    
print("C = ",c)