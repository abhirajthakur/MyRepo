from math import *
from tkinter import *
from tkinter.font import BOLD



def click(event):
    global screen_value
    text = event.widget.cget('text')
    if text == '=':
        if screen_value.get().isdigit():
            value = int(screen_value.get())
        else:
            try:
                value = eval(screen_value.get())
            except Exception as e:
                value = "Error"

        screen_value.set(value)
        screen.update()
    elif text == 'x':
        screen_value.set(screen_value.get() + "*")
        screen.update()
    elif text == 'C':
        screen_value.set("")
        screen.update()
    elif text == '⌫':
        screen.delete(len(screen_value.get())-1, END)
        screen.update()
    elif text == '÷':
        screen_value.set(screen_value.get()+'/')
        screen.update()
    elif text == '±':
        screen_value.set(-eval(screen_value.get()))
        screen.update()
    elif text == '√':
        screen_value.set(sqrt(eval(screen_value.get())))
        screen.update()
    else:
        screen_value.set(screen_value.get()+text)
        screen.update()
        


root = Tk()
blank_space = ' '
root.title(65*blank_space + 'Calculator')
root.resizable(width=False, height=False)

screen_value = StringVar()

frame = Frame(root, bd=20, pady=3, relief=RIDGE, bg='#00BFFF')
frame.grid()

frame2 = Frame(frame, bd=15, pady=5, relief=RIDGE, bg='red')
frame2.grid()

MainFrame = Frame(frame2, bd=6, pady=3, relief=RIDGE, bg='#00BFFF')
MainFrame.grid()




screen_value = StringVar()
screen_value.set("")
screen = Entry(MainFrame, width=14,textvar=screen_value, font=('arial', 35, BOLD), fg='white', bd=6, bg='#00BFFF', justify=RIGHT)
screen.grid(row=0, column=0, columnspan=5, ipady=8)

numberpad = '789456123'
i = 0
btn = []
for j in range(3, 6):
    for k in range(3):
        btn.append(Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text=numberpad[i]))
        btn[i].grid(row=j, column=k)
        btn[i].bind("<Button-1>", click)
        i+=1

clear_all = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='C')
clear_all.grid(row=2, column=0)
clear_all.bind("<Button-1>", click)

backspace = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='⌫')
backspace.grid(row=2, column=1)
backspace.bind("<Button-1>", click)

plus_minus = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='±')
plus_minus.grid(row=2, column=2)
plus_minus.bind("<Button-1>", click)

divide = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='÷')
divide.grid(row=2, column=3)
divide.bind("<Button-1>", click)

multiply = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='x')
multiply.grid(row=3, column=3)
multiply.bind("<Button-1>", click)

minus = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='-')
minus.grid(row=4, column=3)
minus.bind("<Button-1>", click)

plus = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='+')
plus.grid(row=5, column=3)
plus.bind("<Button-1>", click)

square_root = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='√')
square_root.grid(row=6, column=0)
square_root.bind("<Button-1>", click)

zero = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='0')
zero.grid(row=6, column=1)
zero.bind("<Button-1>", click)

point = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='.')
point.grid(row=6, column=2)
point.bind("<Button-1>", click)

equals = Button(MainFrame, fg='white', bg='#00BFFF',width=3, height=2, font=('arial', 19, BOLD), padx=16, bd=6, text='=')
equals.grid(row=6, column=3)
equals.bind("<Button-1>", click)


root.mainloop()


# ÷
# ⌫
# ±
# √