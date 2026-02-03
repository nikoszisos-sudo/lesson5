active = True
while active:
    eisodos = input("Δώσε μια συμβολοσειρά ή γράψε έξοδος: ")
    if eisodos == "έξοδος":
       print ("αντίο")
       active = False
    else:
       print ("Έδωσες " + eisodos)