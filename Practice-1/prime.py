num = int(input("Check Prime = "))
flage = False

if num > 1:
    for x in range(2, num):
        if (num % x) == 0:
            flage = True
            break

if flage == True:
    print("Not Prime")
else:
    print("Prime")
