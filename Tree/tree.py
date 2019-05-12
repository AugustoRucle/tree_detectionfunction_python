# Imports

from tkinter import *
from tkinter import ttk

# CONSTANT

INCREMENT_X = 200
INCREMENT_Y = 150
DIFFERENCE = 75

# Structs

dictionary_cicles = {}

# Functions

def circle (canvas, startX = 10, startY = 10, endX = 80, endY = 80, set_outline='#D9D9D9', set_color = '#737373', width = 2):
    id = canvas.create_oval( startX, startY, endX, endY, 
                                outline = set_outline, 
                                fill = set_color, width = width )

    save_circle(id, startX, startY, endX, endY)

    return id

def text (canvas, x, y, text, font):
    canvas.create_text (x, y, text = text, font = font)

def save_circle (id, startX, startY, endX, endY ):
    dictionary_cicles[id] = { 
        "startX": startX, 
        "startY": startY,
        "endX"  : endX,
        "endY"  : endY
    }

def print_dictionary(dictionary):
    print("Printing dictionary..............\n\n")
    for key, value in enumerate ( dictionary.items() ):
        print(" k: {}, \n  Vs:{} \n".format(key, value))


# Main
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creating Canvas

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))


functions_total = 13

INCREMENT = (functions_total * INCREMENT_X) / 2

idMain =  circle(canvas,  startX= INCREMENT_X + INCREMENT , endX=  ( INCREMENT + INCREMENT_X ) + DIFFERENCE)

later_position = dictionary_cicles[idMain]['startX']
new_position = later_position /  3

id1 = circle(canvas,  
        startY=INCREMENT_Y, endY= INCREMENT_Y + DIFFERENCE, 
        startX= new_position , endX=   new_position + DIFFERENCE)


for i in range(id1, id1+2):
    circle(canvas,  
            startY=INCREMENT_Y, endY= INCREMENT_Y + DIFFERENCE, 
            startX= dictionary_cicles[i]['startX'] + new_position * 2 , endX=   (dictionary_cicles[i]['startX'] + new_position * 2) + DIFFERENCE)

later_position = dictionary_cicles[2]['startX']
new_position = later_position /  10

id5 = circle(canvas,  
        startY=INCREMENT_Y*2, endY= INCREMENT_Y*2 + DIFFERENCE, 
        startX= new_position, endX=    new_position + DIFFERENCE)

for i in range(id5, id5+10):
    circle(canvas,  
            startY=INCREMENT_Y*2, endY= INCREMENT_Y*2 + DIFFERENCE, 
            startX= dictionary_cicles[i]['startX'] + new_position * 2 , endX=   (dictionary_cicles[i]['startX'] + new_position * 2) + DIFFERENCE)

root.mainloop()


