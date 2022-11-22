a = "<span> <s> This is Citrusbug </s> This is Dhaval <s> This is practical test 1 </s> This is Indian <s> This is practical Test 2 </s> This is Ahmedabad </span>"

s1 = "<s>"
s2 = "</s>"
t1 = a.index(s1)
t2 = a.index(s2)
res = ""
l1 = []

for x in range(t1 + len(s1) + 1, t2):
    res = res + a[x]
l1.append(res)

print("res = ", res)
print("l1 = ", l1)