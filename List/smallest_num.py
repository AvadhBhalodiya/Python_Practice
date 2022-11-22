nterms = int(input("Enter number of terms:-\t"))
a = []

for x in range(nterms):
    n = int(input("Num:-\t"))
    a.append(n)

print("List = ", a)

n = a[0]

for i in a:
    if i < n:
        n = i

print("Smallest Number = ", n)