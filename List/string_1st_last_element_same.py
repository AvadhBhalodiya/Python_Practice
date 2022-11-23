nterms = int(input("Enter number of strings:- "))
l1 = []

for x in range(nterms):
    n = str(input(f"String {x}:- "))
    l1.append(n)

print("List = ", l1)


def check_string(words):
    cnt = 0
    for i in words:
        if len(words) > 1 and i[0] == i[-1]:
            cnt += 1
    return cnt


print("1st & last element same string = ", check_string(l1))
