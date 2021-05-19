from domains.Bed import *
from domains.Doctor import *
from domains.Patient import *
from domains.Pharmacy import *
from domains.Room import *
from domains.Staff import *

from tkinter import *
from tkinter import ttk

class Input:
    def __init__(self, driver):
        self.driver = driver

    # Function to input information of patients
    def input_patients_window(self, input_win):
        # Create input patients window
        input_pat_win = Toplevel(input_win)
        # Input variable
        name_var = StringVar()
        age_var = IntVar()
        status_var = StringVar()
        ill_var = StringVar()

        # Create buttons
        def submit():
            name = name_var.get()
            age = age_var.get()
            status = status_var.get()
            ill = ill_var.get()

        sub_btn = Button(input_pat_win, text = 'Submit', command= submit)

        sub_btn.grid()
        input_pat_win.mainloop()

        
    