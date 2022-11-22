n = int(input("Enter Number:\n"))

def rev(num):
    if num<10:
        return num
    else:
        return int(str(num%10) + str(rev(num//10)))

def Palindrom(num):
    if num == rev(num):
        return 1
    return 0

if Palindrom(n) == 1:
    print("Plalindrom")
else:
    print("Not Palindrome")
