from tkinter.ttk import *
from tkinter import *
import Win_Patients
import Win_Employees
import Win_Infrastructure
import Win_Bill
# from PIL import ImageTk,Image

class Driver:

    #Instance variable
    def __init__(self):
        self.Win_Patients = Win_Patients.Win_Patients(self)
        self.Win_Employees = Win_Employees.Win_Employees(self)
        self.Win_Infrastructure = Win_Infrastructure.Win_Infrastructure(self)
        self.Win_Bill = Win_Bill.Win_Bill(self)

        
    #Function to run the program
    def run_Driver(self):
# ============================================================================================
# ================================================Main Window=================================
# ============================================================================================
        # Create the root window
        root = Tk()  
        root.title("Hospital management program")

        # Root window size
        root.geometry("1600x900")

        # Root label
        root_label1 = Label(root, text= "Welcome to hospital management", width = 30 ,font=('calibre',20, 'bold'))
        root_label1.pack(pady = 20)

        # # Image
        # hos_image = Image.PhotoImage(Image.open("img1.png"))
        # hos_image = Label(root, imag= hos_image)
        # hos_image.pack(anchor= E)
        hos_image = Label(root, text = "Image here")
        hos_image.pack(padx= 200, pady = 20, anchor= E)


        # # Frame for buttons
        # root = LabelFrame(root, text= '')
        # root.pack(padx = 150, anchor= W)
        # Buttons 
        btn_patient = Button(root, text= "Patient", width = 20 , height= 4,font=('calibre',15, 'bold'), command= lambda: self.Win_Patients.open_patient(root))

        btn_employee = Button(root, text= "Employees", width = 20 , height= 4,font=('calibre',15, 'bold'), command= lambda: self.Win_Employees.open_employees(root))

        btn_infras = Button(root, text= "Infrastructure", width = 20 , height= 4,font=('calibre',15, 'bold'), command= lambda: self.Win_Infrastructure.open_inf(root))

        btn_bill = Button(root, text= "Bill", width = 20 , height= 4,font=('calibre',15, 'bold'), command= lambda: self.Win_Bill.open_bill(root))

        btn_exit = Button(root, text= "Exit", width = 20 , height= 4,font=('calibre',15, 'bold'), command = root.destroy)


        # Set position
        btn_patient.pack(pady= 5)

        btn_employee.pack(pady = 5)

        btn_infras.pack(pady= 5)

        btn_bill.pack(pady = 5)

        btn_exit.pack(pady = 5)

       
        root.mainloop()



d = Driver()
d.run_Driver()