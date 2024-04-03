from tkinter import *
from PIL import Image, ImageDraw
from random import randint
from tkinter import colorchooser, messagebox

def draw(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=color, width=0)
    draw_img.ellipse((x1, y1, x2, y2), fill=color, width=0)

def chooseColor():
    global color
    (rgb, hx) = colorchooser.askcolor()
    color = hx
    color_lab['bg'] = hx

def select(value):
    global brush_size
    brush_size = int(value)

def popup(event):
    global x, y 
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

def rectangle():
    canvas.create_rectangle(x, y, x + 2*brush_size, y + brush_size, fill=color, width=0)
    draw_img.rectangle((x, y, x + 2*brush_size, y, x + 2*brush_size, y + brush_size, x, y + brush_size), fill=color)

def circle():
    canvas.create_oval(x, y, x + brush_size, y + brush_size, fill=color, width=0)  
    draw_img.ellipse((x, y, x + brush_size, y + brush_size), fill=color) 

x = 0
y = 0

root = Tk()
root.title('Paint')
root.geometry('1280x720')
root.resizable(0, 0)

brush_size = 10
color = 'black'

root.columnconfigure(6, weight=1)
root.rowconfigure(2, weight=1)

canvas = Canvas(root, bg='white')
canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)

canvas.bind('<B1-Motion>', draw)
canvas.bind('<Button-3>', popup)

menu = Menu(tearoff=0)
menu.add_command(label="Rectangle", command=rectangle)
menu.add_command(label="Circle", command=circle)
image1 = Image.new('RGB', (1280, 640), 'white')
draw_img = ImageDraw.Draw(image1)

Label(root, text='Settings: ').grid(row=0, column=0, padx=6)

Button(root, text='Choose color', width=11, command=chooseColor).grid(row=0, column=1, padx=6)

color_lab = Label(root, bg=color, width=10)
color_lab.grid(row=0, column=2, padx=6)

Label(root, text='Actions: ').grid(row=1, column=0, padx=6)

root.mainloop()
