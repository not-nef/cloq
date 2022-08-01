import tkinter
import time

root = tkinter.Tk()
root.configure(background="black")
root.wm_attributes('-alpha', 0.5)
root.overrideredirect(True)

root.geometry("185x210+50+50")

def enter(e):
    root.wm_attributes('-alpha', 1)

def leave(e):
    root.wm_attributes('-alpha', 0.5)

def kill(e):
    root.destroy()

root.bind("<Enter>", enter)
root.bind("<Leave>", leave)
root.bind("<Button-1>", kill)

class lbl(tkinter.Label):
    def __init__(self, text, **kwargs):
        super(lbl, self).__init__(text=text, fg="grey", bg="black", font=("Courier New", 10, "bold"))

# Actual Words
it = lbl(text="I T")
is_ = lbl(text="I S")
a = lbl(text="A")
quarter = lbl(text="Q U A R T E R")
twenty = lbl(text="T W E N T Y")
five = lbl(text="F I V E")
half = lbl(text="H A L F")
ten = lbl(text="T E N")
to = lbl(text="T O")
past = lbl(text="P A S T")
nine = lbl(text="N I N E")
one = lbl(text="O N E")
six = lbl(text="S I X")
three = lbl(text="T H R E E")
four = lbl(text="F O U R")
five_ = lbl(text="F I V E")
two = lbl(text="T W O")
eight = lbl(text="E I G H T")
eleven = lbl(text="E L E V E N")
seven = lbl(text="S E V E N")
twelve = lbl(text="T W E L V E")
ten_ = lbl(text="T E N")
oclock = lbl(text="O C L O C K")

# Fillers
l = lbl(text="L")
asampm = lbl(text="A S A M P M")
c = lbl(text="C")
dc = lbl(text="D C")
x = lbl(text="X")
s = lbl(text="S")
f = lbl(text="F")
eru = lbl(text="E R U")
se = lbl(text="S E")

it.place(x=5, y=5)
l.place(x=37, y=5)
is_.place(x=53, y=5)
asampm.place(x=85, y=5)

a.place(x=5, y=25)
c.place(x=21, y=25)
quarter.place(x=37, y=25)
dc.place(x=149, y=25)

twenty.place(x=5, y=45)
five.place(x=101, y=45)
x.place(x=165, y=45)

half.place(x=5, y=65)
s.place(x=69, y=65)
ten.place(x=85, y=65)
f.place(x=133, y=65)
to.place(x=149, y=65)

past.place(x=5, y=85)
eru.place(x=69, y=85)
nine.place(x=117, y=85)

one.place(x=5, y=105)
six.place(x=53, y=105)
three.place(x=101, y=105)

four.place(x=5, y=125)
five_.place(x=69, y=125)
two.place(x=133, y=125)

eight.place(x=5, y=145)
eleven.place(x=85, y=145)

seven.place(x=5, y=165)
twelve.place(x=85, y=165)

ten_.place(x=5, y=185)
se.place(x=53, y=185)
oclock.place(x=85, y=185)

def on(l:lbl, l2=None):
    l.configure(fg="white")
    if not l2==None:
        l2.configure(fg="white")

def off(l:lbl):
    l.configure(fg="grey")

def alloff():
    off(a)
    off(quarter)
    off(twenty)
    off(five)
    off(half)
    off(ten)
    off(to)
    off(past)
    off(nine)
    off(one)
    off(six)
    off(three)
    off(four)
    off(five_)
    off(two)
    off(eight)
    off(eleven)
    off(seven)
    off(twelve)
    off(ten_)
    off(oclock)

on(it)
on(is_)

def getandset():
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))

    alloff()

    if m >= 0 and m < 5: on(oclock)
    elif (m >= 5 and m < 10) or (m >= 55 and m <= 59): on(five)
    elif (m >= 10 and m < 15) or (m >= 50 and m < 55): on(ten)
    elif (m >= 15 and m < 20) or (m >= 45 and m < 50): on(a, quarter)
    elif (m >= 20 and m < 25) or (m >= 40 and m < 45): on(twenty)
    elif (m >= 25 and m < 30) or (m >= 35 and m < 40): on(twenty, five)
    elif m >= 30 and m < 35: on(half)

    if m >= 5 and m < 35: on(past)
    elif m >= 35 and m <= 59: on(to)


    if h == 1: on(one)
    elif h == 2: on(two)
    elif h == 3: on(three)
    elif h == 4: on(four)
    elif h == 5: on(five_)
    elif h == 6: on(six)
    elif h == 7: on(seven)
    elif h == 8: on(eight)
    elif h == 9: on(nine)
    elif h == 10: on(ten_)
    elif h == 11: on(eleven)
    elif h == 12: on(twelve)

    root.after(1000, getandset)

getandset()

root.mainloop()