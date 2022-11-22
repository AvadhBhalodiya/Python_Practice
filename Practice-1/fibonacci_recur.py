nterms = int(input("Enter Number of terms"))

def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))

if nterms <= 0:
    print("Please enter positive number")
else:
    print("Fibonacci Series : ")
    for x in  range(nterms):
        print(fib(x))
