from tkinter import *

class Calculator():

    def __init__(self, root):
        self.root=root
        self.mylabel=Label(root, text='my test label')
        self.entry=Entry(root, width=35,)
        self.entry.grid(row=0, column=0, columnspan=3, ipadx=13, ipady=20)
        self.num_button_call()
        self.exe_button_call()

    def exe_command(self, exe_type):
        if exe_type == 'c':
            self.entry.delete(0, END)
        self.last_value=self.entry.get()
        self.entry.delete(0, END)
        self.type=exe_type

    def exe_command_dec(self):
        current=self.entry.get()
        self.entry.delete(0, END)
        if not '.' in current:
            self.entry.insert(0, current+'.')
        else:
            self.entry.insert(0, current)
        

    def exe_command_equal(self):
        new_value=self.entry.get()
        self.entry.delete(0, END)
        try:
            last_value=float(self.last_value)
            new_value=float(new_value)
            if self.type=='+':
                self.entry.insert(0, last_value+new_value)
            if self.type=='-':
                self.entry.insert(0, last_value-new_value)
            if self.type=='*':
                self.entry.insert(0, last_value*new_value)
            if self.type=='/':
                try:
                    self.entry.insert(0, last_value/new_value)
                except ZeroDivisionError:
                    self.entry.insert(0, 'zeroDivisionError')
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(0, 'unknown value')
        
                

    def exe_button(self):
        button_add=Button(self.root, text='+', command=lambda: self.exe_command('+'))
        button_sub=Button(self.root, text='-', command=lambda: self.exe_command('-'))
        button_div=Button(self.root, text='/', command=lambda: self.exe_command('/'))
        button_mult=Button(self.root, text='*', command=lambda: self.exe_command('*'))
        button_dec=Button(self.root, text='.', command=lambda: self.exe_command_dec())
        button_equal=Button(self.root, text='=', command=lambda: self.exe_command_equal(), width=15, bg='#102132', fg='white')
        button_clear=Button(self.root, text='C', command=lambda: self.exe_command('c'),bg='#f74a4a', fg='white')
        return button_add, button_sub, button_div, button_mult, button_equal, button_clear, button_dec
    
    def exe_button_call(self):
        self.exe_button()[0].grid(row=4, column=1, ipadx=31, ipady=15 )
        self.exe_button()[1].grid(row=4, column=2, ipadx=33, ipady=15 )
        self.exe_button()[2].grid(row=6, column=0, ipadx=34.5, ipady=15 )
        self.exe_button()[3].grid(row=6, column=1, ipadx=33, ipady=15 )
        self.exe_button()[4].grid(row=7, column=1, ipadx=30, ipady=15, columnspan=2 )
        self.exe_button()[5].grid(row=7, column=0, ipadx=33, ipady=15 )
        self.exe_button()[6].grid(row=6, column=2, ipadx=33, ipady=15, columnspan=3 )


        
    def num_buttons(self):
        button_1=Button(self.root, text='1', command=lambda: self.num_button(1))
        button_2=Button(self.root, text='2', command=lambda: self.num_button(2))
        button_3=Button(self.root, text='3', command=lambda: self.num_button(3))
        button_4=Button(self.root, text='4', command=lambda: self.num_button(4))
        button_5=Button(self.root, text='5', command=lambda: self.num_button(5))
        button_6=Button(self.root, text='6', command=lambda: self.num_button(6))
        button_7=Button(self.root, text='7', command=lambda: self.num_button(7))
        button_8=Button(self.root, text='8', command=lambda: self.num_button(8))
        button_9=Button(self.root, text='9', command=lambda: self.num_button(9))
        button_0=Button(self.root, text='0', command=lambda: self.num_button(0))
        return button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0
    
    def num_button_call(self):
        self.num_buttons()[0].grid(row=1, column=0, ipadx=33, ipady=15)
        self.num_buttons()[1].grid(row=1, column=1, ipadx=33, ipady=15)
        self.num_buttons()[2].grid(row=1, column=2, ipadx=33, ipady=15)
        self.num_buttons()[3].grid(row=2, column=0, ipadx=33, ipady=15)
        self.num_buttons()[4].grid(row=2, column=1, ipadx=33, ipady=15)
        self.num_buttons()[5].grid(row=2, column=2, ipadx=33, ipady=15)
        self.num_buttons()[6].grid(row=3, column=0, ipadx=33, ipady=15)
        self.num_buttons()[7].grid(row=3, column=1, ipadx=33, ipady=15)
        self.num_buttons()[8].grid(row=3, column=2, ipadx=33, ipady=15)
        self.num_buttons()[9].grid(row=4, column=0, ipadx=33, ipady=15)

    def num_button(self, value):
        if self.entry.get()=='zeroDivisionError' or self.entry.get()=='unknown value':
            self.entry.delete(0, END)
        e=self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, e+str(value))
        
            
if __name__ == '__main__':
    root=Tk()
    root.title('pyinc-calculator')
    root.resizable(width=False, height=False)
    calculator = Calculator(root)
    root.mainloop()
