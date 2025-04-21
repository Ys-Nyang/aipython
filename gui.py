import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class AnimalImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("동물 이미지 출력")

        self.image_label = ttk.Label(root)
        self.image_label.pack(pady=10)

        button_frame = ttk.Frame(root)
        button_frame.pack()

        dog_button = ttk.Button(button_frame, text="강아지", command=self.show_dog_image)
        dog_button.pack(side="left", padx=5)

        cat_button = ttk.Button(button_frame, text="고양이", command=self.show_cat_image)
        cat_button.pack(side="left", padx=5)

        rabbit_button = ttk.Button(button_frame, text="토끼", command=self.show_rabbit_image)
        rabbit_button.pack(side="left", padx=5)

        self.current_image = None
        self.show_default_image()

    def load_image(self, filename):
        try:
            image = Image.open(filename)
            resized_image = image.resize((300, 300))  # 이미지 크기 조절 (원하는 크기로 변경 가능)
            photo = ImageTk.PhotoImage(resized_image)
            return photo
        except FileNotFoundError:
            print(f"Error: {filename} 파일을 찾을 수 없습니다.")
            return None

    def display_image(self, photo):
        if photo:
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference!

    def show_dog_image(self):
        dog_image = self.load_image(r"C:\Users\User\Downloads\dog.jpg")
        self.display_image(dog_image)

    def show_cat_image(self):
        cat_image = self.load_image(r"C:\Users\User\Downloads\cat.jpg")
        self.display_image(cat_image)

    def show_rabbit_image(self):
        rabbit_image = self.load_image(r"C:\Users\User\Downloads\rabbit.jpg")
        self.display_image(rabbit_image)

    def show_default_image(self):
        # 초기 이미지 또는 빈 화면을 표시할 수 있습니다.
        # 여기서는 간단하게 "이미지를 선택하세요" 텍스트를 표시합니다.
        self.image_label.config(text="이미지를 선택하세요", image="")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimalImageApp(root)
    root.mainloop()