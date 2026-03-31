numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for i in numbers:
    if 99 < i < 1000:
        print("{}는 3자리 수입니다.".format(i))
    elif 9 < i < 100:
        print("{}는 2자리 수입니다.".format(i))
    elif 0 <= i < 10:
        print("{}는 1자리 수입니다.".format(i))
    else:
        print("{}는 4자리 이상의 수입니다.".format(i))