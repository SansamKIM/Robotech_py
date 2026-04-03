# 파일 열기
file = open("basic.txt", "w")

# 파일에 텍스트 작성
file.write("Hello Python Programming...!")

# 파일 닫기
file.close()

# with 키워드
'''
with open("basic.txt", "w") as file:
    file.write("Hello Python Programming...!")
'''
