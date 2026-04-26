students = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronuu": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell Terrier"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None}
]

for student in students:
    print(student["Name"], student["House"], sep = ", ")

