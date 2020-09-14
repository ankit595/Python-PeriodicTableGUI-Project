# importing libraries
import tkinter
from tkinter import *
from tkinter import messagebox

# create root window
root = Tk()

# root window title and dimension
root.title("Periodic Table")
root.geometry('1260x1000')

# Lable indicating the output
Label(root, text="OUTPUT", bg="red").place(x=230, y=600)

# generating textbox
display = Text(
    root,
    height=5,
    width=20,
    font=('arial', 20, 'bold'),
)
display.place(x=300, y=540)


# defining the function
def detail(element, name):
    data = "Symbol: {}\nAtomic Number: 1\nAtomic Mass: 1.0079\nElement: {}".format(
        element, name)
    display.__dir__()
    display.delete(1.0, END)
    display.insert(INSERT, data)
    print(data)


# First Coloumn Elements
btn = Button(
    root,
    text="H",
    fg="springgreen",
    bg="black",
    bd=7,
    width=4,
    height=2,
    command=lambda: detail("H", "Hydrogen"))  # do this for all elements
btn.grid(column=1, row=0)
btn = Button(root,
             text="Li",
             fg="orange",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=1, row=1)
btn = Button(root,
             text="Na",
             fg="orange",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=1, row=2)
btn = Button(root,
             text="K",
             fg="orange",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=1, row=3)
btn = Button(root,
             text="Rb",
             fg="orange",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=1, row=4)
btn = Button(root,
             text="Cs",
             fg="orange",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=1, row=5)
btn = Button(root,
             text="Fr",
             fg="orange",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=1, row=6)

# Second Coloumn Elements

btn = Button(root,
             text="Be",
             fg="yellow",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=2, row=1)
btn = Button(root,
             text="Mg",
             fg="yellow",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=2, row=2)
btn = Button(root,
             text="Ca",
             fg="yellow",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=2, row=3)
btn = Button(root,
             text="Sr",
             fg="yellow",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=2, row=4)
btn = Button(root,
             text="Ba",
             fg="yellow",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=2, row=5)
btn = Button(root,
             text="Ra",
             fg="yellow",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=2, row=6)

# Third Coloumn Elements

btn = Button(root,
             text="Sc",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=3, row=3)
btn = Button(root,
             text="Y",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=3, row=4)
btn = Button(root,
             text="La",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=3, row=5)
btn = Button(root,
             text="Ac",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=3, row=6)

# Fourth Coloumn Elements

btn = Button(root,
             text="Ti",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=4, row=3)
btn = Button(root,
             text="Zr",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=4, row=4)
btn = Button(root,
             text="Hf",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=4, row=5)
btn = Button(root,
             text="Rf",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=4, row=6)

# Fifth Coloumn Elements

btn = Button(root,
             text="V",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=5, row=3)
btn = Button(root,
             text="Nb",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=5, row=4)
btn = Button(root,
             text="Ta",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=5, row=5)
btn = Button(root,
             text="Db",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=5, row=6)

# Sixth Coloumn Elements

btn = Button(root,
             text="Cr",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=6, row=3)
btn = Button(root,
             text="Mo",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=6, row=4)
btn = Button(root,
             text="W",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=6, row=5)
btn = Button(root,
             text="Sg",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=6, row=6)

# Seventh Coloumn Elements

btn = Button(root,
             text="Mn",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=7, row=3)
btn = Button(root,
             text="Tc",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=7, row=4)
btn = Button(root,
             text="Re",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=7, row=5)
btn = Button(root,
             text="Bh",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=7, row=6)

# Eighth Coloumn Elements

btn = Button(root,
             text="Fe",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=8, row=3)
btn = Button(root,
             text="Ru",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=8, row=4)
btn = Button(root,
             text="Os",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=8, row=5)
btn = Button(root,
             text="Hs",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=8, row=6)

# Ninth Coloumn Elements

btn = Button(root,
             text="Co",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=9, row=3)
btn = Button(root,
             text="Rh",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=9, row=4)
btn = Button(root,
             text="Ir",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=9, row=5)
btn = Button(root,
             text="Mt",
             fg="silver",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=9, row=6)

# Tenth Coloumn Elements

btn = Button(root,
             text="Ni",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=10, row=3)
btn = Button(root,
             text="Pd",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=10, row=4)
btn = Button(root,
             text="Pt",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=10, row=5)
btn = Button(root,
             text="Ds",
             fg="silver",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=10, row=6)

# Eleventh Coloumn Elements

btn = Button(root,
             text="Cu",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=11, row=3)
btn = Button(root,
             text="Ag",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=11, row=4)
btn = Button(root,
             text="Au",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=11, row=5)
btn = Button(root,
             text="Rg",
             fg="silver",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=11, row=6)

# Twelveth Coloumn Elements

btn = Button(root,
             text="Zn",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=12, row=3)
btn = Button(root,
             text="Cd",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=12, row=4)
btn = Button(root,
             text="Hg",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=12, row=5)
btn = Button(root,
             text="Cn",
             fg="red",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=12, row=6)

# Thirteenth Coloumn Elements

