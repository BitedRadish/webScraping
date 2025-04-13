def zip_func():
    li1 = [1, 2, 3]
    li2 = [10, 20, 30]

    for pair in zip(li1, li2):
        p1, p2 = pair
        print(p1, p2)


zip_func()
