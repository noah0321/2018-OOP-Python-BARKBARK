#그냥 부분적으로 코드를 넣어서 연습하는 py
#아무 의미 없다.

import threading
import keyboard
import tkinter

def keypress(self):  #self
    print("Click")

def main_thread():
    root = tkinter.Tk()
    root.bind_all('<Key>', keypress)
    root.withdraw()
    root.mainloop()

thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()
