#사용자로부터 구구단 숫자 입력 받는 곳
num = int(input("출력할 구구단 단수를 입력하세요: "))

# 구구단 출력
print(f"{num}단 출력")
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")