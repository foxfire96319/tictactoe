import Tkinter as Tk
from game_engine import win
import tkMessageBox


t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_bool = False


def reset():
    temp = 1
    for index in xrange(0, 9):
        t[index] = temp
        temp += 1
    board()


def board():
    for num in gui_canvas.find_all():
        gui_canvas.delete(num)
    gui_canvas.create_line(100, 0, 100, 300, width=3)
    gui_canvas.create_line(200, 0, 200, 300, width=3)
    gui_canvas.create_line(0, 100, 300, 100, width=3)
    gui_canvas.create_line(0, 200, 300, 200, width=3)
    y = 50
    k = 0

    for i in range(0, 3):
        x = 50
        for j in range(0, 3):
            font_var = 'helvetica 20'
            fill_color = 'black'
            if t[k] == 'X':
                fill_color = 'blue'
                font_var = 'helvetica 22'
            elif t[k] == 'O':
                fill_color = 'red'
                font_var = 'helvetica 22'
            gui_canvas.create_text(x, y, text=t[k], fill=fill_color, font=font_var)
            x += 100
            k += 1
        y += 100
    if win(t):
        tkMessageBox.showinfo("", "You Win")
        reset()


def _play(num):
    if type(t[num]) == int:
        if player_bool:
            t[num] = 'X'
        else:
            t[num] = 'O'
        board()


def text_one():
    _play(0)


def text_two():
    _play(1)


def text_three():
    _play(2)


def text_four():
    _play(3)


def text_five():
    _play(4)


def text_six():
    _play(5)


def text_seven():
    _play(6)


def text_eight():
    _play(7)


def text_nine():
    _play(8)

gui = Tk.Tk()
gui.title("Tic-Tac-Toe")

gui_canvas = Tk.Canvas(gui, height=300, width=325)
gui_canvas.pack(side='left')


right_frame = Tk.Frame(gui)
right_frame.pack(side='right')

C1 = Tk.Button(right_frame, text='1', command=text_one)
C2 = Tk.Button(right_frame, text='2', command=text_two)
C3 = Tk.Button(right_frame, text='3', command=text_three)
C4 = Tk.Button(right_frame, text='4', command=text_four)
C5 = Tk.Button(right_frame, text='5', command=text_five)
C6 = Tk.Button(right_frame, text='6', command=text_six)
C7 = Tk.Button(right_frame, text='7', command=text_seven)
C8 = Tk.Button(right_frame, text='8', command=text_eight)
C9 = Tk.Button(right_frame, text='9', command=text_nine)

C1.pack()
C2.pack()
C3.pack()
C4.pack()
C5.pack()
C6.pack()
C7.pack()
C8.pack()
C9.pack()

board()


gui.mainloop()
