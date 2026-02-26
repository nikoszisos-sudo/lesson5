guests = ["Kostas", "Maria", "Vaso", "Jim", "Antonis", "Nikos", "Ioanna", "Eleni", "Eva", "Christina"]
buddies = ["Nikos", "Ioannas", "Eva"]
common = 0
for guest in guests:
    if guest in buddies:
            common += 1
print("Στο πάρτυ των 10 ατόμων είναι καλεσμένοι " + str(common) + " κολλητοί μου")
if common >= 2:
    print ("Θα πάω στο πάρτυ")
else:
    print("Δε Θα πάω στο πάρτυ")


