import random

# 간단한 한글 리스트를 만듭니다.
hanguls = list("가나다라마바사아자차카타파하")
# 파일을 쓰기 모드로 엽니다.
with open("info.txt", "w", encoding="utf-8") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수 작성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트 작성
        file.write("{}, {}, {}\n".format(name, weight, height))