# 딕셔너리를 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredients": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 딕셔너리에 요소 추가
dictionary["price"] = 5000
print(dictionary)

# 딕셔너리 요소 수정
dictionary["name"] = "8D 건조 망고"
print(dictionary)

# 딕셔너리 요소 삭제
del dictionary["ingredients"]
print(dictionary)