# 아스키 코드 그림 출력 하기
# 참고 사이트 : https://wikidocs.net/227933

# 만약에 1을 입력하면 1번 캐릭터 출력
# 만약에 2를 입력하면 2번 캐릭터 출력
# 만약에 3을 입력하면 3번 캐릭터 출력
# 잘못 입력하면 잘못 입력했다고 출력

# 실행 전 pip install art 수동 실행

# pip install 자동 설치
import subprocess
import sys

# art 모듈 설치 시도
try:
    from art import text2art, tprint
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "art"])

from art import text2art, tprint

def play(n):
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

# 1. 5번 반복하는 부분
print("▶ 5번 반복 실행 모드 시작!")
for i in range(5):
    n = int(input("숫자를 입력하세요 (1: 고양이, 2: 강아지, 3: 토끼): "))
    play(n)

# 2. 0 입력 시 종료되는 무한 반복 모드
print("\n▶ 0을 입력하면 종료되는 무한 반복 모드 시작!")
while True:
    n = int(input("숫자를 입력하세요 (1: 고양이, 2: 강아지, 3: 토끼, 0: 종료): "))
    if n == 0:
        print("프로그램을 종료합니다.")
        break
    play(n)