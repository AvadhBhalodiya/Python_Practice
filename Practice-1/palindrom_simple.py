n = int(input("Chaek Plindrom Or Not?\n"))

rev = 0
temp = n

while temp!=0:
    rev = rev*10 + temp%10
    temp //= 10

if rev == n:
    print("Planidrom")
else:
    print("Not Palindrom")
