from tkinter import *
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.ttk import Combobox
import os
from fetch0 import *
from decode1 import *
from execute0 import *
from driver_step import myFunc
from memoryaccess1 import *
from registerupdate1 import *
import linecache
import globalss
from error_handling import *
from converttomachinecode1 import *

registers = {}  # register dictionary
memory = {}  # memory
if __name__ == '__main__':
    for i in range(32):
        registers[i] = 0

    window = Tk()
    window.title('RISC-V Simulator')
    var1 = StringVar()
    l = Label(window, bg='green', fg='yellow', font=('Arial', 20), width=60, text="RISC-V Editor & Simulator").grid(
        row=0,
        columnspan=13,
        pady=7)

    index = 1


    def step():
        return


    def run():
        myFunc()
        for i in range(32):
            registers[i] = globalss.register[i]
            print(registers[i])
            field[i].delete(0, END)
            field[i].insert(0, str(registers[i]))
        for i in range(64):
            field2[i].delete(0, END)
            field2[i].insert(0, str(globalss.memory_array[i]))

        messagebox.showinfo("Success",
                            "Code compilation successful. Machine code has been saved in machinecode.txt. Use the "
                            "editor to open it.")


    def dump():
        file = open("store.txt", 'w')
        file.write("Register Values:\n")
        for i in range(32):
            str1 = "x" + str(i) + ": " + str(registers[i]) + "\n"
            file.write(str1)
        file.write("Stack Values Values:\n")
        for i in range(1000):
            str1 = str(1000 - i) + ": " + str(globalss.stack_array[i]) + "\n"
            file.write(str1)
        for i in range(1000):
            str1 = str(hex(268435456 + i)) + ": " + str(globalss.memory_array[i]) + "\n"
            file.write(str1)
        messagebox.showinfo("Success",
                            "Execution terminated, all reg, stack and memory values stored in store.txt")
        window.after(3500, lambda: window.destroy())


    def openfile():
        # file = filedialog.askopenfile(parent=window, title="Select a file",
        #     filetypes=(("ASM file", "*.asm"), ("All Files", "*.*")))
        file = open('assembly.txt', 'w')
        data = textArea.get('1.0', 'end' + '-1c')
        file.write(data)
        file.close()
        file = open('assembly.txt', 'r')
        if file is not None:
            contents = file.read().splitlines()
            for line in contents:
                lb.insert('end', line)

            file.close()


    def repSelect(event):
        if w.current() == 0:
            for i in range(32):
                field[i].delete(0, END)
                field[i].insert(0, str(registers[i]))
            for i in range(64):
                field2[i].delete(0, END)
                field2[i].insert(0, str(globalss.memory_array[i]))

        if w.current() == 1:
            for i in range(32):
                field[i].delete(0, END)
                field[i].insert(0, str(chr(registers[i])))
            for i in range(64):
                field2[i].delete(0, END)
                field2[i].insert(0, str(chr(globalss.memory_array[i])))

        if w.current() == 2:
            for i in range(32):
                field[i].delete(0, END)
                field[i].insert(0, str(bin(registers[i])))
            for i in range(64):
                field2[i].delete(0, END)
                field2[i].insert(0, str(bin(globalss.memory_array[i])))

        if w.current() == 3:
            for i in range(32):
                field[i].delete(0, END)
                field[i].insert(0, str(hex(registers[i])))
            for i in range(64):
                field2[i].delete(0, END)
                field2[i].insert(0, str(hex(globalss.memory_array[i])))


    def jumpSelect(event):
        if z.current() == 0:
            for i in range(16):
                # label2[i] = Label(window, text=str(hex(268435456 + i * 4)))
                label2[i].config(text=str(hex(268435456 + i * 4)))
                # label2[i].grid(row=4 + i, column=2+6, padx=1, pady=0, sticky=E)
            for i in range(64):
                field2[i].delete(0, END)
                field2[i].insert(0, str(globalss.memory_array[i]))

        if z.current() == 1:
            for i in range(16):
                # label2[i] = Label(window, text=str(1000 - i * 4))
                # label2[i].grid(row=4 + i, column=2+6, padx=1, pady=0, sticky=E)
                label2[i].config(text=str(1000 - i * 4))
            for i in range(64):
                field2[i].delete(0, END)
                field2[i].insert(0, str(globalss.stack_array[1000 - i]))


    b1 = Button(window, text='Step', width=10, height=2, command=step)
    b1.grid(row=1, column=1, padx=2, pady=7)
    b2 = Button(window, text="Run", width=10, height=2, command=run)
    b2.grid(row=1, column=3, padx=2, pady=7)
    b3 = Button(window, text="Dump", width=10, height=2, command=dump)
    b3.grid(row=1, column=4, padx=2, pady=7)
    b4 = Button(window, text="Simulate", width=10, height=2, command=openfile)
    b4.grid(row=1, column=0, padx=2, pady=7)
    b5 = Button(window, text="Previous", width=10, height=2)
    b5.grid(row=1, column=2, pady=7)
    var2 = StringVar()
    var2.set((1, 2, 3, 4))

    textArea = scrolledtext.ScrolledText(window, height=40, width=30, padx=2)
    textArea.grid(row=2, column=0, rowspan=20, columnspan=2)
    scrollbar = Scrollbar(window)
    lb = Listbox(window, height=40, width=30)
    lb.grid(row=2, column=2 + 0, rowspan=20, columnspan=2, padx=5, pady=10)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)

    # lb.pack()
    label = [Label()] * 32
    field = [Entry()] * 32
    l2 = Label(window, text="Register Values")
    l2.grid(row=2, column=2 + 2, columnspan=2, sticky=W + E, padx=10)
    l3 = Label(window, text="Memory Values")
    l3.grid(row=2, column=2 + 6, columnspan=2, padx=10)
    for i in range(32):
        if i < 16:
            label[i] = Label(window, text="x" + str(i), width=5)
            label[i].grid(row=4 + i, column=2 + 2, padx=1, pady=0, sticky=E)
            field[i] = Entry(window)
            field[i].grid(row=4 + i, column=2 + 3, padx=1, pady=0)
        else:
            label[i] = Label(window, text="x" + str(i), width=5)
            label[i].grid(row=4 + i - 16, column=2 + 4, padx=1, pady=0, sticky=E)
            field[i] = Entry(window)
            field[i].grid(row=4 + i - 16, column=2 + 5, padx=10, pady=0)
        # label[i].pack()
        # field[i].pack()
        label2 = [Label()] * 16
        field2 = [Entry()] * 64
        memlab0 = Label(window, text="0")
        memlab0.grid(row=3, column=2 + 7)
        memlab1 = Label(window, text="1")
        memlab1.grid(row=3, column=2 + 8)
        memlab2 = Label(window, text="2")
        memlab2.grid(row=3, column=2 + 9)
        memlab3 = Label(window, text="3")
        memlab3.grid(row=3, column=2 + 10)
    for i in range(16):
        label2[i] = Label(window, text=str(hex(268435456 + i * 4)))
        label2[i].grid(row=4 + i, column=2 + 6, padx=1, pady=0, sticky=E)
        field2[4 * i] = Entry(window)
        field2[4 * i].grid(row=4 + i, column=2 + 7, padx=2, pady=0)
        field2[4 * i + 1] = Entry(window)
        field2[4 * i + 1].grid(row=4 + i, column=2 + 8, padx=2, pady=0)
        field2[4 * i + 2] = Entry(window)
        field2[4 * i + 2].grid(row=4 + i, column=2 + 9, padx=2, pady=0)
        field2[4 * i + 3] = Entry(window)
        field2[4 * i + 3].grid(row=4 + i, column=2 + 10, padx=2, pady=0)

    choices = ['Decimal', 'ASCII', 'Binary', 'Hexadecimal']
    variable = StringVar(window)
    variable.set('Decimal')

    w = Combobox(window, values=choices, state="readonly")
    w.grid(row=20, column=2 + 3)
    w.current(0)
    w.bind("<<ComboboxSelected>>", repSelect)
    repChoiceLabel = Label(window, text="Choose base:").grid(row=20, column=2 + 2)
    stackMemChoicLabel = Label(window, text="Jump To:").grid(row=20, column=2 + 6)
    z = Combobox(window, values=["memory", "stack"], state="readonly")
    z.grid(row=20, column=2 + 7)
    z.current(0)
    z.bind("<<ComboboxSelected>>", jumpSelect)
    window.mainloop()
