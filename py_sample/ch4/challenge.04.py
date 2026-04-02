# 다음과 같이 리스트가 중첩되어 있을 때 중첩을 제거하는 리스트 평탄화를 구현해보시오.
'''
numbers = [1, 2, [3, 4], 5, [6, 7], [8,9]]

for i in numbers:
    if type(i) == list:
        for j in i:
            numbers.append(j)
            numbers.pop(j)

print(list)
'''

numbers = [1, 2, [3, 4], 5, [6, 7], [8,9]]
output = []

for i in numbers:
    if type(i) == list:
        for j in i:
            output.append(j)
        else:
            output.append(i)

print(f"{numbers}를 평탄화하면")
print(f"{output}입니다.")