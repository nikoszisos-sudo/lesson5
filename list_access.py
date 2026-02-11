x = input("Δώσε την πρώτη πόλη: ")
y = input("Δώσε την δεύτερη πόλη: ")
z = input("Δώσε την τρίτη πόλη: ")
w = input("Δώσε την τέταρτη πόλη: ")
xa = input("Δώσε την πέμπτη πόλη: ")
my_list = [x,y,z,w,xa]
new_list = []
element = 0
while element < len(my_list):
    if element % 2 == 0:
       new_list.append(my_list[element])
    element = element + 1
print (new_list)


