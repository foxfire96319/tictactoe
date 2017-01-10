import Tkinter as tk
from game_engine import win
import tkMessageBox

t = [1,2,3,4,5,6,7,8,9]

def reset():
    temp = 1
    for index in xrange(0,9):
        t[index] = temp
        temp += 1
    board()

def board():
    for num in gui_canvas.find_all():
        gui_canvas.delete(num)
    gui_canvas.create_line(100,0,100,300,width=3)
    gui_canvas.create_line(200,0,200,300,width=3)
    gui_canvas.create_line(0,100,300,100,width=3)
    gui_canvas.create_line(0,200,300,200,width=3)
    y = 50
    k=0
    
    for i in range(0,3):
        x = 50
        for j in range(0,3):
            font_var = 'helvetica 20'
            fill_color = 'black'
            if t[k] == 'X':
                fill_color = 'blue'
                font_var = 'helvetica 22'
            elif t[k] == 'O':
                fill_color = 'red'
                font_var = 'helvetica 22'
            gui_canvas.create_text(x,y, text=t[k], fill = fill_color, font=font_var)
            x += 100
            k += 1
        y += 100
    if win(t):
        tkMessageBox.showinfo("","You Win")
        reset()

'''
def draw(x,y,index,delete_char):
    fill_color = 'red'
    if t[index] == 'X':
        fill_color = 'blue'
    gui_canvas.delete(num_tup[delete_char])
    print gui_canvas.find_all()
    gui_canvas.create_text(x,y, text=t[index], font='helvetica 22', fill = fill_color)
    if win(t):
        print "winner"
        board()
'''
def text_one():
    if type(t[0]) == int:
        t[0] = 'X'
        board()
    
def text_two():
    if type(t[1]) == int:
        t[1] = 'X'
        board()

def text_three():
    if type(t[2]) == int:
        t[2] = 'X'
        board()

def text_four():
    if type(t[3]) == int:
        t[3] = 'X'
        board()

def text_five():
    if type(t[4]) == int:
        t[4] = 'X'
        board()

def text_six():
    if type(t[5]) == int:
        t[5] = 'X'
        board()

def text_seven():
    if type(t[6]) == int:
        t[6] = 'X'
        board()

def text_eight():
    if type(t[7]) == int:
        t[7] = 'X'
        board()

def text_nine():
    if type(t[8]) == int:
        t[8] = 'X'
        board()

gui = tk.Tk()
gui.title("Tic-Tac-Toe")

gui_canvas = tk.Canvas(gui, height=300, width=325)
gui_canvas.pack(side = 'left')


right_frame = tk.Frame(gui)
right_frame.pack(side = 'right')

C1 = tk.Button(right_frame, text = '1',command=text_one)
C2 = tk.Button(right_frame, text = '2',command=text_two)
C3 = tk.Button(right_frame, text = '3',command=text_three)
C4 = tk.Button(right_frame, text = '4',command=text_four)
C5 = tk.Button(right_frame, text = '5',command=text_five)
C6 = tk.Button(right_frame, text = '6',command=text_six)
C7 = tk.Button(right_frame, text = '7',command=text_seven)
C8 = tk.Button(right_frame, text = '8',command=text_eight)
C9 = tk.Button(right_frame, text = '9',command=text_nine)

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
