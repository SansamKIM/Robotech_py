import datetime

time = datetime.datetime.now()

text = input("입력: ")

if text in "안녕":
    print("안녕하세요.")
elif text in "몇 시" or text in "몇시":
    print("지금은 {}시 {}분 입니다.".format(time.hour, time.minute))
else:
    print("text")
