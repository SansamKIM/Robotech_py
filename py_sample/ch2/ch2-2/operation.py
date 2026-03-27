print(2 + 2 - 2 * 2 / 2 * 2)
print(2 - 2 + 2 / 2 * 2 + 2)

def solution(n):
    answer = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            answer.append(i)
    answer.sort()
    return answer

solution(10)
