# 다음 리스트에서 몇 가지 종류의 숫자가 사용되었는 지 구하는 프로그램을 만들어보세요.
# [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]

numbers = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
count = {}

for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

print("사용된 숫자의 종류는 {}개입니다.".format(len(count)))
print(count)