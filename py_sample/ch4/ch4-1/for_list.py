# 리스트 선언
array = [273, 32, 103, 57, 52]

# 리스트에 반복문을 적용
for element in array:
    print(element)
    
for character in "안녕하세요":
    print("-", character)
    
list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.extend(list_a)
print(list_a)