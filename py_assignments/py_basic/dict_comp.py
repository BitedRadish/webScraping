def dict_comp():
    li = ["apple", "banana", "cherry"]
    dict = {}
    for i in li:
        dict[i] = len(i)
    print(dict)


dict_comp()
