
from domains.Bed import *
from domains.Doctor import *
from domains.Patient import *
from domains.Medicine import *
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
        input_pat_win.title("Input patients window")
        label_pat = Label(input_pat_win, text= "Patients",  font=('calibre',10, 'bold'))
        label_treeview = Label(input_pat_win, text="Treeviewhere")

        # Input variable
        name_pat_var = StringVar()
        age_pat_var = IntVar()
        ill_pat_var = StringVar()
        roomname_pat_var = StringVar()
        roomid_pat_var = IntVar()
        bedid_pat_var = IntVar()
    
        # Patients - Buttons
        # Name
        name_pat_label = Label(input_pat_win, text = 'Name', font=('calibre',10, 'bold'))
        name_pat_entry = Entry(input_pat_win, width = 27, textvariable= name_pat_var, font=('calibre',10,'normal'))

        # Age
        age_pat_label = Label(input_pat_win, text = 'Age', font=('calibre',10, 'bold'))
        age_pat_entry = Entry(input_pat_win, width = 27, textvariable= age_pat_var, font=('calibre',10,'normal'))

        # Ill
        ill_pat_label = Label(input_pat_win, text = 'Ill', font=('calibre',10, 'bold'))
        ill_pat_entry = Entry(input_pat_win, width = 27, textvariable= ill_pat_var, font=('calibre',10,'normal'))

        # Roomname
        roomname_pat_label = Label(input_pat_win, text = 'Roomname', font=('calibre',10, 'bold'))
        roomname_pat_entry = ttk.Combobox(input_pat_win, width = 25, textvariable= roomname_pat_var)
        roomname_pat_entry['values'] = ('Rest room', 'Imergency room')
        roomname_pat_entry.current(0)

        # Roomid
        roomid_pat_label = Label(input_pat_win, text = 'Roomid', font=('calibre',10, 'bold'))
        roomid_pat_entry = ttk.Combobox(input_pat_win, width = 25, textvariable= roomid_pat_var)
        roomid_pat_entry['values'] = (list(range(1,51)))
        roomid_pat_entry.current(0)

        # Bedid
        bedid_pat_label = Label(input_pat_win, text = 'Bedid', font=('calibre',10, 'bold'))
        bedid_pat_entry = ttk.Combobox(input_pat_win, width = 25, textvariable= bedid_pat_var)
        bedid_pat_entry['values'] = (list(range(1,11)))
        bedid_pat_entry.current(0)

        # Submit function
        def submit_pat(self, driver):
            name = name_pat_var.get()
            age = age_pat_var.get()
            ill = ill_pat_var.get()
            roomname = roomname_pat_var.get()
            roomid = roomid_pat_var.get()
            bedid = bedid_pat_var.get()

 
            self.driver.patients.append(Patient(driver, name, age, ill, Bed(driver, bedid, bstatus, Room(driver, roomname, roomid))))

            # Clean entry
            name_pat_entry.delete(0, END)
            age_pat_entry.delete(0, END)
            ill_pat_entry.delete(0, END)
            roomname_pat_entry.delete(0, END)
            roomid_pat_entry.delete(0, END)
            bedid_pat_entry.delete(0, END)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!! Treeview here !!!!!!!!!!!!!!!!!!!!!!!!!!
        sub_btn = Button(input_pat_win, text = 'Submit', command= lambda: submit_pat(self, self.driver))

        label_pat.grid(row= 0, column= 1)
        label_treeview.grid(row= 1, column=2)

        name_pat_label.grid(row=1, column=0)
        name_pat_entry.grid(row=1, column=1)

        age_pat_label.grid(row=2, column=0)
        age_pat_entry.grid(row=2, column=1)

        ill_pat_label.grid(row=3, column=0)
        ill_pat_entry.grid(row=3, column=1)

        roomname_pat_label.grid(row=5, column=0)
        roomname_pat_entry.grid(row=5,  column= 1)

        roomid_pat_label.grid(row=6, column=0)
        roomid_pat_entry.grid(row=6, column=1)

        bedid_pat_label.grid(row=7, column=0)
        bedid_pat_entry.grid(row=7, column=1)


        sub_btn.grid(row=8, column=1)
        input_pat_win.mainloop()


    # Function to input employees(doctors - staffs)
    def input_employees_window(self, input_win):
        # Create input doctor window
        input_employees_win = Toplevel(input_win)
        input_employees_win.title("Input employees window")
        

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Input doctors~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_doc_1 = Label(input_employees_win, text = "Doctor", font=('calibre',10, 'bold'))
        label_doc_2 = Label(input_employees_win, text= "Treeview doctor here                     ")
        
        # Input doctor variable
        doc_name_var = StringVar()
        doc_age_var = IntVar()
        doc_major_var = StringVar()

        # Doctors - Buttons
        # Name
        name_doc_label = Label(input_employees_win, text = 'Name', font=('calibre',10, 'bold'))
        name_doc_entry = Entry(input_employees_win, width = 27, textvariable= doc_name_var, font=('calibre',10,'normal'))

        # Age
        age_doc_label = Label(input_employees_win, text = 'Age', font=('calibre',10, 'bold'))
        age_doc_entry = Entry(input_employees_win, width = 27, textvariable= doc_age_var, font=('calibre',10,'normal'))

        # Major
        doc_major_label = Label(input_employees_win, text = "Major", font=('calibre',10, 'bold'))
        doc_major_entry = Entry(input_employees_win, width = 27, textvariable= doc_major_var, font=('calibre',10,'normal'))

        sub_doc_btn = Button(input_employees_win, text = 'Submit', command= lambda: submit_doc(self, self.driver))

        # Doctors submit
        def submit_doc(self, driver):
            doc_name = doc_name_var.get()
            doc_age = doc_age_var.get()
            doc_major = doc_major_var.get()

            self.driver.doctors.append(Doctor(driver, doc_name, doc_age, doc_major))
            name_doc_entry.delete(0, END)
            age_doc_entry.delete(0, END)
            doc_major_entry.delete(0, END)

        # Set position for doctors
        label_doc_1.grid(column=1, row=0)
        label_doc_2.grid(column= 2, row= 1)

        name_doc_label.grid(column=0, row=1)
        name_doc_entry.grid(column=1, row=1)

        age_doc_label.grid(column=0, row=2)
        age_doc_entry.grid(column=1, row=2)

        doc_major_label.grid(column=0, row=3)
        doc_major_entry.grid(column=1, row=3)

        sub_doc_btn.grid(row=4, column=1)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Space label
        label_space1 = Label(input_employees_win, text= "               ")
        label_space1.grid(row=5 , column= 0)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Input Staffs ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_staff_1 = Label(input_employees_win, text = "Staff", font=('calibre',10, 'bold'))
        label_staff_2 = Label(input_employees_win, text= "Treeview Staff here                     ")
        
        # Input staff variable
        staff_name_var = StringVar()
        staff_work_var = StringVar()

        # Staffs submit
        def submit_staff(self, driver):
            staff_name = staff_name_var.get()
            staff_work = staff_work_var.get()

            self.driver.staffs.append(Staff(driver, staff_name, staff_work))

            # Clean entry
            staff_name_entry.delete(0, END)
            staff_work_entry.delete(0, END)

        # Staffs - Buttons
        # Name
        staff_name_label = Label(input_employees_win, text = 'Name', font=('calibre',10, 'bold'))
        staff_name_entry = Entry(input_employees_win, width = 27, textvariable= staff_name_var, font=('calibre',10,'normal'))

        # Major
        staff_work_label = Label(input_employees_win, text = "Major", font=('calibre',10, 'bold'))
        staff_work_entry = Entry(input_employees_win, width = 27, textvariable= staff_work_var, font=('calibre',10,'normal'))

        sub_staff_btn = Button(input_employees_win, text = 'Submit', command= lambda: submit_staff(self, self.driver))
        # Set position for staffs

        label_staff_1.grid(row=6, column=1)
        label_staff_2.grid(row=6, column=2)

        staff_name_label.grid(row = 7, column=0)
        staff_name_entry.grid(row = 7, column = 1)

        staff_work_label.grid(row = 8, column= 0)
        staff_work_entry.grid(row = 8, column= 1)

        sub_staff_btn.grid(row = 9, column=1)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Space label
        label_space2 = Label(input_employees_win, text= "               ")
        label_space2.grid(row=10 , column= 0)
        input_employees_win.mainloop()





    # Function to input infrastructure(Bed - Room - Pharmacy)
    def input_infrastructure_window(self, input_win):
        # Create input doctor window
        input_inf_win = Toplevel(input_win)
        input_inf_win.title("Input infrastructure")
        
        # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Input Room~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # label_room_1 = Label(input_inf_win, text = "Doctor", font=('calibre',10, 'bold'))
        # label_room_2 = Label(input_inf_win, text= "Treeview room here                     ")
        
        # # Input room variable
        
        # # Room submit

        # # Room buttons

        
        # # Set position for room

        
        # label_room_1.grid(column=0, row=1)
        # label_room_2.grid(column= 1, row= 1)
        
        # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # # Space
        # label_space1 = Label(input_inf_win, text = '                          ')
        # label_space1.grid()

        # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Input Bed~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # label_bed_1 = Label(input_inf_win, text = "Bed", font=('calibre',10, 'bold'))
        # label_bed_2 = Label(input_inf_win, text= "Treeview bed here                     ")

        # # Input bed variable

        # # Bed submit

        # # Bed buttons

        # # Set position for bed

        # label_bed_1.grid(column=0, row=1)
        # label_bed_2.grid(column= 1, row= 1)

        # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # # Space
        # label_space2 = Label(input_inf_win, text = '                          ')
        # label_space2.grid()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Input Medicine~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_med_1 = Label(input_inf_win, text = "Medicine", font=('calibre',10, 'bold'))
        label_med_2 = Label(input_inf_win, text= "Treeview medicine here                     ")

        # Input medicine variable
        med_name_var = StringVar()
        med_quantity_var = IntVar()

        # Medicine submit
        def med_submit(self, driver):
            med_name = med_name_var.get()
            med_quantity = med_quantity_var.get()

            self.driver.medicines.append(Medicine(driver, med_name, med_quantity))

            # Clean entry
            med_name_entry.delete(0, END)
            med_quantity_entry.delete(0, END)
            
        # Medicine buttons
        # Name
        med_name_label = Label(input_inf_win, text = 'Name', font=('calibre',10, 'bold'))
        med_name_entry = Entry(input_inf_win, width = 27, textvariable= med_name_var, font=('calibre',10,'normal'))

        # Quantity
        med_quantity_label = Label(input_inf_win, text = "Quantity", font=('calibre',10, 'bold'))
        med_quantity_entry = Entry(input_inf_win, width = 27, textvariable= med_quantity_var, font=('calibre',10,'normal'))

        med_sub_btn = Button(input_inf_win, text = 'Submit', command= lambda: med_submit(self, self.driver))

        # Set position for medicine
        label_med_1.grid(row = 0, column= 1)
        label_med_2.grid(row=1, column=2)

        med_name_label.grid(row= 1, column= 0)
        med_name_entry.grid(row= 1, column=1)

        med_quantity_label.grid(row=2,column=0)
        med_quantity_entry.grid(row=2,column=1)

        med_sub_btn.grid(row=3, column=1)
       
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        input_inf_win.mainloop()

        
    