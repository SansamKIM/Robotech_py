# 구의 부피와 겉넓이 구하기
# 부피 = 3/4pir**3
# 겉넓이 = 4pir*r

pi = 3.141592
r = int(input("구의 반지름을 입력하세요. >>> "))

volum = (3 / 4) * pi * (r ** 3)

s_area = 4 * pi * r * r

print("반지름{}의 부피는 {:.2f}입니다.".format(r, volum))
print("반지름{}의 겉넓이는 {:.2f}입니다.".format(r, s_area))

# fstring 표현