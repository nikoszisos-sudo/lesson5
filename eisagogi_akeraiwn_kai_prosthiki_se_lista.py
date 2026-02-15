my_list = []
N = int(input("Δώσε αριθμό μεγαλύτερο του 3 και μικρότερο του 20: "))
while N < 3 or N > 20:
    N = int(input("Δώσε αριθμό μεγαλύτερο του 3 και μικρότερο του 20: "))
for i in range(0, N):
    N = input ("Δώσε τον " + str(i+1) + "ο ακέραιο: ")
    my_list.append(N)
    my_list.sort()
print(my_list)
