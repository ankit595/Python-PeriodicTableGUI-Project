# importing libraries
import tkinter
from tkinter import *
from tkinter import messagebox
import auto_py_to_exe
import tkinter.font as font

# create root window
root = Tk()

# root window title and dimension
root.title("Periodic Table")
root.geometry('1200x600')

myFont = font.Font(size=15)

# defining the function
def detail(element, name,no,mass,bl,pr,yr):
    msg = messagebox.Message(root,
                             message=f"Symbol: {element}\nAtomic Number: {no}\nElement: {name}\nAtomic Mass: {mass}\nBlock: {bl}\nProperty: {pr}\nDiscovery Year: {yr}"
    )
    msg.show()



# First Coloumn Elements

btn = Button(root,

             text="H",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("H", "Hydrogen","1","1.0079","s","Nonmetal","1776"))
# do this for all elements
btn.grid(column=1, row=0)
btn = Button(root,
             text="Li",
             fg="orange",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Li","Lithium","3","6.941","s","Alkali Metal","1817"))
btn.grid(column=1, row=1)
btn = Button(root,
             text="Na",
             fg="orange",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Na", "Sodium","11","22.9897","s","Alkali Metal","1807"))
btn.grid(column=1, row=2)
btn = Button(root,
             text="K",
             fg="orange",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("K", "Potassium","19","39.0983","s","Alkali Metal","1807"))
btn.grid(column=1, row=3)
btn = Button(root,
             text="Rb",
             fg="orange",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Rb", "Rubidium","37","85.4678","s","Alkali Metal","1861"))
btn.grid(column=1, row=4)
btn = Button(root,
             text="Cs",
             fg="orange",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Cs", "Cesium","55","132.9055","s","Alkali Metal","1860"))
btn.grid(column=1, row=5)
btn = Button(root,
             text="Fr",
             fg="orange",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Fr", "Francium","87","223","s","Alkali Metal","1939"))
btn.grid(column=1, row=6)

# Second Coloumn Elements

btn = Button(root,
             text="Be",
             fg="yellow",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Be", "Beryllium","4","9.0122","s","Alkali Earth Metal","1797"))
btn.grid(column=2, row=1)
btn = Button(root,
             text="Mg",
             fg="yellow",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Mg", "Magnesium","12","24.305","s","Alkali Earth Metal","1755"))
btn.grid(column=2, row=2)
btn = Button(root,
             text="Ca",
             fg="yellow",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ca", "Calcium","20","40.078","s","Alkali Earth Metal","1808"))
btn.grid(column=2, row=3)
btn = Button(root,
             text="Sr",
             fg="yellow",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Sr","Strontium","38","87.62","s","Alkali Earth Metal","1790"))
btn.grid(column=2, row=4)
btn = Button(root,
             text="Ba",
             fg="yellow",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ba","Barium","56","137.327","s","Alkali Earth Metal","1808"))
btn.grid(column=2, row=5)
btn = Button(root,
             text="Ra",
             fg="yellow",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ra","Radium","88","226","s","Alkali Earth Metal","1898"))
btn.grid(column=2, row=6)

# Third Coloumn Elements

btn = Button(root,
             text="Sc",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Sc","Scandium","21","44.9559","d","Transition Metal","1879"))
btn.grid(column=3, row=3)
btn = Button(root,
             text="Y",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command =lambda: detail("Y","Yttrium","39","88.9059","d","Transition Metal","1794"))
btn.grid(column=3, row=4)
btn = Button(root,
             text="La",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command =lambda: detail("La","Lanthanum","57","138.9055","d","Transition Metal","1839"))
btn.grid(column=3, row=5)
btn = Button(root,
             text="Ac",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command =lambda: detail("Ac","Actinium","89","227","d","Transition Metal","1899"))
btn.grid(column=3, row=6)

# Fourth Coloumn Elements

btn = Button(root,
             text="Ti",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ti","Titanium","22","47.867","d","Transition Metal","1791"))
btn.grid(column=4, row=3)
btn = Button(root,
             text="Zr",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Zr","Zirconium","40","91.224","d","Transition Metal","1789"))
btn.grid(column=4, row=4)
btn = Button(root,
             text="Hf",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Hf","Hafnium","72","178.49","d","Transition Metal","1923"))
btn.grid(column=4, row=5)
btn = Button(root,
             text="Rf",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Rf","Rutherfordium","104","261","d","Transition Metal","1964"))
btn.grid(column=4, row=6)

# Fifth Coloumn Elements

btn = Button(root,
             text="V",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("V","Vanadium","23","50.9415","d","Transition Metal","1830"))
btn.grid(column=5, row=3)
btn = Button(root,
             text="Nb",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Nb","Niobium","41","92.9064","d","Transition Metal","1801"))
btn.grid(column=5, row=4)
btn = Button(root,
             text="Ta",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ta","Tantalum","73","180.9479","d","Transition Metal","1802"))
btn.grid(column=5, row=5)
btn = Button(root,
             text="Db",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Db","Dubnium","105","262","d","Transition Metal","1967"))
btn.grid(column=5, row=6)

# Sixth Coloumn Elements

btn = Button(root,
             text="Cr",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Cr","Chromium","24","51.9961","d","Transition Metal","1797"))
btn.grid(column=6, row=3)
btn = Button(root,
             text="Mo",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Mo","Molybdenum","42","95.94","d","Transition Metal","1781"))
btn.grid(column=6, row=4)
btn = Button(root,
             text="W",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("W","Tungsten","74","183.84","d","Transition Metal","1783"))
btn.grid(column=6, row=5)
btn = Button(root,
             text="Sg",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Sg","Seaborgium","106","266","d","Transition Metal","1974"))
btn.grid(column=6, row=6)

# Seventh Coloumn Elements

btn = Button(root,
             text="Mn",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Mn","Manganese","25","54.938","d","Transition Metal","1774"))
btn.grid(column=7, row=3)
btn = Button(root,
             text="Tc",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Tc","Technetium","43","98","d","Transition Metal","1937"))
btn.grid(column=7, row=4)
btn = Button(root,
             text="Re",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Re","Rhenium","75","186.207","d","Transition Metal","1925"))
btn.grid(column=7, row=5)
btn = Button(root,
             text="Bh",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Bh","Bohrium","107","264","d","Transition Metal","1981"))
btn.grid(column=7, row=6)

# Eighth Coloumn Elements

btn = Button(root,
             text="Fe",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Fe","Iron","26","55.845","d","Transition Metal","Ancient"))
btn.grid(column=8, row=3)
btn = Button(root,
             text="Ru",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ru","Ruthenium","44","101.07","d","Transition Metal","1844"))
btn.grid(column=8, row=4)
btn = Button(root,
             text="Os",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Os","Osmium","76","190.23","d","Transition Metal","1803"))
btn.grid(column=8, row=5)
btn = Button(root,
             text="Hs",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Hs","Hassium","108","277","d","Transition Metal","1984"))
btn.grid(column=8, row=6)

# Ninth Coloumn Elements

btn = Button(root,
             text="Co",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Co","Cobalt","27","58.9332","d","Transition Metal","1735"))
btn.grid(column=9, row=3)
btn = Button(root,
             text="Rh",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command =lambda: detail("Rh","Rhodium","45","102.9055","d","Transition Metal","1803"))
btn.grid(column=9, row=4)
btn = Button(root,
             text="Ir",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ir","Iridium","77","196.9665","d","Transition Metal","Ancient"))
btn.grid(column=9, row=5)
btn = Button(root,
             text="Mt",
             fg="silver",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Mt","Meitnerium","109","2628","d","Transition Metal","1968"))
btn.grid(column=9, row=6)

# Tenth Coloumn Elements

btn = Button(root,
             text="Ni",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ni","Nickel","28","58.6934","d","Transition Metal","1751"))
btn.grid(column=10, row=3)
btn = Button(root,
             text="Pd",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Pd","Palladium","46","106.42","d","Transition Metal","1803"))
btn.grid(column=10, row=4)
btn = Button(root,
             text="Pt",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Pt","Platinum","78","192.217","d","Transition Metal","1803"))
btn.grid(column=10, row=5)
btn = Button(root,
             text="Ds",
             fg="silver",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ds","Darmstadtium","110","261.9","d","Transition Metal","1994"))
btn.grid(column=10, row=6)

# Eleventh Coloumn Elements

btn = Button(root,
             text="Cu",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Cu","Copper","29","60.546","d","Transition Metal","Ancient"))
btn.grid(column=11, row=3)
btn = Button(root,
             text="Ag",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command =lambda: detail("Ag","Silver","47","107.8682","d","Transition Metal","Ancient"))
btn.grid(column=11, row=4)
btn = Button(root,
             text="Au",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command =lambda: detail("Au","Gold","79","195.078","d","Transition Metal","1735"))
btn.grid(column=11, row=5)
btn = Button(root,
             text="Rg",
             fg="silver",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Rg","Roentgenium","111","271.8","d","Transition Metal","1994"))
btn.grid(column=11, row=6)

# Twelveth Coloumn Elements

btn = Button(root,
             text="Zn",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Zn","Zinc","30","65.39","d","Transition Metal","Ancient"))
btn.grid(column=12, row=3)
btn = Button(root,
             text="Cd",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Cd","Cadmium","48","112.411","d","Transition Metal","1817"))
btn.grid(column=12, row=4)
btn = Button(root,
             text="Hg",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Hg","Mercury","80","200.59","d","Transition Metal","Ancient"))
btn.grid(column=12, row=5)
btn = Button(root,
             text="Cn",
             fg="red",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Cn","Copernicium","112","285","d","Transition Metal","1996"))
btn.grid(column=12, row=6)

# Thirteenth Coloumn Elements

btn = Button(root,
             text="B",
             fg="limegreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("B","Boron","5","10.811","p","Metalloid","1888"))
btn.grid(column=13, row=1)
btn = Button(root,
             text="Al",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Al","Aluminum","13","26.9815","p","Post-Transition Metal","1825"))
btn.grid(column=13, row=2)
btn = Button(root,
             text="Ga",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ga","Gallium","31","69.723","p","Post-Transition Metal","1875"))
btn.grid(column=13, row=3)
btn = Button(root,
             text="In",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("In","Indium","49","114.818","p","Post-Transition Metal","1863"))
btn.grid(column=13, row=4)
btn = Button(root,
             text="Tl",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Tl","Thallium","81","204.3833","p","Post-Transition Metal","1861"))
btn.grid(column=13, row=5)
btn = Button(root,
             text="Nh",
             fg="silver",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command =lambda: detail("Nh","Nihonium","113","286","p","Post-Transition Metal","2003"))
btn.grid(column=13, row=6)

# Fourteenth Coloumn Elements

btn = Button(root,
             text="C",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("C","Carbon","6","12.0107","p","Nonmetal","Ancient"))
btn.grid(column=14, row=1)
btn = Button(root,
             text="Si",
             fg="limegreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Si","Silicon","14","28.0855","p","Metalloid","1824"))
btn.grid(column=14, row=2)
btn = Button(root,
             text="Ge",
             fg="limegreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ge","Germanium","32","72.64","p","Metalloid","1886"))
btn.grid(column=14, row=3)
btn = Button(root,
             text="Sn",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Sn","Tin","50","118.71","p","Post-Transition Metal","Ancient"))
btn.grid(column=14, row=4)
btn = Button(root,
             text="Pb",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Pb","Lead","82","207.2","p","Post-Transition Metal","Ancient"))
btn.grid(column=14, row=5)
btn = Button(root,
             text="Fl",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Fl","Flerovium","114","289","p","Post-Transition Metal","1998"))
btn.grid(column=14, row=6)

# Fifteenth Coloumn Elements

btn = Button(root,
             text="N",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("N","Nitrogen","7","14.0067","p","Nonmetal","1772"))
btn.grid(column=15, row=1)
btn = Button(root,
             text="P",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("P","Phosphorus","15","30.9738","p","Nonmetal","1669"))
btn.grid(column=15, row=2)
btn = Button(root,
             text="As",
             fg="limegreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("As","Arsenic","33","74.9216","p","Metalloid","Ancient"))
btn.grid(column=15, row=3)
btn = Button(root,
             text="Sb",
             fg="limegreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Sb","Antimony","51","121.76","p","Metalloid","Ancient"))
btn.grid(column=15, row=4)
btn = Button(root,
             text="Bi",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Bi","Bismuth","83","208.9804","p","TPost-Transition Metal","Ancient"))
btn.grid(column=15, row=5)
btn = Button(root,
             text="Mc",
             fg="silver",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command =lambda: detail("Mc","Moscovium","115","288","p","Post-Transition Metal","2010"))
btn.grid(column=15, row=6)

# Sixteenth Coloumn Elements

btn = Button(root,
             text="O",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("O","Oxygen","8","15.9994","p","Nonmetal","1774"))
btn.grid(column=16, row=1)
btn = Button(root,
             text="S",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("S","Sulphur","16","32.065","p","Nonmetal","Ancient"))
btn.grid(column=16, row=2)
btn = Button(root,
             text="Se",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Se","Selenium","34","78.96","p","Nonmetal","1817"))
btn.grid(column=16, row=3)
btn = Button(root,
             text="Te",
             fg="limegreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Te","Tellurium","52","127.6","p","Metalloid","1783"))
btn.grid(column=16, row=4)
btn = Button(root,
             text="Po",
             fg="green",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Po","Polonium","84","209","p","Metalloid","1898"))
btn.grid(column=16, row=5)
btn = Button(root,
             text="Lv",
             fg="silver",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Lv","Livermorium","116","293","p","Post-Transition Metal","2000"))
btn.grid(column=16, row=6)

# Seventeenth Coloumn Elements

btn = Button(root,
             text="F",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("F","Fluorine","9","18.9984","p","Halogen","1886"))
btn.grid(column=17, row=1)
btn = Button(root,
             text="Cl",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Cl","Chlorine","17","35.453","p","Halogen"," 1774"))
btn.grid(column=17, row=2)
btn = Button(root,
             text="Br",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Br","Bromine","35","79.904","p","Halogen","1826"))
btn.grid(column=17, row=3)
btn = Button(root,
             text="I",
             fg="springgreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("I","Iodine","53","126.9045","p","Halogen","1811"))
btn.grid(column=17, row=4)
btn = Button(root,
             text="At",
             fg="limegreen",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("At","Astatine","85","210","p","Halogen","1967"))
btn.grid(column=17, row=5)
btn = Button(root,
             text="Ts",
             fg="silver",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ts","Tennessine","117","260.9","p","Halogen","2010"))
btn.grid(column=17, row=6)

# Eighteenth Coloumn Elements

btn = Button(root,
             text="He",
             fg="skyblue",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("He","Helium","2","4.0026","p","Noble Gas","1895"))
btn.grid(column=18, row=0)
btn = Button(root,
             text="Ne",
             fg="skyblue",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ne","Neon","10","262","p","Noble Gas"," 1898"))
btn.grid(column=18, row=1)
btn = Button(root,
             text="Ar",
             fg="skyblue",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ar","Argon","18","39.948","p","Noble Gas","1894"))
btn.grid(column=18, row=2)
btn = Button(root,
             text="Kr",
             fg="skyblue",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Kr","Krypton","36","79.904","p","Noble Gas","1898"))
btn.grid(column=18, row=3)
btn = Button(root,
             text="Xe",
             fg="skyblue",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Xe","Xenon","54","131.293","p","Noble Gas","1898"))
btn.grid(column=18, row=4)
btn = Button(root,
             text="Rn",
             fg="skyblue",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Rn","Radon","86","222","p","Noble Gas","1900"))
btn.grid(column=18, row=5)
btn = Button(root,
             text="Og",
             fg="silver",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Og","Oganesson","118","294","p","Noble Gas","2006"))
btn.grid(column=18, row=6)

# Lathenide Series Elements

btn = Button(root,
             text="Ce",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ce","Cerium","58","140.116","f","Lanthanide","1803"))
btn.grid(column=4, row=8, pady=20)
btn = Button(root,
             text="Pr",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Pr","Praseodymium","59","140.9077","f","Lanthanide","1885"))
btn.grid(column=5, row=8, pady=20)
btn = Button(root,
             text="Nd",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Nd","Neodymium","60","144.24","f","Lanthanide","1885"))
btn.grid(column=6, row=8, pady=20)
btn = Button(root,
             text="Pm",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Pm","Promethium","61","145","f","Lanthanide","1945"))
btn.grid(column=7, row=8, pady=20)
btn = Button(root,
             text="Sm",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Sm","Samarium","62","150.36","f","Lanthanide","1879"))
btn.grid(column=8, row=8, pady=20)
btn = Button(root,
             text="Eu",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Eu","Europium","63","151.964","f","Lanthanide","1901"))
btn.grid(column=9, row=8, pady=20)
btn = Button(root,
             text="Gd",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Gd","Gadolinium","64","157.25","f","Lanthanide","1880"))
btn.grid(column=10, row=8, pady=20)
btn = Button(root,
             text="Tb",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Tb","Terbium","65","158.9253","f","Lanthanide","1843"))
btn.grid(column=11, row=8, pady=20)
btn = Button(root,
             text="Dy",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Dy","Dysprosium","66","162.5","f","Lanthanide","1886"))
btn.grid(column=12, row=8, pady=20)
btn = Button(root,
             text="Ho",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Ho","Holmium","67","164.9303","f","Lanthanide","1867"))
btn.grid(column=13, row=8, pady=20)
btn = Button(root,
             text="Er",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Er","Erbium","68","167.259","f","Lanthanide","1842"))
btn.grid(column=14, row=8, pady=20)
btn = Button(root,
             text="Tm",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Tm","Thulium","69","168.9342","f","Lanthanide","1879"))
btn.grid(column=15, row=8, pady=20)
btn = Button(root,
             text="Yb",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Yb","Ytterbium","70","173.04","f","Lanthanide","1878"))
btn.grid(column=16, row=8, pady=20)
btn = Button(root,
             text="Lu",
             fg="bisque",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Lu","Lutetium","71","174.967","f","Lanthanide","1907"))
btn.grid(column=17, row=8, pady=20)

# Actinide Series Elements

btn = Button(root,
             text="Th",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Th","Thorium","90","232.0381","f","Actinide","1829"))
btn.grid(column=4, row=9, pady=1)

btn = Button(root,
             text="Pa",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Pa","Protactinium","91","231.0359","f","Actinide","1913"))
btn.grid(column=5, row=9, pady=1)

btn = Button(root,
             text="U",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("U","Uranium","92","238.0289","f","Actinide","1789"))
btn.grid(column=6, row=9, pady=1)

btn = Button(root,
             text="Np",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Np","Neptunium","93","237","f","Actinide","1940"))
btn.grid(column=7, row=9, pady=1)

btn = Button(root,
             text="Pu",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Pu","Plutonium","94","244","f","Actinide","1940"))
btn.grid(column=8, row=9, pady=1)

btn = Button(root,
             text="Am",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Am","Americium","95","243","f","Actinide","1944"))
btn.grid(column=9, row=9, pady=1)

btn = Button(root,
             text="Cm",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Cm","Curium","96","247","f","Actinide","1944"))
btn.grid(column=10, row=9, pady=1)
btn = Button(root,
             text="Bk",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Bk","Berkelium","97","247","f","Actinide","1949"))
btn.grid(column=11, row=9, pady=1)
btn = Button(root,
             text="Cf",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Cf","Californium","98","251","f","Actinide","1950"))
btn.grid(column=12, row=9, pady=1)
btn = Button(root,
             text="Es",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Es","Einsteinium","99","252","f","Actinide","1952"))
btn.grid(column=13, row=9, pady=1)
btn = Button(root,
             text="Fm",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Fm","Fermium","100","257","f","Actinide","1952"))
btn.grid(column=14, row=9, pady=1)
btn = Button(root,
             text="Md",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Md","Mendelevium","101","258","f","Actinide","1955"))
btn.grid(column=15, row=9, pady=1)
btn = Button(root,
             text="No",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("No","Nobelium","102","259","f","Actinide","1958"))
btn.grid(column=16, row=9, pady=1)
btn = Button(root,
             text="Lr",
             fg="lightsalmon",
             bg="black",
             bd=7,
             width=6,
             height=2,
             command=lambda: detail("Lr","Lawrencium","103","262","f","Actinide","1961"))
btn.grid(column=17, row=9, pady=1)



# holding the screen
root.mainloop()
