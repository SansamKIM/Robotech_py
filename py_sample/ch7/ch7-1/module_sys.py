import sys

print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보 출력
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copytight:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램을 강제로 종료
sys.exit()