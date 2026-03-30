list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거 방법1 - del 키워드
del list_a[1]
print("del list_a[1] ->", list_a)

# 제거 방법2 - pop() 메서드
list_a.pop(2)
print("pop(2):", list_a)

# 제거 방법3 - 범위 지정하여 제거하기
list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print("del list_b[3:6] ->", list_b)

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[3:]
print("del list_c[3:] ->", list_c)

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
print("del list_c[:3] ->", list_c) 