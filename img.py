# 필요한 라이브러리 설치: pip install Pillow matplotlib
from PIL import Image
import matplotlib.pyplot as plt
import os # 파일 존재 여부 확인을 위해 추가

# 처리할 이미지 파일 경로
input_filename = "C:\Users\User\Downloads\ChatGPT Image 2025년 4월 21일 오전 11_32_02.png"
output_grayscale_filename = "output_grayscale.jpg"
output_resized_filename = "output_resized.jpg"

# 입력 파일이 있는지 확인
if not os.path.exists(input_filename):
    print(f"오류: '{input_filename}' 파일을 찾을 수 없습니다. 스크립트와 같은 디렉토리에 넣어주세요.")
else:
    try:
        # --- 1. 이미지 열기 ---
        img = Image.open(input_filename)

        # --- 2. 이미지 정보 출력 ---
        print(f"원본 이미지 형식: {img.format}")
        print(f"원본 이미지 크기: {img.size}")
        print(f"원본 이미지 모드: {img.mode}")

        # --- 3. 이미지 흑백으로 변환 ---
        gray_img = img.convert("L")
        gray_img.save(output_grayscale_filename)
        print(f"흑백 이미지 저장 완료: {output_grayscale_filename}")

        # --- 4. 이미지 리사이즈 ---
        width = 200
        # 원본 비율 유지
        ratio = float(width) / img.size[0]
        height = int(img.size[1] * ratio)
        resized_img = img.resize((width, height))
        resized_img.save(output_resized_filename)
        print(f"리사이즈된 이미지 저장 완료: {output_resized_filename}")

        # --- 5. Matplotlib을 사용하여 이미지 보여주기 ---
        plt.figure(figsize=(10, 5)) # 전체 그림(figure)의 크기 조절 (선택 사항)

        # 원본 이미지 표시
        plt.subplot(1, 3, 1) # 1행 3열 중 첫 번째 위치
        plt.imshow(img)
        plt.title('Original Image')
        plt.axis('off') # 축 정보 끄기

        # 흑백 이미지 표시
        plt.subplot(1, 3, 2) # 1행 3열 중 두 번째 위치
        # 흑백 이미지는 cmap='gray'를 지정해야 올바른 색으로 보입니다.
        plt.imshow(gray_img, cmap='gray')
        plt.title('Grayscale Image')
        plt.axis('off')

        # 리사이즈된 이미지 표시
        plt.subplot(1, 3, 3) # 1행 3열 중 세 번째 위치
        plt.imshow(resized_img)
        plt.title('Resized Image')
        plt.axis('off')

        plt.tight_layout() # subplot 간 간격 자동 조절
        plt.show() # 모든 플롯을 화면에 표시

        print("\n이미지 처리 및 보기 완료!")

    except Exception as e:
        print(f"오류 발생: {e}")