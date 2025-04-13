def id_number_parser(res):
    birth,info = res.split("-")
    year, month, day = map(int, [birth[:2], birth[2:4], birth[4:6]])

    if(int(info[0])==1 or int(info[0])==2):
       pre="19"
    else:
        pre="20"
    print(f"{pre}{year}년 {month}월 {day}일")


id_number_parser("901212-1234567")
