user_text = str(input("Enter a phrase :"))
text = user_text.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)