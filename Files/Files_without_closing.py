with open("Filesc.txt","w") as new_file:
    new_file.write("This is a file created to check with\n")

with open("Filesc.txt",mode='a') as new_file:
    print(new_file.write("This is the appended line"))


with open("Filesc.txt",mode='r') as new_file:
    print(new_file.read())