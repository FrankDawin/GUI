## GUI advanced


import tkinter as tk



class app(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.master = self
        self.maker_main()
##        the_entry = tk.StringVar()

    def maker_main(self):
        self.a = calculator(self.master).pack()
        self.b = cal_entry(self.master).pack()
        self.c = menu(self.master)



class calculator(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.maker()
        

    def maker(self):
        tk.Button(self,text="1",width=3).grid(row=0, column=0)
        tk.Button(self,text="2",width=3).grid(row=0, column=1)
        tk.Button(self,text="3",width=3).grid(row=0, column=2)
        tk.Button(self,text="4",width=3).grid(row=1, column=0)
        tk.Button(self,text="5",width=3).grid(row=1, column=1)
        tk.Button(self,text="6",width=3).grid(row=1, column=2)
        tk.Button(self,text="7",width=3).grid(row=2, column=0)
        tk.Button(self,text="8",width=3).grid(row=2, column=1)
        tk.Button(self,text="9",width=3).grid(row=2, column=2)
        tk.Button(self,text="0",width=3).grid(row=3, column=0)
        tk.Button(self,text=",",width=3).grid(row=3, column=1)



class cal_entry(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.maker()

    def maker(self):
        tk.Entry(self.master).pack()



class menu(tk.Menu):

    def __init__(self, master):
        tk.Menu.__init__(self, master)
        self.master = master
        self.maker()

    def maker(self):

        ## Main menu
        self.master.config(menu = self)

        ## Sub menu 1
        self.file_menu = tk.Menu(self)
        self.add_cascade(label = "File", menu = self.file_menu)
        self.file_menu.add_command(label = "New file....")

        ## Sub menu 2
        self.edit_menu = tk.Menu(self)
        self.add_cascade(label = "Edit", menu = self.edit_menu)
        self.edit_menu.add_command(label = "Other file....")        



if __name__ == "__main__":
    theapp = app()
    theapp.mainloop()
