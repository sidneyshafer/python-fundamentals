# This program draws a rectangle on a Canvas

import tkinter

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create the Canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Draw a rectangle
        self.canvas.create_rectangle(20, 20, 180, 180, fill='red', width=2)

        # Pack the canvas
        self.canvas.pack()

        # Start the mainloop
        tkinter.mainloop()

# Create an instance
my_gui = MyGUI()
