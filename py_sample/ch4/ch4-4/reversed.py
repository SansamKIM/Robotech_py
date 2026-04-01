list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]):", list_reversed) # 이터레이터
print("lsit(reversed([1, 2, 3, 4, 5])):", list(list_reversed), "\n")

print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)
    
# 제너레이터
'''
tmp = reversed([1, 2, 3, 4, 5, 6])

for i in tmp
print("첫 번째 반복문: {}".format(i))

for i in tmp
print("두 번째 반복문: {}".format(i))
'''
# 첫 번째 반복문만 실행 두 번째 반복문은 출력 안됨

# => 필요한 시점에서 사용
numbers = [1, 2, 3, 4, 5, 6]

for i in reversed(numbers):
    print("첫 번째 반복문: {}".format(i))
    
for i in reversed(numbers):
    print("두 번째 반복문: {}".format(i))