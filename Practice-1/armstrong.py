num = int(input("Check Armstrong = "))
sum = 0
temp = num

while temp > 0:
    d = temp % 10
    sum = sum + d ** 3
    temp = temp // 10

if sum == num:
    print("ArmStrong = ", sum)

else:
    print("Not ArmStrong = ", sum)