my_list = [20,30,40,5,5,6]
metritis = 0
athroisma = 0
while metritis < len(my_list):
    athroisma = athroisma + my_list[metritis]
    metritis = metritis + 1
print ("Το άθροισμα όλων των αριθμών είναι: " + str(athroisma))