from tkinter import *
import re

class Main:

    def __init__(self):
        self.registers = [0, 0, 0, 0, 0, 0]
        self.file_lines = []
        self.current_line = 1

    def run_button_action(self):
        """executes entire file. updates registers afterwards"""
        self.load_inputs("../resources/" + path_input_field.get())
        while True:
            self.run_line()

    def run_single_line_button_action(self):
        """"""
        self.load_inputs("../resources/" + path_input_field.get())
        self.run_line()

    def run_line(self):
        if self.current_line >= len(self.file_lines):
            return
        self.calculate_line(self.file_lines[self.current_line - 1])
        self.update_gui()

    def calculate_line(self, line):
        params = line.split(",")
        is_reg = re.compile("^\$.*")
        for i in range(len(params)):
            if i == 2:
                continue
            if is_reg.match(params[i]):
                params[i] = self.registers[int(params[i][1])]
                continue
            params[i] = int(params[i])
        params[2] = int(params[2].replace("$", ""))

        self.registers[params[2]-1] = params[0] - params[1]
        self.current_line = int(params[3])

    def load_file(self, path):
        f = open(path, "r")
        self.file_lines = []
        for x in f:
            self.file_lines.append(re.sub("//.*$", "", re.sub("^.*:", "", x.replace(" ", "").replace('\n', ""))))

    def load_inputs(self, path):
        self.load_file(path)
        self.current_line = int(line_input_field.get())
        self.registers[0] = int(reg_1_input_field.get())
        self.registers[1] = int(reg_2_input_field.get())
        self.registers[2] = int(reg_3_input_field.get())
        self.registers[3] = int(reg_4_input_field.get())
        self.registers[4] = int(reg_5_input_field.get())
        self.registers[5] = int(reg_6_input_field.get())

    def update_gui(self):
        line_input_field.delete(0, 'end')
        line_input_field.insert(0, self.current_line)

        reg_1_input_field.delete(0, 'end')
        reg_1_input_field.insert(0, self.registers[0])
        reg_2_input_field.delete(0, 'end')
        reg_2_input_field.insert(0, self.registers[1])
        reg_3_input_field.delete(0, 'end')
        reg_3_input_field.insert(0, self.registers[2])
        reg_4_input_field.delete(0, 'end')
        reg_4_input_field.insert(0, self.registers[3])
        reg_5_input_field.delete(0, 'end')
        reg_5_input_field.insert(0, self.registers[4])
        reg_6_input_field.delete(0, 'end')
        reg_6_input_field.insert(0, self.registers[5])

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
    line_input_field.insert(0, "1")

    reg_1_input_field = Entry(window, bd=5, width=3)
    reg_1_input_field.insert(0, "0")
    reg_2_input_field = Entry(window, bd=5, width=3)
    reg_2_input_field.insert(0, "0")
    reg_3_input_field = Entry(window, bd=5, width=3)
    reg_3_input_field.insert(0, "0")
    reg_4_input_field = Entry(window, bd=5, width=3)
    reg_4_input_field.insert(0, "0")
    reg_5_input_field = Entry(window, bd=5, width=3)
    reg_5_input_field.insert(0, "0")
    reg_6_input_field = Entry(window, bd=5, width=3)
    reg_6_input_field.insert(0, "0")

    reg_1_label = Label(window, text="1:")
    reg_2_label = Label(window, text="2:")
    reg_3_label = Label(window, text="3:")
    reg_4_label = Label(window, text="4:")
    reg_5_label = Label(window, text="5:")
    reg_6_label = Label(window, text="6:")

    path_label = Label(window, text="Pfad:")
    path_input_field = Entry(window, bd=5, width=40)
    path_input_field.insert(0, "src.txt")

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
