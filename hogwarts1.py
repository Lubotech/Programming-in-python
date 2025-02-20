students = [
  {'name': 'Hermione', 'house': 'Gryffindor', 'patronus': 'Otter'},
  {'name': 'Harry', 'house': 'Gryffindor', 'patronus': 'Stag'},
  {'name': 'Ron', 'house': 'Gryffindor', 'patronus': 'Unicorn'},
  {'name': 'Hermione Granger', 'house': 'Gryffindor', 'patronus': 'Hippogriff'},
  {'name': 'Draco Malfoy', 'house': 'Slytherin', 'patronus': None},
  {'name': 'Voldemort', 'house': 'Slytherin', 'patronus': 'Imp'}
]

for student in students:
  print(student['name'], student['house'], student['patronus'],sep=', ')