from tkinter import *
window = Tk()
window.title('Semestral Grade')
window.geometry("400x300+20+10")

class Mywindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Semestral Grade")
        self.lbl1.place(relx=0.50, y=50, anchor="center")
        self.lbl2 = Label(window, text="Prelim Grade")
        self.lbl2.place(x=50, y=80)
        self.txtfld2 = Entry(window, bd=3)
        self.txtfld2.place(x=180, y=80)
        self.lbl3 = Label(window, text="Midterm Grade")
        self.lbl3.place(x=50, y=120, )
        self.txtfld3 = Entry(window, bd=3)
        self.txtfld3.place(x=180, y=120)
        self.lbl4 = Label(window, text="Final Grade")
        self.lbl4.place(x=50, y=160, )
        self.txtfld4 = Entry(window, bd=3)
        self.txtfld4.place(x=180, y=160)
        self.btn1 = Button(window, text="Semestral Grade", command=self.Grade)
        self.btn1.place(relx=0.50, y=220, anchor="center")
        self.txtfld5 = Entry(window, bd=3)
        self.txtfld5.place(relx=.50, y=250, anchor= "center")

    def Grade(self):
        self.txtfld5.delete(0, 'end')
        Prelim = int(self.txtfld2.get())
        Midterm = int(self.txtfld3.get())
        Final = int(self.txtfld4.get())
        Grade = Prelim * .30 + Midterm * .30 + Final * .40
        self.txtfld5.insert(END, str(Grade))


mywin =Mywindow(window)
window.mainloop()
