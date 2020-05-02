string = input("Give me the text please: ")

if string[::2] == string[1::2]:
    print("They are all doubled ")

elif string[::3] == string[1::3]:
    print("They are all tripled ")

else:
    print("They are not doubled nor tripled")

