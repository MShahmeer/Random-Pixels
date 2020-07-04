from random import randint
from tkinter import *
from PIL import ImageTk, Image

WIDTH = 500
HEIGHT = 500


def create_rgb_triplet():
    out = ""
    for j in range(3):
        val = randint(0, 255)
        if val < 10:
            out += "  " + str(val)
        elif val < 100:
            out += " " + str(val)
        else:
            out += str(val)
        if j != 2:
            out += " "
    return out


f = open("image.ppm", "w+")

f.write("P3\n")
f.write(str(WIDTH) + " " + str(HEIGHT) + "\n")
f.write("255" + "\n")

for _ in range(HEIGHT):
    for i in range(WIDTH):
        f.write(create_rgb_triplet())
        if i != WIDTH - 1:
            f.write("  ")
    f.write("\n")

f.close()

root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
img = ImageTk.PhotoImage(image=Image.open("image.ppm"))
canvas.create_image(WIDTH, HEIGHT, anchor=CENTER, image=img)
mainloop()
