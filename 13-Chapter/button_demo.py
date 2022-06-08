# This program demonstrates a button widget
# and dialog box

import tkinter
import tkinter.messagebox

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create a button widget
        self.my_button = tkinter.Button(self.main_window,
                                        text='Click Me!',
                                        command=self.do_something)

        # Create a Quit button
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the button
        self.my_button.pack()
        self.quit_button.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The do_something method is a callback function
    # for the Button widget.

    def do_something(self):
        # Display an info dialog box
        tkinter.messagebox.showinfo('Response',
                                    'Thanks for clicking the button.')

my_gui = MyGUI()
