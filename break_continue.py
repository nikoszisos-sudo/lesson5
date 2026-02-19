rep = 0
hiddennum = int(input("Δώσε τον κρυφό αριθμό: "))
maxtry = int(input("Δώσε τον μέγιστο αριθμό προσπαθειών: "))
while rep <= maxtry:
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
if rep > maxtry:
    print("έχεις υπερβεί τις " + str(maxtry) + " προσπάθειες")
