from tkinter import *
import re

class Main:

    def __init__(self):
        self.registers = [0, 0, 0, 0, 0, 0]
        self.file_lines = []

    def run_button_action(self):
        """"""
        self.load_file("../resources/src.txt")

    def run_single_line_button_action(self):
        """"""

    def load_file(self, path):
        f = open(path, "r")
        self.file_lines = []
        for x in f:
            self.file_lines.append(re.sub("//.*$", "", re.sub("^.*:", "", x.replace(" ", ""))))

if __name__ == '__main__':
    main = Main()

    # canvas width, canvas height
    canvasConfig = [500, 300]

    window = Tk()
    window.title("SPOZ-I-Interpreter")

    # Label and Buttons
    run_button = Button(window, text="run file", command=main.run_button_action)
    run_single_line_button = Button(window, text="run single line", command=main.run_single_line_button_action)

    line_input_field = Entry(window, bd=5, width=5)

    reg_1_input_field = Entry(window, bd=5, width=3)
    reg_2_input_field = Entry(window, bd=5, width=3)
    reg_3_input_field = Entry(window, bd=5, width=3)
    reg_4_input_field = Entry(window, bd=5, width=3)
    reg_5_input_field = Entry(window, bd=5, width=3)
    reg_6_input_field = Entry(window, bd=5, width=3)

    reg_1_label = Label(window, text="1:")
    reg_2_label = Label(window, text="1:")
    reg_3_label = Label(window, text="1:")
    reg_4_label = Label(window, text="1:")
    reg_5_label = Label(window, text="1:")
    reg_6_label = Label(window, text="1:")

    path_label = Label(window, text="Pfad:")
    path_input_field = Entry(window, bd=5, width=40)

    # add elements
    run_button.grid(row=0, column=1)
    run_single_line_button.grid(row=1, column=1)

    line_input_field.grid(row=1, column=0)

    reg_1_input_field.grid(row=4, column=3)
    reg_2_input_field.grid(row=5, column=3)
    reg_3_input_field.grid(row=6, column=3)
    reg_4_input_field.grid(row=7, column=3)
    reg_5_input_field.grid(row=8, column=3)
    reg_6_input_field.grid(row=9, column=3)

    reg_1_label.grid(row=4, column=2)
    reg_2_label.grid(row=5, column=2)
    reg_3_label.grid(row=6, column=2)
    reg_4_label.grid(row=7, column=2)
    reg_5_label.grid(row=8, column=2)
    reg_6_label.grid(row=9, column=2)

    path_label.grid(row=10, column=0)
    path_input_field.grid(row=10, column=1)

    window.mainloop()
