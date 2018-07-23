import tkinter as tk
from structures import Shield

class GeomancyApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Enter the date.
        # Enter your question.
        # Throw dice button.
        # Display for the chart.
        pass

    def draw_chart(self):
        my_shield = Shield.quick_cast()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "hellow Word\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                             command=root.destroy)
        self.quit.pack(side="bottom")
    
    def say_hi(self):
        print("hi there, everyone!")


class PhoneApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        print(self.grid_size())
    
    def create_widgets(self):
        dial_keys = []
        dial_keys.append([1,2,3])
        dial_keys.append([4,5,6])
        dial_keys.append([7,8,9])
        dial_keys.append(["*",0,"#"])
        self.buttons = {}
        cur_column = 0
        cur_row = 0
        for row in dial_keys:
            for k in row:
                ks = str(k)
                self.buttons[ks] = tk.Button(self, text=ks,
                                           command=self.print_val(ks))
                self.buttons[ks].grid(row=cur_row, column=cur_column)
                cur_column += 1
            cur_column = 0
            cur_row += 1

    def print_val(self, val):
        return lambda: print(val)
            
root = tk.Tk()
app_choice = {'ph':PhoneApp, 'app':Application}
app = app_choice['ph'](master=root)
root.mainloop()

