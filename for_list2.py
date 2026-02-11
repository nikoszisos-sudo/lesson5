semester_grades = [4, 5, 7, 10, 10]
passed = 0
total_grades = 0

for grades in semester_grades:
    if grades >= 5:
        passed = passed + 1
        total_grades = total_grades + grades
print ("Έχω περάσει " + str(passed))
print ("Ο μέσος όρος μου είναι: " + str(total_grades/passed))
