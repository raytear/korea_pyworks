# 로또 복권 당첨 번호 확인
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

# 윈도우 앱 만들기

def lotto_win():
    try:
        num = int(entry.get()) #입력된 회차 번호 가져옴
        if num <= 0 or num > 1180:
            messagebox.showerror("오류", "회차가 없습니다.")
            entry.delete(0, END)  # 입력 초기화 
            output.delete(0.0, END) # 출력 초기화 
            return #즉시 종료(실행 중단)

        # 웹 크롤링
        url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
        resp = requests.get(url)

        soup = BeautifulSoup(resp.text, "html.parser")
        win_nums = soup.select('div.nums span')

        # 당첨 번호, 보너스 번호
        win_num_list = [num.text for num in win_nums]

        # 출력
        output.delete(0.0, END)
        output.insert(END, f"당첨 번호: {win_num_list[:-1]} \
                        \n\n보너스 번호: {win_num_list[-1]}")
    except ValueError:
        messagebox.showerror("오류", "유효한 숫자를 입력하세요.")
        entry.delete(0, END)  # 입력 초기화 
        output.delete(0.0, END) # 출력 초기화 

window = Tk()
window.title("로또복권 당첨확인")

Label(window, text="당첨 회차 입력: ") \
    .grid(row=0, column=0, sticky=W)
# 입력 상자
entry = Entry(window, bg="yellow")
entry.grid(row=1, column=0, sticky=W)

Button(window, text="당첨번호 확인", command=lotto_win) \
    .grid(row=2, column=0, sticky=W)
# 출력상자
output = Text(window, bg="lightgreen", width=50, height=6)
output.grid(row=3, column=0, sticky=W)

window.mainloop()