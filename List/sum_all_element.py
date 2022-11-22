nterms = int(input("Enter number of terms:-\t"))
a = []

for x in range(nterms):
    n = int(input("Num:-\t"))
    a.append(n)

s = 0

print("List = ", a)

for i in a:
    s = s + i

print("Sum = ", s)
