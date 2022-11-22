# 6 is a positive number and its divisor is 1,2,3 and 6 itself.
# But we should not include 6 as by the definition of perfect number.
# Lets add its divisor excluding itself
# 1+2+3 = 6 which is equal to number itself.
# It means 6 is a Perfect Number.

n = int(input("Enter Number:-\n"))
s=0

for i in range(1,(n//2)+1):
    r = n % i
    if r == 0:
        s = s + i

if n == s:
    print("Number is Perfect")
else:
    print("Not Perfect")