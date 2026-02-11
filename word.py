f = open("data.txt","r")
text = f.read()
print("Sentence", text , end = " ")
space = 1
for char in text:
    if char == ' ':
        space += 1
print(f"From file Countable {space} word")
f.close()
