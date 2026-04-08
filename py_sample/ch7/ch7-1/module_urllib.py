from urllib import request

# urlopen() 함수로 구글의 메인 페이지 읽기
target = request.urlopen("https://www.google.com/")
output = target.read()

print(output)