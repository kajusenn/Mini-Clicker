#Build exe:
#pip install pyinstaller
# pyinstaller --onefile --windowed clicker.py

from tkinter import *
win = Tk()
win.title('CLICKER')
win.geometry('520x550')
# win.resizable(0, 0)

# def fchan_gold():

# def fchan_diamond():

def btn_click():
    global expression
    global mult
    global adding
    expression = expression + adding
    wood_var.set(f"{expression:,}")
    update_display()
    print(f"plus {adding}")

def btn_multipla(add, price):
    global adding
    global expression
    if expression >= price:
        expression = expression - price
        wood_var.set(f"{expression:,}")
        adding += add


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

multipla_wood1 = Button(btn_frame, text='UPGRADE +1 (-100)', width=15, height=3, command=lambda: btn_multipla(1, 10)).grid(row=2, column=2, padx=10, pady=5)
multipla_wood2 = Button(btn_frame, text='UPGRADE +2 (-500)', width=15, height=3, command=lambda: btn_multipla(2, 50)).grid(row=3, column=2, padx=10, pady=5)
multipla_wood3 = Button(btn_frame, text='UPGRADE +5 (-5.5K)', width=15, height=3, command=lambda: btn_multipla(5, 150)).grid(row=4, column=2, padx=10, pady=5)

multipla_gold1 = Button(btn_frame, text='UPGRADE +1 (-50k)', width=15, height=3, command=lambda: btn_multipla(1, 50000)).grid(row=2, column=3, padx=10, pady=5)
multipla_gold2 = Button(btn_frame, text='UPGRADE +2 (-200k)', width=15, height=3, command=lambda: btn_multipla(2, 200000)).grid(row=3, column=3, padx=10, pady=5)
multipla_gold3 = Button(btn_frame, text='UPGRADE +5 (-400k)', width=15, height=3, command=lambda: btn_multipla(5, 400000)).grid(row=4, column=3, padx=10, pady=5)

multipla_diamond1 = Button(btn_frame, text='UPGRADE +1 (-10)', width=15, height=3, command=lambda: btn_multipla(10)).grid(row=2, column=4, padx=10, pady=5)
multipla_diamond2 = Button(btn_frame, text='UPGRADE +2 (-50)', width=15, height=3, command=lambda: btn_multipla(50)).grid(row=3, column=4, padx=10, pady=5)
multipla_diamond3 = Button(btn_frame, text='UPGRADE +5 (-1500)', width=15, height=3, command=lambda: btn_multipla(1500)).grid(row=4, column=4, padx=10, pady=5)

chan_frame = Frame(win, width=330, height=170)
chan_frame.pack(pady=10, padx=25, anchor='center')

chan_btn_diamond = Button(chan_frame, text='+1 chance for diamond (1M)', width=30, height=3, command=lambda: btn_multipla(1500)).grid(row=5, column=3, padx=6, pady=5)
chan_btn_gold = Button(chan_frame, text='+1 chance for gold (500K)', width=30, height=3, command=lambda: btn_multipla(1500)).grid(row=5, column=2, padx=6, pady=5)

win.mainloop()
