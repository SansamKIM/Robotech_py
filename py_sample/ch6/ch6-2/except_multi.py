list_number = [52, 273, 32, 72, 100]

#try except 구문을 이용하여 예외 처리
try:
    # 숫자 입력 받기
    number_input = int(input("정수 입력> "))
    # 리스트의 요소를 출력
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    # ValueError 예외가 발생하는 경우
    print("정수를 입력해주세요.")
except IndexError:
    # IndexError 예외가 발생하는 경우
    print("리스트의 인덱스 범위를 벗어났어요!")