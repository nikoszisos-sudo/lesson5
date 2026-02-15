x = input("Δώσε την πρώτη πόλη: ")
y = input("Δώσε την δεύτερη πόλη: ")
z = input("Δώσε την τρίτη πόλη: ")
w = input("Δώσε την τέταρτη πόλη: ")
xa = input("Δώσε την πέμπτη πόλη: ")
my_list = [x,y,z,w,xa]
for element in range(0, len(my_list), 2):
    print (my_list[element])
