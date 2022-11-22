A = [
{'a':5, 'b':10, 'c':90},
{'a':45, 'b':78}, 
{'a':90, 'c':10, 'd' : 34}
]

l1 = []

for i in A:
    for j in i.items():
        l1.append(j)
print(l1)

sum = {}

for a,b in l1:
    if a not in sum:
        sum[a] = b
    else: 
        sum[a] = sum[a] + b

print(sum)