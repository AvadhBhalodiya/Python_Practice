nterms = int(input("Enter number of terms: - "))

n1, n2 = 0, 1
cnt = 0

if nterms <= 0:
    print("Please enter positive int!")
elif nterms == 1:
    print("Fibonaci : - ", n1)
elif nterms == 2:
    print("Fibonaci : - ", n1, n2)
else:
    while cnt < nterms:
        print(n1)
        n = n1 + n2

        n1 = n2
        n2 = n
        cnt += 1