from tkinter import *
root = Tk()

root.wm_attributes('-fullscreen','true')
root.configure(background='black')

def quitApp():
    root.destroy()

button = Button(text = 'QUIT', command = quitApp).pack(side = TOP, anchor = NE)

frame = Frame(root, bg = "grey", width = 600).pack(side = LEFT, fill = Y, padx = 10, pady = 10)

root.mainloop()
