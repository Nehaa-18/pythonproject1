word=input("Enter the word :")
w=word[0]
for i in word :
    if i==w:
        word=word.replace(i,"$")
        word=w+word[1: ]
print(word)