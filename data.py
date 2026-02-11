text = input("Enter text : ")
print("1.Overwrite ")
print("2.Write at the end ")
j = int(input("Select data : "))
f = open("data.txt")
if j == 1:
    f = open("data.txt","w")
    f.write(text)
elif j == 2:
    f = open("data.txt","a")
    f.write(text)
else:
    print("Invalid input")

     
 



