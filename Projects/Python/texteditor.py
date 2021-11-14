#create a text editor

from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
import os, sys
import win32print
import win32api

root = Tk()
root.title('TXT Editor')
root.iconbitmap('../Python/book.ico')
root.geometry("1200x710")

# set variable for filename
global open_status_name
open_status_name = False

# set variable for highlighted
global selected
selected = False

# create new file function
def new_file():
    my_text.delete("1.0", END)
    root.title('New File - TXT Editor')
    status_bar.config(text="New File        ")

    global open_status_name
    open_status_name = False


# open files
def open_file():
    my_text.delete("1.0", END)
    # get filename
    text_file = filedialog.askopenfilename(initialdir="H:/Projects/Python/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    # check if there is a file name, then make it global if there is
    if text_file:
        global open_status_name
        open_status_name = text_file
    # update status bars
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("H:/Projects/Python/", "")
    root.title(f'{name} - TXT Editor')
    # open file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # add file to text box
    my_text.insert(END, stuff)
    # close opened file
    text_file.close()

# save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="H:/Projects/Python/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # update status bars
        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        name = name.replace("H:/Projects/Python/", "")
        root.title(f'{name} - TXT Editor')

        # save file and close
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        messagebox.showinfo("File Status","File Saved!")

# save file
def save_file():
    global open_status_name
    if open_status_name:
      # save file and close
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

        status_bar.config(text=f'Saved: {open_status_name}        ')
        name = open_status_name
        name = name.replace("H:/Projects/Python/", "")
        root.title(f'{name} - TXT Editor')
        messagebox.showinfo("File Status","File Saved!")
    else:
        save_as_file()

# cut text
def cut_text(e):
    global selected
    # check if keyboard shortcut was used
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # grab text then delete and clear/append clipboard
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


# copy text
def copy_text(e):
    global selected
    # check if keyboard shortcut was used
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        # grab selected and clear/append clipboard
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


# paste text
def paste_text(e):
    global selected
    # check if keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

# bold text
def bold_it():
    # create font
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    # define current tags
    current_tags = my_text.tag_names("sel.first")

    # configure tag
    my_text.tag_configure("bold", font=bold_font)

    # check to see if tag has been set
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


# italics
def italics_it():
    # create font
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    # define current tags
    current_tags = my_text.tag_names("sel.first")

    # configure tag
    my_text.tag_configure("italics", font=italics_font)

    # check to see if tag has been set
    if "italics" in current_tags:
        my_text.tag_remove("italics", "sel.first", "sel.last")
    else:
        my_text.tag_add("italics", "sel.first", "sel.last")

# change selected text color
def text_color():
    # pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        color_font = font.Font(my_text, my_text.cget("font"))
    

        # define current tags
        current_tags = my_text.tag_names("sel.first")

        # configure tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)

        # check to see if tag has been set
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")

# change bg color
def bg_color():
    # pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

# change all text color
def all_text_color():
    # pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)

# print file
def print_file():
    file_to_print = filedialog.askopenfilename(initialdir="H:/Projects/Python/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    
    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)


# select all text
def select_all(e):
    # add sel tag
    my_text.tag_add('sel', '1.0', 'end')


# clear all text
def clear_all():
    my_text.delete(1.0, END)

# night mode on
def night_on():
    main_color = "#000000"
    second_color = "#373737"
    text_color = "green"

    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg=text_color)
    my_text.config(bg=second_color)
    toolbar_frame.config(bg=main_color)
    # toolbar buttons
    bold_button.config(bg=second_color)
    italics_button.config(bg=second_color)
    redo_button.config(bg=second_color)
    undo_button.config(bg=second_color)
    color_text_button.config(bg=second_color)
    # file menu colors
    file_menu.config(bg= main_color, fg=text_color)
    edit_menu.config(bg= main_color, fg=text_color)
    color_menu.config(bg= main_color, fg=text_color)
    options_menu.config(bg= main_color, fg=text_color)

#night mode off
def night_off():
    main_color = "SystemButtonFace"
    second_color = "SystemButtonFace"
    text_color = "black"

    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg=text_color)
    my_text.config(bg=second_color)
    toolbar_frame.config(bg=main_color)
    # toolbar buttons
    bold_button.config(bg=second_color)
    italics_button.config(bg=second_color)
    redo_button.config(bg=second_color)
    undo_button.config(bg=second_color)
    color_text_button.config(bg=second_color)
    # file menu colors
    file_menu.config(bg= main_color, fg=text_color)
    edit_menu.config(bg= main_color, fg=text_color)
    color_menu.config(bg= main_color, fg=text_color)
    options_menu.config(bg= main_color, fg=text_color)


# create toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# create vertical scrollbar for text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side= RIGHT, fill=Y)

# create horizontal scrollbar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# create text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

# configure scroll bar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# add edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command= lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command= lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste",command= lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: select_all(False), accelerator="(Ctrl+a)")
edit_menu.add_command(label="Clear", command=clear_all, )


# add color menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# add options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Night Mode On", command= night_on)
options_menu.add_command(label="Night Mode Off", command= night_off)

# add status bar
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15) 

# edit bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-a>', select_all)
root.bind('<Control-A>', select_all)

# buttons
# bold
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# italics
italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5, pady=5)
# undo
undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5, pady=5)
# redo 
redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5, pady=5)
# text color 
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)


root.mainloop()