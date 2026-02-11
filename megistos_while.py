my_list = [20,30,40,555,5,6]
metritis = 0
megistos = my_list[metritis]
while metritis < len(my_list):
    if my_list[metritis] > megistos:
       megistos = my_list[metritis]
    metritis = metritis + 1
print ("Ο μέγιστος όλων των αριθμών είναι: " + str(megistos))
