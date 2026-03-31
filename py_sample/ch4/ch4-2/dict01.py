# 딕셔너리 요소에 접근하기

# 딕셔너리를 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredients": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 딕셔너리 출력
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredients:", dictionary["ingredients"])
print("origin:", dictionary["origin"], "\n")

# 딕셔너리 요소 추가
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"], "\n")

# 딕셔너리 리스트 요소 출력
print(dictionary["ingredients"][1])