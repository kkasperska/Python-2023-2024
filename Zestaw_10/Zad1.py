from tkinter import *
import random

def rzut():
    kostka = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(kostka)}')
    label.pack()

root = Tk()
root.configure(bg="white")
root.geometry("550x400")
root.title("Rzut kostką")


przycisk = Button(root, text="Rzut!", width=8, height=2, font=20, bg="light pink", bd=2, command= rzut)
przycisk.pack(padx=0, pady=15)
label = Label(root, font=("times", 300), bg="white", fg="light blue")
root.mainloop()