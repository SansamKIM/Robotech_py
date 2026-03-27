# 숫자 입력
raw_input = input("inch 단위의 숫자를 입력해주세요:  ")

# 입력받은 데이터를 숫자 자료형으로 변환하고, cm 단위로 반환
inch = int(raw_input)
cm = inch * 2.54

print("{}inch는 {}cm 입니다.".format(inch, cm))