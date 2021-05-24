
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

        # self.patients = [Patient(self, "Minh", 18, "Sick", Bed(self, 4, Room(self, "Imergency", 18)))]
        
        # self.rooms = [# Imergency room
        #              Room(self, 'Imergency', 1 , 'Free') ,
        #              Room(self, 'Imergency', 2 , 'Free') ,  
        #              Room(self, 'Imergency', 3 , 'Free') ,
        #              Room(self, 'Imergency', 4 , 'Free') ,
        #              Room(self, 'Imergency', 5 , 'Free') ,
        #              # Rest room
        #              Room(self, 'Rest', 1 , 'Free') ,
        #              Room(self, 'Rest', 2 , 'Free') ,
        #              Room(self, 'Rest', 3 , 'Free') ,
        #              Room(self, 'Rest', 4 , 'Free') ,
        #              Room(self, 'Rest', 5 , 'Free') ,
        #              Room(self, 'Rest', 6 , 'Free') ,
        #              Room(self, 'Rest', 7 , 'Free') ,
        #              Room(self, 'Rest', 8 , 'Free') ,
        #              Room(self, 'Rest', 9 , 'Free') ,
        #              Room(self, 'Rest', 10 , 'Free')  ]
            

        # self.beds = [# Imergency 1
        #             Bed(self, 1 , 'Free', self.rooms[0]),
        #             # Imergency 2
        #             Bed(self, 2 , 'Free', self.rooms[1]),
        #             # Imergency 3
        #             Bed(self, 3 , 'Free', self.rooms[2]),
        #             # Imergency 4
        #             Bed(self, 4 , 'Free', self.rooms[3]),
        #             # Imergency 5
        #             Bed(self, 5 , 'Free', self.rooms[4]),

        #             #Rest 1
        #             Bed(self, 1 , 'Free', self.rooms[5]),
        #             Bed(self, 2 , 'Free', self.rooms[5]),
        #             Bed(self, 3 , 'Free', self.rooms[5]),
        #             Bed(self, 4 , 'Free', self.rooms[5]),
        #             Bed(self, 5 , 'Free', self.rooms[5]),
        #             #Rest 2
        #             Bed(self, 1 , 'Free', self.rooms[6]),
        #             Bed(self, 2 , 'Free', self.rooms[6]),
        #             Bed(self, 3 , 'Free', self.rooms[6]),
        #             Bed(self, 4 , 'Free', self.rooms[6]),
        #             Bed(self, 5 , 'Free', self.rooms[6]),
        #             #Rest 3
        #             Bed(self, 1 , 'Free', self.rooms[7]),
        #             Bed(self, 2 , 'Free', self.rooms[7]),
        #             Bed(self, 3 , 'Free', self.rooms[7]),
        #             Bed(self, 4 , 'Free', self.rooms[7]),
        #             Bed(self, 5 , 'Free', self.rooms[7]),
        #             #Rest 4
        #             Bed(self, 1 , 'Free', self.rooms[8]),
        #             Bed(self, 2 , 'Free', self.rooms[8]),
        #             Bed(self, 3 , 'Free', self.rooms[8]),
        #             Bed(self, 4 , 'Free', self.rooms[8]),
        #             Bed(self, 5 , 'Free', self.rooms[8]),
        #             #Rest 5        
        #             Bed(self, 1 , 'Free', self.rooms[9]),
        #             Bed(self, 2 , 'Free', self.rooms[9]),
        #             Bed(self, 3 , 'Free', self.rooms[9]),
        #             Bed(self, 4 , 'Free', self.rooms[9]),
        #             Bed(self, 5 , 'Free', self.rooms[9]),
        #             #Rest 6
        #             Bed(self, 1 , 'Free', self.rooms[10]),
        #             Bed(self, 2 , 'Free', self.rooms[10]),
        #             Bed(self, 3 , 'Free', self.rooms[10]),
        #             Bed(self, 4 , 'Free', self.rooms[10]),
        #             Bed(self, 5 , 'Free', self.rooms[10]),
        #             #Rest 7
        #             Bed(self, 1 , 'Free', self.rooms[11]),
        #             Bed(self, 2 , 'Free', self.rooms[11]),
        #             Bed(self, 3 , 'Free', self.rooms[11]),
        #             Bed(self, 4 , 'Free', self.rooms[11]),
        #             Bed(self, 5 , 'Free', self.rooms[11]),
        #             #Rest 8
        #             Bed(self, 1 , 'Free', self.rooms[12]),
        #             Bed(self, 2 , 'Free', self.rooms[12]),
        #             Bed(self, 3 , 'Free', self.rooms[12]),
        #             Bed(self, 4 , 'Free', self.rooms[12]),
        #             Bed(self, 5 , 'Free', self.rooms[12]),
        #             #Rest 9
        #             Bed(self, 1 , 'Free', self.rooms[13]),
        #             Bed(self, 2 , 'Free', self.rooms[13]),
        #             Bed(self, 3 , 'Free', self.rooms[13]),
        #             Bed(self, 4 , 'Free', self.rooms[13]),
        #             Bed(self, 5 , 'Free', self.rooms[13]),
        #             #Rest 10
        #             Bed(self, 1 , 'Free', self.rooms[14]),
        #             Bed(self, 2 , 'Free', self.rooms[14]),
        #             Bed(self, 3 , 'Free', self.rooms[14]),
        #             Bed(self, 4 , 'Free', self.rooms[14]),
        #             Bed(self, 5 , 'Free', self.rooms[14]),

        #             ]
    
    #Function to run the program
    def run_Driver(self):
        #Upon starting the program
        ########



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

        btn_bill = Button(root, text= "Bill", width = 20 , height= 4,font=('calibre',15, 'bold'))

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