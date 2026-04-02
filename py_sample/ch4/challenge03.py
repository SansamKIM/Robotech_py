# 코돈의 개수를 세는 프로그램(염기서열은 일반적으로 3개씩 묶여서 하나의 의미를 나타냄)

dna = input("염기 서열을 입력해주세요.>>> ")
counter = {}

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    if len(codon) == 3:
        print(codon)

#===================================================

dna = input("염기 서열을 입력해주세요.>>> ")
counter = {}

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    if len(codon) == 3:
        if codon not in counter:
            counter[codon] = 0
        counter[codon] += 1

print(counter)