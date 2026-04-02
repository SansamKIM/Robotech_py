def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += item
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8,9]]
print("원본: ", example)
print("변환: ", flatten(example))

#원본:  [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
#변환:  [1, 2, 3, 4, [5, 6], 7, 8, 9]
# 어떻게 해결해야 할 지 생각

