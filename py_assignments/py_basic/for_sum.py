def for_sum(mod):
    sum = 0
    for i in range(1, 101):
        if i % mod == 0:
            sum += i
    print(sum)


for_sum(3)
