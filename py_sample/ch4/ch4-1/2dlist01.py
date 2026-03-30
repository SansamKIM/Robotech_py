# 2차원 리스트에 반복문 한번 사용
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for items in list_of_list:
    print(items)
    
# 리스트의 요소 하나씩 출력
for items in list_of_list:
    for item in items:
        print(item)