from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()

# 1. 컬러 텍스트 출력
console.print("[bold green]Hello, Rich![/bold green]")
console.print("[italic red]이건 빨간색 이탤릭 텍스트야[/italic red]")

# 2. 테이블 출력
table = Table(title="학생 목록")

table.add_column("이름", style="cyan", no_wrap=True)
table.add_column("학년", style="magenta")
table.add_column("학과", style="green")

table.add_row("지민", "3학년", "미디어콘텐츠학과")
table.add_row("수빈", "2학년", "컴퓨터공학과")
table.add_row("현우", "1학년", "기계공학과")

console.print(table)

# 3. 진행 바 출력
for step in track(range(10), description="작업 중..."):
    time.sleep(0.3)  # 작업 대기 시간 (예시용)