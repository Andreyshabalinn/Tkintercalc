from tkinter import *
class Calculator:
    def __init__(self,master):
        self.lbl = Label(root, width=20, text='Шрекный калькулятор')
        self.n1 = Entry(root, width=20)
        self.n2 = Entry(root, width=20)
        self.plus = Button(root, width=20, text='+')
        self.minus = Button(root, width=20, text='-')
        self.umnozh = Button(root, width=20, text='*')
        self.delit = Button(root, width=20, text='/')
        self.vivod = Label(root, width=20)

        self.plus['command'] = eval('self.'+ 'func_plus')
        self.minus['command'] = eval('self.' + 'func_minus')
        self.umnozh['command'] = eval('self.' + 'func_umnozh')
        self.delit['command'] = eval('self.' + 'func_delit')
        self.lbl.pack()
        self.n1.pack()
        self.n2.pack()
        self.plus.pack()
        self.minus.pack()
        self.umnozh.pack()
        self.delit.pack()
        self.vivod.pack()
    def func_plus(self):
        try:
            a = float(self.n1.get())
            b = float(self.n2.get())
            self.vivod['text'] = str (a+b)
        except:
            self.vivod['text'] = 'Что то пошло не так...'
    def func_minus(self):
        try:
            a = float(self.n1.get())
            b = float(self.n2.get())
            self.vivod['text'] = str (a-b)
        except:
            self.vivod['text'] = 'Что то пошло не так...'
    def func_umnozh(self):
        try:
            a = float(self.n1.get())
            b = float(self.n2.get())
            self.vivod['text'] = str (a*b)
        except:
            self.vivod['text'] = 'Что то пошло не так...'
    def func_delit(self):
        try:
            a = float(self.n1.get())
            b = float(self.n2.get())
            self.vivod['text'] = str (a/b)
        except:
            self.vivod['text'] = 'Что то пошло не так...'
root = Tk()

calculator = Calculator(root)
root.geometry("400x400+300+300")
root.title = "Шрекный калькулятор"
root.colormapwindows = "green"
root.mainloop()


