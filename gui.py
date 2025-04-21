import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# --- 함수 정의 ---
def open_image():
    """파일 대화상자를 열어 이미지를 선택하고 화면에 표시하는 함수"""
    global image_label, photo_image # 전역 변수 사용 선언

    # 파일 대화상자 열기 (이미지 파일 필터 적용)
    filepath = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=[("이미지 파일", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff"), ("모든 파일", "*.*")]
    )

    # 사용자가 파일을 선택했는지 확인
    if not filepath:
        print("파일을 선택하지 않았습니다.")
        return # 함수 종료

    try:
        # Pillow를 사용하여 이미지 열기
        image = Image.open(filepath)

        # --- (선택 사항) 이미지 크기 조절 ---
        # 너무 큰 이미지는 창 크기에 맞게 축소 (예: 최대 500x500)
        max_width = 500
        max_height = 500
        image.thumbnail((max_width, max_height)) # 원본 비율 유지하며 축소

        # Pillow 이미지를 Tkinter에서 사용할 수 있는 PhotoImage 객체로 변환
        photo_image = ImageTk.PhotoImage(image)

        # 레이블 위젯에 이미지 업데이트
        image_label.config(image=photo_image)

        # ★★★ 중요: PhotoImage 객체에 대한 참조 유지 ★★★
        # 함수 내에서 생성된 PhotoImage는 함수가 끝나면 가비지 컬렉션될 수 있으므로,
        # 레이블 객체 자체에 참조를 저장하여 이미지가 사라지지 않게 합니다.
        image_label.image = photo_image

        # 창 제목에 파일 이름 표시 (선택 사항)
        root.title(f"이미지 뷰어 - {os.path.basename(filepath)}")
        print(f"이미지 로드 완료: {filepath}")

    except FileNotFoundError:
        print(f"오류: 파일을 찾을 수 없습니다 - {filepath}")
    except Exception as e:
        print(f"이미지를 열거나 처리하는 중 오류 발생: {e}")


# --- GUI 설정 ---
# 메인 윈도우 생성
root = tk.Tk()
root.title("간단 이미지 뷰어")
root.geometry("600x600") # 초기 창 크기 설정 (너비x높이)

# 파일 열기 버튼 생성
open_button = tk.Button(root, text="이미지 열기", command=open_image, padx=10, pady=5)
open_button.pack(pady=10) # 버튼 배치 (위쪽에 약간의 여백 포함)

# 이미지를 표시할 레이블 위젯 생성 (초기에는 비어 있음)
image_label = tk.Label(root)
image_label.pack(padx=10, pady=10, expand=True, fill='both') # 레이블 배치 (여백, 창 크기 변경 시 확장)

# Tkinter 이벤트 루프 시작 (창을 화면에 표시하고 사용자 입력 대기)
root.mainloop()

print("프로그램 종료.")