btn = Button(root,
             text="B",
             fg="limegreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=13, row=1)
btn = Button(root,
             text="Al",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=13, row=2)
btn = Button(root,
             text="Ga",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=13, row=3)
btn = Button(root,
             text="In",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=13, row=4)
btn = Button(root,
             text="Tl",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=13, row=5)
btn = Button(root,
             text="Nh",
             fg="silver",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=13, row=6)

# Fourteenth Coloumn Elements

btn = Button(root,
             text="C",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=14, row=1)
btn = Button(root,
             text="Si",
             fg="limegreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=14, row=2)
btn = Button(root,
             text="Ge",
             fg="limegreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=14, row=3)
btn = Button(root,
             text="Sn",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=14, row=4)
btn = Button(root,
             text="Pb",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=14, row=5)
btn = Button(root,
             text="Fl",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=14, row=6)

# Fifteenth Coloumn Elements

btn = Button(root,
             text="N",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=15, row=1)
btn = Button(root,
             text="P",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=15, row=2)
btn = Button(root,
             text="As",
             fg="limegreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=15, row=3)
btn = Button(root,
             text="Sb",
             fg="limegreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=15, row=4)
btn = Button(root,
             text="Bi",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=15, row=5)
btn = Button(root,
             text="Mc",
             fg="silver",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=15, row=6)

# Sixteenth Coloumn Elements

btn = Button(root,
             text="O",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=16, row=1)
btn = Button(root,
             text="S",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=16, row=2)
btn = Button(root,
             text="Se",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=16, row=3)
btn = Button(root,
             text="Te",
             fg="limegreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=16, row=4)
btn = Button(root,
             text="Po",
             fg="green",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=16, row=5)
btn = Button(root,
             text="Lv",
             fg="silver",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=16, row=6)

# Seventeenth Coloumn Elements

btn = Button(root,
             text="F",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=17, row=1)
btn = Button(root,
             text="Cl",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=17, row=2)
btn = Button(root,
             text="Br",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=17, row=3)
btn = Button(root,
             text="I",
             fg="springgreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=17, row=4)
btn = Button(root,
             text="At",
             fg="limegreen",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=17, row=5)
btn = Button(root,
             text="Ts",
             fg="silver",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=17, row=6)

# Eighteenth Coloumn Elements

btn = Button(root,
             text="He",
             fg="skyblue",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=18, row=0)
btn = Button(root,
             text="Ne",
             fg="skyblue",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=18, row=1)
btn = Button(root,
             text="Ar",
             fg="skyblue",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=18, row=2)
btn = Button(root,
             text="Kr",
             fg="skyblue",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=18, row=3)
btn = Button(root,
             text="Xe",
             fg="skyblue",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=18, row=4)
btn = Button(root,
             text="Rn",
             fg="skyblue",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=18, row=5)
btn = Button(root,
             text="Og",
             fg="silver",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=18, row=6)

# Lathenide Series Elements

btn = Button(root,
             text="Ce",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=4, row=8, pady=20)
btn = Button(root,
             text="Pr",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=5, row=8, pady=20)
btn = Button(root,
             text="Nd",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=6, row=8, pady=20)
btn = Button(root,
             text="Pm",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=7, row=8, pady=20)
btn = Button(root,
             text="Cm",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=8, row=8, pady=20)
btn = Button(root,
             text="Eu",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=9, row=8, pady=20)
btn = Button(root,
             text="Gd",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=10, row=8, pady=20)
btn = Button(root,
             text="Tb",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=11, row=8, pady=20)
btn = Button(root,
             text="Dy",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=12, row=8, pady=20)
btn = Button(root,
             text="Ho",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=13, row=8, pady=20)
btn = Button(root,
             text="Er",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=14, row=8, pady=20)
btn = Button(root,
             text="Tm",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=15, row=8, pady=20)
btn = Button(root,
             text="Yb",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=16, row=8, pady=20)
btn = Button(root,
             text="Lu",
             fg="bisque",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=17, row=8, pady=20)

# Actinide Series Elements

btn = Button(root,
             text="Th",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=4, row=9, pady=1)
btn = Button(root,
             text="Pa",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=5, row=9, pady=1)
btn = Button(root,
             text="U",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=6, row=9, pady=1)
btn = Button(root,
             text="Np",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=7, row=9, pady=1)
btn = Button(root,
             text="Pu",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=8, row=9, pady=1)
btn = Button(root,
             text="Am",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=9, row=9, pady=1)
btn = Button(root,
             text="Cm",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=10, row=9, pady=1)
btn = Button(root,
             text="Bk",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=11, row=9, pady=1)
btn = Button(root,
             text="Cf",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=12, row=9, pady=1)
btn = Button(root,
             text="Es",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=13, row=9, pady=1)
btn = Button(root,
             text="Fm",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=14, row=9, pady=1)
btn = Button(root,
             text="Md",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=15, row=9, pady=1)
btn = Button(root,
             text="No",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=16, row=9, pady=1)
btn = Button(root,
             text="Lr",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=4,
             height=2,
             command=lambda: detail("Li", "Lithium"))
btn.grid(column=17, row=9, pady=1)

# holding the screen
root.mainloop()
