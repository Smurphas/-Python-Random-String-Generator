import random
import time
from tkinter import*


char_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
char_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
char = [char_lower]
charcount = 10

file = open("passwords.txt", "w")
window = Tk()


window.title("Random String Generator")

window.geometry('700x500')
t = Text(window, width=40, height=10)


def generate():
    charcount=int(a.get())
    while charcount>0:
        charcount-=1
        g = random.choice(char)
        g = random.choice(g)
        t.insert(END, g)
        with open("passwords.txt", "w") as f:
            f.write(str(g))
    t.insert(END, " ")

def use_upper():
    if char_upper in char:
        char.remove(char_upper)
    else:
        char.append(char_upper)
def use_num():
    if char_num in char:
        char.remove(char_num)
    else:
        char.append(char_num)

def reset():
    t.delete("1.0", "end")

Label(window, text="How many characters?:", font=('Calibri 10')).pack()
a=Entry(window, width=35)
a.pack()

check_upp = Checkbutton(window, text='Use Upper Case', command=use_upper)
check_upp.pack()

check_num = Checkbutton(window, text='Use Numbers', command=use_num)
check_num.pack()


label=Label(window, text="Generated number ", font=('Calibri 15'))
label.pack(pady=20)

Button(window, text="Generate", command=generate).pack()
Button(window, text="Reset", command=reset).pack()
t.pack()

file.close()
window.mainloop()