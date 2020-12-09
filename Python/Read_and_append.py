with open("bear1.txt") as file:
    x = file.read()
with open("bear2.txt","a") as file:
    file.write(x)