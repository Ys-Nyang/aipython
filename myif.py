# 아스키 코드 그림 출력 하기
# 참고 사이트 : https://wikidocs.net/227933

# 만약에 1을 입력하면 1번 캐릭터 출력
# 만약에 2를 입력하면 2번 캐릭터 출력
# 만약에 3을 입력하면 3번 캐릭터 출력
# 잘못 입력하면 잘못 입력했다고 출력
from art import text2art, tprint
n = int(input("숫자를 입력하세요:"))

if n == 1:
    print(text2art("1. CAT"))
    print(" /\\_/\\  ")
    print("( o.o ) ")
    print(" > ^ <  ")
elif n == 2:
    print(text2art("2. DOG"))
    print(" /\\__  ")
    print(" (    @\\___ ")
    print(" /         O ")
    print("/   (_____ /")
    print("/_____/   U")
elif n == 3:
    print(text2art("3. RABBIT"))
    print("(\\(\\  ")
    print("( -.-) ")
    print("o_('')('')")
else:
    print("올바른 숫자 입력값이 아닙니다.")