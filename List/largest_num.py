nterms = int(input("Enter number of terms:-\t"))
a = []

for x in range(nterms):
    n = int(input("Num:-\t"))
    a.append(n)

print("List = ", a)

n = [0]

for i in range(len(a)):
    if a[i] > n[0]:
        n[0] = a[i]

print("Largest Number = ", n)