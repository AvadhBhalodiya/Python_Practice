a=[1,55,34,26,78,85,34,56]
b=[1,56,34,21,78,83]
c=[]

for i in a:
    if i in b:
        c.append(i)
    
print("c = ",c)

for x in range(len(c)):
    for y in range(x+1, len(c)):
        if c[x] > c[y]:
            c[x], c[y] = c[y], c[x]

print("acse = ",c)

for x in range(len(c)):
    for y in range(x+1, len(c)):
        if c[x] < c[y]:
            c[x], c[y] = c[y], c[x]

print("dces = ",c)