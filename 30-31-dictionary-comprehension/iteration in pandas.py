import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 78, 92]
}

students_df = pandas.DataFrame(student_dict)
print(students_df)
