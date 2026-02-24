rep = 0
hiddennum = int(input("Δώσε τον κρυφό αριθμό: "))
maxtry = int(input("Δώσε τον μέγιστο αριθμό προσπαθειών: "))
while maxtry <= 0:
    maxtry = int(input("Δώσε τον μέγιστο αριθμό προσπαθειών: "))
while True:
    i = int(input("Δωσε μια τιμή: "))
    if i < hiddennum:
      print("Δώσε μεγαλύτερη τιμή")
      rep = rep + 1
      print("έκανες " + str(rep) + " προσπάθειες" )
    elif i > hiddennum:
     print("Δώσε μικρότερη τιμή")
     rep = rep + 1
     print("έκανες " + str(rep) + " προσπάθειες")
    else:
     print("Το βρήκες")
     rep = rep+1
     print("έκανες " + str(rep) + " προσπάθειες")
     break
if rep == maxtry:
    print("έχεις εξαντλήσει τις " + str(maxtry) + " προσπάθειες")
