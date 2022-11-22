d1 = {
    "a":["green", "red", "blue"]
}

d2 = {
    "b":["green", "yellow", "red"]
}

l1 = []
l2 = []

for i in d1.values():
    for j in i:
        l1.append(j)
        
for i in d2.values():
    for j in i:
        l2.append(j)

c = set(l1) & set(l2)
print("C = ",c)

l3 = list(c)

print(l3)

d3 = {}

d3["a"] = l3[0]
d3["b"] = l3[1]

print(d3)