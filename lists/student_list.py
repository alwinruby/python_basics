#Create three dictionaries: lloyd, alice, and tyler.
#Give each dictionary the keys "name", "homework", "quizzes", and "tests".
#Have the "name" key be the name of the student
#(that is, lloyd's name should be "Lloyd")

#Dictionary - 1
#lloyd = {
#  "name": "Lloyd",
#  "homework": [90.0,97.0,75.0,92.0],
#  "quizzes": [88.0,40.0,94.0],
#  "tests": [75.0,90.0]
#}

lloyd = {
      "name": "Lloyd",
      "homework": [90.0,97.0,75.0,92.0],
      "quizzes": [88.0,40.0,94.0],
      "tests": [75.0,90.0]
}
print(lloyd)
print("\n")

#Dictionary - 2
# alice = {
#   "name": "Alice",
#   "homework": [100.0, 92.0, 98.0, 100.0],
#   "quizzes": [82.0, 83.0, 91.0],
#   "tests": [89.0, 97.0]
# }

alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
print(alice)
print("\n")

#Dictionary - 3

# tyler = {
#   "name": "Tyler",
#   "homework": [0.0, 87.0, 75.0, 22.0],
#   "quizzes": [0.0, 75.0, 78.0],
#   "tests": [100.0, 100.0]
# }

tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

print(tyler)
print("\n")



#Creating a list called students
students = [lloyd,alice,tyler]
for student in students:
    print("Name: ", student['name'])

    avg_homework = sum(student['homework'])/len(student['homework'])
    print("Avg Homework Score: {0:.2f}".format(avg_homework))

    avg_quiz = sum(student['quizzes'])/len(student['quizzes'])
    print("Avg Quiz Score: {0:.2f}".format(avg_quiz))

    avg_test = sum(student['tests'])/len(student['tests'])
    print("Avg Test Score: {0:.2f}".format(avg_test))


    #Get weighted average
    #Homework is 10%, quizzes are 30% and tests are 60%

    total_score = avg_homework*0.1 + avg_quiz*0.3 + avg_test*0.6
    print("Total Score: {0:.2f}".format(total_score))


    if total_score >= 90:
        print("Grade: A")
    elif total_score >= 80:
        print("Grade: B")
    elif total_score >= 70:
        print("Grade: C")
    elif total_score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")


    print("\n")
