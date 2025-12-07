import csv

# Writing data to CSV
data = [
    ["id", "name", "salary"],
    [1, "Uttam", 70000],
    [2, "Amit", 80000],
    [3, "Addy", 90000]
]

with open("data/employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print(f" File {file.name} created successfully !")

# Reading data from CSV
with open("data/employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print(f" File {file.name} read successfully !")