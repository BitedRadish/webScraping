from functools import reduce


def list_process():
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")

    print(fruits)

    num1 = [10, 20, 30]
    print(reduce(lambda x, y: x+y, num1))
    num2 = [1, 2, 3, 4, 5]
    num2.sort(reverse=True)
    print(num2)
    num3 = [5, 2, 8, 1, 9]
    num3.sort()
    print(num3)


list_process()
