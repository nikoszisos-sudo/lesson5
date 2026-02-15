my_list = []
for i in range(5):
    x = input ("Δώσε την " + str(i+1) + "η πόλη: ")
    my_list.append(x)
for index in range(0, len(my_list), 2):
    print(my_list[index])
