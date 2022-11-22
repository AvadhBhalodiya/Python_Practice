d1 = {
    "a":"India",
    "101":"USA",
    "231":"Pakistan",
    "arg":"Argentina",
    "c":"Bhutan",
    "X":"Srilanka",
    "D":"India",
    "34":"Australia"
}

word = input("Enter Country  Name:")

value = [k for k in d1 if d1[k]==word ]

print(value)