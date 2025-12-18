# pyinstaller --onefile --windowed clicker.py

from tkinter import *
win = Tk()
win.title('CLICKER')
win.geometry('520x350')
# win.resizable(0, 0)

def btn_click():
    global expression
    global mult
    global adding
    expression = expression + adding
    input_text.set(f"{expression:,}")
    update_display()
    print(f"plus {adding}")

def btn_multipla(cena):
    global adding
    global expression
    if expression >= cena and cena == 10:
        expression = expression - cena
        input_text.set(f"{expression:,}")
        adding += 1
    elif expression >= cena and cena == 50:
        expression = expression - cena
        input_text.set(f"{expression:,}")
        adding += 2
    elif expression >= cena and cena == 1500:
        expression = expression - cena
        input_text.set(f"{expression:,}")
        adding += 5
    update_display()

def size():
    if expression >= 1_000_000_000:
        return 20
    elif expression >= 1_000_000:
        return 15
    elif expression >= 100_000:
        return 10
    else:
        return 5

def update_display():
    input_text.set(f"{expression:,}")
    input_field.config(width=size())


# sizes = 5
adding = 1
expression = 0
input_text = StringVar()
input_text.set('0')

input_frame = Frame(win, width=312, height=90)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), width=size(), justify=CENTER, textvariable=input_text, state='readonly')
input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

#BUTTONS
btn_frame = Frame(win, width=330, height=170)
btn_frame.pack()

click = Button(btn_frame, text='CLICK', width=15, height=5, command=lambda: btn_click()).grid(row=0, column=3, pady=20)

multipla1 = Button(btn_frame, text='UPGRADE (-10)', width=15, height=5, command=lambda: btn_multipla(10)).grid(row=1, column=2, padx=2, pady=10)
multipla2 = Button(btn_frame, text='UPGRADE (-50)', width=15, height=5, command=lambda: btn_multipla(50)).grid(row=1, column=3, padx=2, pady=10)
multipla3 = Button(btn_frame, text='UPGRADE (-1500)', width=15, height=5, command=lambda: btn_multipla(1500)).grid(row=1, column=4, padx=2, pady=10)

win.mainloop()