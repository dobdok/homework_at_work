def add_to_dict(wyniki):
    dict_all = {
        "TODO": [],
        "IN PROGRESS": [],
        "zadania_done": []
        }

    input_where = where_modify()
    if input_where == "T":
        dict_all["TODO"].append(wyniki)
    if input_where == "I":
        dict_all["IN PROGRESS"].append(wyniki)
    if input_where == "D":
        dict_all["zadania_done"].append(wyniki)
    print(dict_all)

def inputs():
    my_list = []
    id = 0
    #  here adding the data to TO DO list
    while True:
        id += 1
        data = input(f"enter your data:  ")
        indeksowane_data = "ID_" + str(id) + " " + data   # nadanie inputowi indeksu
        print(indeksowane_data)
        my_list.append(indeksowane_data)
        # print(my_list)
        add_to_dict(my_list)



def where_modify():
    where_modify_inp = input('where to edit todo, in progress, zadania_done').upper()
    return where_modify_inp


inputs()

