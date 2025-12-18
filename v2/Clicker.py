# pyinstaller --onefile --windowed clicker.py

from tkinter import *
win = Tk()
win.title('CLICKER')
win.geometry('520x550')
# win.resizable(0, 0)

def btn_click():
    global expression
    global mult
    global adding
    expression = expression + adding
    wood_var.set(f"{expression:,}")
    update_display()
    print(f"plus {adding}")

def btn_multipla(cena):
    global adding
    global expression
    if expression >= cena and cena == 10:
        expression = expression - cena
        wood_var.set(f"{expression:,}")
        adding += 1
    elif expression >= cena and cena == 50:
        expression = expression - cena
        wood_var.set(f"{expression:,}")
        adding += 2
    elif expression >= cena and cena == 1500:
        expression = expression - cena
        wood_var.set(f"{expression:,}")
        adding += 5
    update_display()

def update_display():
    wood_var.set(f"{expression:,}")

chan_gold = 0
chan_diam = 0
adding = 1
expression = 0

#FRAME
input_frame = Frame(win, width=330, height=170)
input_frame.pack(pady=10, padx=25, anchor='w')

#TEXT
text_wood = Label(input_frame, text="Wood: ", font=('arial', 20, 'bold')).grid(row=0, column=0, padx=30)
text_gold = Label(input_frame, text="Gold: ", font=('arial', 20, 'bold')).grid(row=0, column=1, padx=30)
text_diamond = Label(input_frame, text="Diamond: ", font=('arial', 20, 'bold')).grid(row=0, column=2, padx=30)

#COUNT
wood_var = StringVar(value='0')
gold_var = StringVar(value='0')
diamond_var = StringVar(value='0')

input_field_wood = Label(input_frame, textvariable=wood_var, font=('consolas', 28, 'bold')).grid(row=1, column=0)
input_field_gold = Label(input_frame, textvariable=gold_var, font=('consolas', 28, 'bold')).grid(row=1, column=1)
input_field_diadmond = Label(input_frame, textvariable=diamond_var, font=('consolas', 28, 'bold')).grid(row=1, column=2)

#BUTTONS
btn_frame = Frame(win, width=330, height=170)
btn_frame.pack(padx=55, anchor='w')

click = Button(btn_frame, text='CLICK', width=15, height=5, command=lambda: btn_click()).grid(row=1, column=3, pady=(1, 10))

multipla1 = Button(btn_frame, text='UPGRADE (-10)', width=15, height=5, command=lambda: btn_multipla(10)).grid(row=2, column=2, padx=10, pady=5)
multipla2 = Button(btn_frame, text='UPGRADE (-50)', width=15, height=5, command=lambda: btn_multipla(50)).grid(row=3, column=2, padx=10, pady=5)
multipla3 = Button(btn_frame, text='UPGRADE (-1500)', width=15, height=5, command=lambda: btn_multipla(1500)).grid(row=4, column=2, padx=10, pady=5)

multipla1 = Button(btn_frame, text='UPGRADE (-10)', width=15, height=5, command=lambda: btn_multipla(10)).grid(row=2, column=3, padx=10, pady=5)
multipla2 = Button(btn_frame, text='UPGRADE (-50)', width=15, height=5, command=lambda: btn_multipla(50)).grid(row=3, column=3, padx=10, pady=5)
multipla3 = Button(btn_frame, text='UPGRADE (-1500)', width=15, height=5, command=lambda: btn_multipla(1500)).grid(row=4, column=3, padx=10, pady=5)

multipla1 = Button(btn_frame, text='UPGRADE (-10)', width=15, height=5, command=lambda: btn_multipla(10)).grid(row=2, column=4, padx=10, pady=5)
multipla2 = Button(btn_frame, text='UPGRADE (-50)', width=15, height=5, command=lambda: btn_multipla(50)).grid(row=3, column=4, padx=10, pady=5)
multipla3 = Button(btn_frame, text='UPGRADE (-1500)', width=15, height=5, command=lambda: btn_multipla(1500)).grid(row=4, column=4, padx=10, pady=5)

win.mainloop()