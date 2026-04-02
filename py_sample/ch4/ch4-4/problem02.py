# 1~100의 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고 합을 구하시오.

output = [num for num in range(1, 100) 
          if "{:b}".format(num).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계: ", sum(output))