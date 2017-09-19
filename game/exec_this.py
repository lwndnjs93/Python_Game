from tkinter import *
from PIL import Image, ImageTk
import os

class App:
    def __init__(self, Parent):
        self.myParent = Parent
        self.F = Frame(Parent)
        self.myParent.geometry("800x800")
        self.myParent.title("미니게임천국")
        self.myParent.resizable(width = False, height = False)
        self.F.pack()

        bg_image =  PhotoImage(file="background1.png")

        self.control_frame = Frame(self.myParent, bg="green", width=600, height=800)
        self.control_frame.backimg = Label(image = bg_image)
        self.control_frame.backimg.image = bg_image
        self.control_frame.backimg.pack(side=RIGHT)

        self.left_frame = Frame(self.myParent)
        self.left_frame.pack(side=LEFT, expand=NO, fill=Y)

        self.button1 = Button(self.left_frame)
        self.button1.photo=PhotoImage(file="turtle1.png")
        self.button1.config(image=self.button1.photo,width="200",height="200")
        self.button1.pack()
        self.button1.bind("<Button-1>", self.button1Click)
     #  self.button1.bind("<Enter>", self.button1Enter)
     #  self.button1.bind("<Leave>", self.button1Enter)

        self.button2 = Button(self.left_frame)
        self.button2.photo=PhotoImage(file="brick1.png")
        self.button2.config(image=self.button2.photo,width="200",height="200")
        self.button2.pack()
        self.button2.bind("<Button-1>", self.button2Click)
     #  self.button2.bind("<Enter>", self.button2Enter)
     #  self.button2.bind("<Leave>", self.button2Enter)

        self.button3 = Button(self.left_frame)
        self.button3.photo=PhotoImage(file="pingpong1.png")
        self.button3.config(image=self.button3.photo,width="200",height="200")
        self.button3.pack()
        self.button3.bind("<Button-1>", self.button3Click)
     #  self.button3.bind("<Enter>", self.button3Enter)
     #  self.button3.bind("<Leave>", self.button3Enter)

        self.button4 = Button(self.left_frame)
        self.button4.photo=PhotoImage(file="marioworld1.png")
        self.button4.config(image=self.button4.photo,width="200",height="200")
        self.button4.pack()
        self.button4.bind("<Button-1>", self.button4Click)
     #  self.button4.bind("<Enter>", self.button4Enter)
     #  self.button4.bind("<Leave>", self.button4Enter)


    def button1Click(self, event):
        os.chdir("./turtle_game")
        os.system("python .")
        os.chdir("..")
        self.control_frame.config(bg="yellow")
        self.control_frame.pack()

    def button2Click(self, event):
        os.chdir("./brickbreak")
        os.system("python .")
        os.chdir("..")

    def button3Click(self, event):
        os.chdir("./pingpong")
        os.system("python .")
        os.chdir("..")

    def button4Click(self, event):
        os.chdir("./marioworld")
        os.system("python .")
        os.chdir("..")
'''
    def button1Enter(self, event):

    def button2Enter(self, event):

    def button3Enter(self, event):
        self.control_frame.config(background="yellow")

    def button4Enter(self, event):
        self.control_frame.config(background="yellow")

    def button1Leave(self, event):
        self.control_frame.config(background="yellow")

    def button2Leave(self, event):
        self.control_frame.config(background="yellow")

    def button3Leave(self, event):
        self.control_frame.config(background="yellow")

    def button4Leave(self, event):
        self.control_frame.config(background="yellow")
'''
root=Tk()
App = App(root)
root.mainloop()


