from Tkinter import *
import tkMessageBox

class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.minsize(width=300,height=50)
        self.root.maxsize(width=300,height=110)
        self.root.wm_title("Milliseconds Conversion")
        self.label = Label (self.root, text= "Enter value in Milliseconds.")
        self.label.pack()


        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        self.buttontext = StringVar()
        self.buttontext.set("Calculate Seconds")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()
        Button(self.root, text="Calculate Minutes", command=self.clicked2).pack()

        self.label = Label (self.root, text="")
        self.label.pack()

        self.root.mainloop()


    def clicked1(self):
        input = self.entrytext.get()
        result = float(input)/1000
        self.label.configure(text="Seconds = " + str(result))
        return result

    def clicked2(self):
        result = App.clicked1(self) / 60
        self.label.configure(text="Minutes = " + str(result))

    def button_click(self, e):
        pass

App()
