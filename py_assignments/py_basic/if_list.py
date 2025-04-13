def if_list(line):
    scores = [70, 85, 90, 55, 78]
    for s in scores:
        if s >= line:
            print(f"합격 : {s}")


if_list(60)
