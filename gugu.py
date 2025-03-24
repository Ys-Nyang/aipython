while True:
    try:
        # 사용자로부터 입력을 받아 숫자로 변환
        num = int(input("출력할 구구단 단수를 입력하세요: "))
        break  # 올바른 숫자가 입력되면 루프 종료
    except ValueError:
        print("올바른 숫자를 입력하세요!")  # 숫자가 아닌 값을 입력했을 때 예외 처리

# 입력된 숫자의 구구단 출력
print(f"{num}단 출력")
for i in range(1, 10):  # 1부터 9까지 반복
    print(f"{num} x {i} = {num * i}")  # 구구단 출력