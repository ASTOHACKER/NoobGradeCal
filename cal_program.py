
import tkinter as tk
def show_output():
    Grade = ["A","B","C","F"]
    number = int(number_input.get())
    output = ''
    if number == 101:
        label = str("Please Select Number 1-100 You number is"),str(number)
    elif number >= 50:
        label = str("You score is = "),str(number)
        if number >= 80:
            output = "You grade",Grade[0]
        elif number >= 70:
            output = "You grade",Grade[1]
        elif number >= 50:
            output = "You grade",Grade[2]
    elif number >= 0:
        label = str("You number is = >"),str(number)
        output = "You grade",Grade[3]
    output_lable.configure(text=output)
    out_label.configure(text=label) 



window = tk.Tk()
window.title()
window.minsize(width=500,height=500)
title_label = tk.Label(master=window,text='Cal Grade')
title_label.pack()

number_input = tk.Entry(master=window)
number_input.pack()

go_button =  tk.Button(master=window, text='Go',command=show_output)
go_button.pack()


out_label = tk.Label(master=window)
out_label.pack()

output_lable = tk.Label(master=window)
output_lable.pack()

window.mainloop()