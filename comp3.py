word=input("Enter your word :")
vow="aeiou"
for i in word:
    j=i.split(",")
    for x in vow:
        v=x.split(",")
        if j==v:
            print(v)