# DNA 구성 요소 A, T, G, C 중 염기서열을 입력했을 때 각각 염기가 몇 개인지 확인하는 프로그램

dna = input("염기 서열을 입력해주세요.>>> ")

counter = {
    "a" : 0, 
    "t" : 0,
    "g" : 0,
    "c" : 0
}

for nucelo in dna:
    counter[nucelo] += 1
    
for key in counter:
    print(f"{key}의 갯수: {counter[key]}")
    
# 카운터 모듈 사용 ====================