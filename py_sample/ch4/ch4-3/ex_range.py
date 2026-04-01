a = range(5)
print(a)
print(list(a))  # print(list(range(5)))

print(list(range(0, 5)))
print(list(range(5, 10)))

print(list(range(0, 10, 2)))
print(list(range(0, 10, 3)))

b = range(0, 10 + 1)
print(list(b))

n = 10
c = range(0, n / 2)  # TypeError: 'float' object cannot be interpreted as an integer
                     # range() 함수의 매개변수는 정수여야 한다.

c = range(0, int(n / 2))  # int() 함수를 사용하여 실수를 정수로 변환 - 잘 사용하지 않음
print(list(c))

c = range(0, n // 2)  # // 연산자를 사용하여 실수를 정수로 변환
print(list(c))