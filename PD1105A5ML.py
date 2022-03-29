##How do you count the occurrence of a given character in a string?

string = "bubbles are bubbly"
count = 0
choice = (input("Choose a character: "))
for i in string:
    if i == choice:
        count += 1
print(count)

