from tkinter import *
from tkinter import ttk
import Input
import Output
import os
import pickle


class Driver:

    # Variable
    # List to store information of patients
    patients = []
    # List to store information of pharmacies
    medicines = []
    # List to store information of doctors
    doctors = []
    # List to store information of staffs
    staffs = []
    # List to store information of rooms
    rooms = []
    # List to store information of beds
    beds = []

    nofpatients = None
    nofpharmacies = None
    nofdoctors = None
    nofstaffs = None
    nofrooms = None
    nofbes = None
    

    #Instance variable
    def __init__(self):
        self.input = Input.Input(self)
        self.output = Output.Output(self)


    
    #Function to run the program
    def run_Driver(self):
        #Upon starting the program
        ########



# ============================================================================================
# ================================================Main Window=================================
# ============================================================================================
        # Create the root window
        # with specified size and title
        root = Tk()  
        root.title("Hosptital management program")  
        # root.geometry("1024x768")  

        # Create label for root window
        label1 = Label(root, text = "Welcome to hospital management")
        label2 = Label(root, text= "Image here                     ")
        # ========================================================================
        # ============================Input data Window===========================
        # ========================================================================
        def input_window(self):
            # Create input window
            input_win = Toplevel(root)
            input_win.title("Input Window")
            label11 = Label(input_win, text = "Inpur data here")
            label22 = Label(input_win, text= "Treeview here                     ")
            # #~~~~~~~~~~~~~~~~~~~~~~~~~ Input patients~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            btn_input_patients = Button(input_win, padx= 135, pady= 20, text = 'Patients', command= lambda: self.input.input_patients_window(input_win))
            btn_input_employees = Button(input_win, padx= 126, pady= 20, text = 'Employees', command= lambda: self.input.input_employees_window(input_win))
            btn_input_infrastructure = Button(input_win, padx= 118, pady= 20, text= 'Infrastructure', command= lambda: self.input.input_infrastructure_window(input_win))
            
            # Set position
            btn_input_patients.grid(column=0, row=1)
            btn_input_employees.grid(column=0, row=2)
            btn_input_infrastructure.grid(column=0, row=3)

            label11.grid(column=0, row=0, padx=10, pady= 10)
            label22.grid(column= 1, row= 1, columnspan= 3)
            input_win.mainloop()
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        # Create buttons
        btn_input = Button(root, padx= 130, pady= 20, text = 'Input data', command= lambda: input_window(self))
        btn_upd = Button(root, padx= 123, pady= 20, text = 'Update data', command = '')
        btn_find = Button(root, padx= 132, pady= 20, text = 'Find data', command= '')
        btn_display = Button(root, padx= 122, pady= 20, text = 'Display data', command= '')
        btn_exit = Button(root, padx= 150, pady= 20, text = 'Exit', command= root.destroy)

        # Set position


        btn_input.grid(column=0, row=1)
        btn_upd.grid(column=0, row=2)
        btn_find.grid(column=0, row= 3)
        btn_display.grid(column=0, row= 4)
        btn_exit.grid(column=0, row= 5)

        label1.grid(column=0, row=0, padx=10, pady= 10)
        label2.grid(column= 1, row= 1, columnspan= 3)
        root.mainloop()

        for item in self.patients:
            print(item.get_patname())