import tkinter as tk
from .structures import Shield, Figure
from .stringfuncs import center_lines

class GeomancyApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.master = master
        self.default_font = 'Courier'
        self.bgcolors = ('red','yellow','blue','green')
        self.cur_throw = 0
        self.figures = [None for m in range(Shield.num_mothers)]

        sample_figure = Figure.quick_throw()
        num_lines = len(str(sample_figure).split('\n'))
        label_width = len(Figure.longest_name)
        self.blank_lines = center_lines('\n' * ( num_lines-1), label_width)

        self.create_widgets()

    def create_widgets(self):
        # Enter the date.
        # Enter your question.
        # Display the mother figures. If not fully thrown, show the blank page or the partial group of figures.
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row = 0)
        self.figure_slots = []
        self.figure_strings = []
        for m in range(Shield.num_mothers):
            cur_stringvar = tk.StringVar(self)
            cur_stringvar.set(self.blank_lines)
            self.figure_strings.append(cur_stringvar)
            cur_label = tk.Label(self.top_frame, textvariable=cur_stringvar, font=self.default_font, bg = self.bgcolors[m])
            self.figure_slots.append(cur_label)
            cur_label.grid(row=0, column=Shield.num_mothers - m)
        # The dice button.
        self.one_throw_button = tk.Button(self, text = 'Throw the dice.', command = self.throw_dice)
        self.one_throw_button.grid(row = 1)
        # The chart button. Become enabled when all four Figure objects have been initiated.
        self.chart_button = tk.Button(self, text = 'Create the chart.', command = self.create_chart, state = tk.DISABLED)
        self.chart_button.grid(row = 2)
        
        self.start_over_button = tk.Button(self, text = 'Start over.', command = self.start_over, state = tk.DISABLED)
        self.start_over_button.grid(row = 3)

        self.chartvar = tk.StringVar()
        self.chart = tk.Label(self, anchor=tk.W, textvariable=self.chartvar, font = self.default_font, state=tk.DISABLED)

    def throw_dice(self):
        fig = Figure.quick_throw()
        cur_throw = self.cur_throw
        self.figures[cur_throw] = fig
        self.figure_slots[cur_throw].config(bg=self.bgcolors[cur_throw])
        centered_str = center_lines(str(fig), len(Figure.longest_name))
        self.figure_strings[cur_throw].set(centered_str)
        self.cur_throw = (self.cur_throw + 1) % Shield.num_mothers
        if all(self.figures):
            self.chart_button.config(state = tk.NORMAL)
        if any(self.figures):
            self.start_over_button.config(state = tk.NORMAL)

    def create_chart(self):
        my_shield = Shield(*self.figures)
        self.chartvar.set(my_shield.text_art())
        self.chart.config(state=tk.NORMAL)
        self.chart.grid(row = 4)

    def start_over(self):
        self.cur_throw = 0
        for i in range(len(self.figures)):
            self.figures[i] = None
        for s in self.figure_strings:
            s.set(self.blank_lines)
        self.chart_button.config(state = tk.DISABLED)
        self.chart.grid_forget()
        self.start_over_button.config(state = tk.DISABLED)
 
def run():
    root = tk.Tk()
    app = GeomancyApplication(master=root)
    root.mainloop()

