## Multi frame GUI

import tkinter as tk



class App(tk.Tk):
    """The main tk instance"""

    def __init__(self):
        tk.Tk.__init__(self)
        self.master = self
        self.title("Title")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand = True)
        
        self.frames = {}
        self.content()
        

    def content(self):
        """Adding all tk.Frames to the dict"""

        for f in (Home, Calculator):
            frame = f(self.container, self)
            self.frames[f] = frame
            frame.pack(fill="both")
        

    def show_frame(self, name):
        """Put the desired frame on top"""

        frame = self.frames[name]
        frame.tkraise()

    

class Home(tk.Frame):
    """Win1 frame"""

    def __init__(self, master, controller):

        tk.Frame.__init__(self, master)
        self.master = master
        self.content()
        self.pack()

    def content(self):
        """adding panel to frame"""

        main_panel = tk.PanedWindow()
        main_panel.pack(fill=tk.BOTH, expand=1)

        left = tk.Label(main_panel, text="Main application windows")
        main_panel.add(left)

        m2 = tk.PanedWindow(main_panel, orient=tk.VERTICAL)
        main_panel.add(m2)

        top = tk.Button(m2, text="Windows 1", command=lambda: self.master.show_frame(Home))
        m2.add(top)

        bottom = tk.Button(m2, text="Windows 2", command=lambda: self.master.show_frame(Calculator))
        m2.add(bottom)
        


class Calculator(tk.Frame):
    """the main frame for the Home of the app"""

    def __init__(self, master, controller):

        tk.Frame.__init__(self, master)
        self.master = master
        self.button_list = []
        self.content()
        self.pack()

    def content(self):
        """Add the content of the frame"""

        for i in range(10):
            self.button_list.append(tk.Button(self.master, text=str(i)).pack())
        self.button_list.append(tk.Button(self.master, text="HOME", command= lambda: controller.show_frame(Home)).pack())
        return




a = App()

a.mainloop()
