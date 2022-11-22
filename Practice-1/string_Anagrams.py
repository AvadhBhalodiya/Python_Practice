# avadh , vaahd both sorted and match result both are aadhv, it means anagram.

s1 = input("Enter 1st String:-\n")
s2 = input("Enter 2nd String:-\n")

def anagramCheck(s1,s2):
    if(sorted(s1)==sorted(s2)):
        return True
    else:
        return False

if anagramCheck(s1,s2):
    print("Anagram")
else:
    print("Not Anagram")