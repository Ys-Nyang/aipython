#num = int(input("출력할 구구단 단수를 입력하세요: "))
s_num = input("출력할 구구단 단수를 입력하세요: ")
print(f"{s_num}단:")
#num 값이 문자열이기 때문에 숫자로 변경해서 연산하여야 함
num = int(s_num)
result = num * 2
print(result)