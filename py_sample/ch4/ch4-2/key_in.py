# 키가 존재하는지 확인하고 값에 접근하기

# 딕셔너리를 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredients": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 사용자로부터 입력받기
key = input("접근하고자 하는 키 >>> ")

# 출력
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키입니다.")