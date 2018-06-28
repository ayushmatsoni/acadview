my_dict = {'name':'AYUSHMAT', 'phno':"9882540059 "}
#print(my_dict['name'])
#print(my_dict.get('phno'))

from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
#name_text_box=""
#ph_text_box=""
def cmd():
    root = Tk()
    root.title("Average Speed Checker")
    root.geometry("450x165")
    name_label = Label(root, text="NEW NAME")
    name_label.pack()

    name_text_box =(Entry(root, bd=1))
    name_text_box.pack()

    ph_label = Label(root, text="NEW PHONE NUMBER")
    ph_label.pack()

    ph_text_box =(Entry(root, bd=1))
    ph_text_box.pack()

    def add_new():
        name=name_text_box.get()
        print(name)
        phn=ph_text_box.get()
        print(phn)
        my_dict = {'name': name, 'phno':phn}
        label1 = Label(root, text="You have entered the information to the dictionary")
        label1.pack()

    enter_button = Button(root, text="Enter", command=add_new)
    enter_button.pack()
    root.mainloop()
print("\n")
print(my_dict['name'])
print(my_dict.get('phno'))





master = Tk()
master.title("GUI Asignment 2")
master.geometry("600x500")
scrollbar = Scrollbar(master)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(master, yscrollcommand = scrollbar.set)
mylist.insert(END, "NAME- "+ my_dict['name'])
mylist.insert(END, "PHONENO- " + str(my_dict['phno']))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

lb=Label(master,text="GUI2")
lb.pack()


import tkinter as tk
frame = tk.Frame(master)
frame.pack()
slogan = tk.Button(frame,text="Enter New Details",bg='blue',fg='black',command=cmd)
slogan.pack(side=tk.LEFT)

button = tk.Button(frame,text="QUIT",fg="red",bg='black',command=quit)
button.pack(side=tk.LEFT)
mainloop()