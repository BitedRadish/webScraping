def dict_process():
    dict1 = {"name": "John", "age": 30}
    print(f"나이 : {dict1["age"]}")
    dict2 = {"math": 90, "science": 85, "history": 78}
    print(list(dict2.keys()))
    dict3 = {'apple': 3, 'banana': 5}
    dict3["apple"] = dict3["apple"]+2
    print(dict3)


dict_process()
