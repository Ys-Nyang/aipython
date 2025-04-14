import subprocess
import sys
import time
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from art import text2art

# 필요한 모듈 설치
try:
    from art import text2art
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "art"])
    from art import text2art

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.table import Table
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.table import Table

console = Console()

def print_options_table():
    table = Table(title="입력 가능한 명령어", show_header=True, header_style="bold magenta")
    table.add_column("명령어", style="cyan", justify="center")
    table.add_column("기능", style="green", justify="center")
    table.add_row("animal", "동물 명령어로 이동 (cat, dog, rabbit)")
    table.add_row("end", "프로그램 종료 🚪")
    table.add_row("reset", "초기화 🔁")
    table.add_row("chart", "명령어 목록 다시 보기 📊")
    console.print(table)

def play(n):
    if n == 1:
        console.rule("[bold magenta]1. CAT")
        art = text2art("CAT")
        console.print(f"[bold blue]{art}[/bold blue]")

        cat_art = r"""
         /\     /\
        {  `---'  }
        {  O   O  }
        ~~>  V  <~~
         \  \|/  /
         `-----'____
        /     \    \_
        {       }\  )_\_   _
        |  \_/  |/ /  \_\_/ )
        \__/  /(_/     \__/
        (__/
        """
        console.print(Panel(Text(cat_art, style="bold white"), title="리얼 고양이 🐱", border_style="blue"))

    elif n == 2:
        console.rule("[bold green]2. DOG")
        art = text2art("DOG")
        console.print(f"[bold green]{art}[/bold green]")

        dog_art = r"""
        /^-----^\
        V  o o  V
         |  Y  |
          \ Q /
          / - \
          |    \
          |     \     )
          || (___\====
        """
        console.print(Panel(Text(dog_art, style="bold white"), title="리얼 강아지 🐶", border_style="green"))

    elif n == 3:
        console.rule("[bold yellow]3. RABBIT")
        art = text2art("RABBIT")
        console.print(f"[bold yellow]{art}[/bold yellow]")

        rabbit_art = r"""
         (\_/)
         ( •_•)
        / >🌿   당근~!
        """
        console.print(Panel(Text(rabbit_art, style="bold white"), title="귀염 토끼 🐰", border_style="yellow"))
    else:
        console.print("[bold red]❌ 올바른 숫자 입력값이 아닙니다.[/bold red]")

# ▶ 메인 프로그램 실행
while True:
    console.print("\n[bold cyan]▶ 동물 아트 출력 프로그램을 시작합니다![/bold cyan]")
    print_options_table()

    while True:
        user_input = console.input("[bold white]숫자 또는 명령어를 입력하세요 (표 참고): [/bold white]").strip()

        if user_input.lower() == "reset":
            # 초기화 중 화면 청소 및 줄 내림
            console.clear()
            console.print("[bold magenta]🔁 초기화 중...[/bold magenta]")
            console.print("\n" * 20)  # 줄 내림

            # 프로그래스 바 구현
            with Progress() as progress:
                task = progress.add_task("[green]초기화 진행 중...", total=100)
                while not progress.finished:
                    progress.update(task, advance=1)
                    time.sleep(0.05)  # 5초간 진행되도록 설정

            # 초기화 완료 후
            console.clear()  # 표 중복 방지
            console.print("\n" * 20)  # 추가 줄 내림
            console.print("[bold green]초기화 완료![/bold green]")  # 초기화 완료 메시지 출력

            print_options_table()  # 표 다시 출력
            break  # 바깥 while로 돌아감 (처음으로)
        elif user_input.lower() == "end":
            console.print("[bold magenta]👋 프로그램을 종료합니다. 안녕~[/bold magenta]")
            sys.exit(0)
        elif user_input.lower() == "animal":
            console.print("\n[bold cyan]▶ 동물 명령어를 입력하세요! (cat, dog, rabbit)[/bold cyan]")
            while True:
                animal_input = console.input("[bold white]동물 명령어 입력: [/bold white]").strip().lower()
                if animal_input == "cat":
                    play(1)
                    print_options_table()  # 동물 출력 후 명령어 표 다시 표시
                    break
                elif animal_input == "dog":
                    play(2)
                    print_options_table()  # 동물 출력 후 명령어 표 다시 표시
                    break
                elif animal_input == "rabbit":
                    play(3)
                    print_options_table()  # 동물 출력 후 명령어 표 다시 표시
                    break
                elif animal_input == "chart":
                    print_options_table()
                elif animal_input == "reset":
                    console.print("[bold magenta]🔁 초기화 중...[/bold magenta]")

                    # 프로그래스 바 구현
                    with Progress() as progress:
                        task = progress.add_task("[green]초기화 진행 중...", total=100)
                        while not progress.finished:
                            progress.update(task, advance=1)
                            time.sleep(0.05)  # 5초간 진행되도록 설정

                    # 초기화 완료 후
                    console.clear()  # 표 중복 방지
                    print_options_table()  # 표 다시 출력
                    console.print("[bold green]초기화 완료![/bold green]")
                    break  # 바깥 while로 이동
                elif animal_input == "end":
                    console.print("[bold magenta]👋 프로그램을 종료합니다. 안녕~[/bold magenta]")
                    sys.exit(0)
                else:
                    console.print("[red]⚠️ 올바른 동물 명령어를 입력해 주세요! (cat / dog / rabbit)[/red]")
        elif user_input == "chart":
            print_options_table()
        else:
            console.print("[red]⚠️ 'animal' 명령어로 동물 선택을 시작하거나, 'reset', 'chart', 'end'을 입력해 주세요![/red]")