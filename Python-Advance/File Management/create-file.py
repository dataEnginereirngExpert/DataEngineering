# Open and read a text file
with open("data/input.txt", "r") as file:   #with open() — it automatically closes the files to avoid memroy leaks 
    content = file.read()
    print(content)

# Write to a text file
with open("data/output.txt", "w") as file:
    file.write("This is a new line of text.\n")
    file.write("Data engineers love automation!")