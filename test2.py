v = input("입력값:")

# 숫자인지 문자인지 알고 싶을 때 사용하는 방법.
print(type(v))
print("숫자로 변환")
v = int(v)
print(type(v))

# 만약에 입력받은 값이 0 이면 0이다.
if v == 0:
    print("0이다.")

# 만약에 입력받은 값이 0이 아니면 0이 아니다.
if v != 0:
    print("0이 아니다.")

# 만약에 입력받은 값이 0 이면 0이다를 출력, 아니면 0이 아니다를 출력
if v == 0:
    print("0이다.")
else:
    print("0이 아니다.")