
from tkinter import *
from tkinter.ttk import *

class Win_Employees:
    def __init__(self, driver):
        self.driver = driver


    # Function to manage employees
    def open_employees(self, root):
        #======================================================================================================
        #============================================= Doctors ================================================
        #======================================================================================================
        # Create patien window
        win = Toplevel(root)
        win.title("Employee")

        # Rezise patient window
        win.geometry("1600x900")

        label_doctor = Label(win, text = "Doctor" ,font=('calibre',20, 'bold') )
        label_doctor.pack(pady= 5)

        # Create Treeview Frame
        tree1_frame = Frame(win)
        tree1_frame.pack(pady=5)

        # Treeview scrollbar
        tree1_scroll = Scrollbar(tree1_frame)
        tree1_scroll.pack(side=RIGHT, fill= Y)

        # Create Treeview
        my_tree1 = Treeview(tree1_frame, yscrollcommand= tree1_scroll.set, selectmode='extended')


        # Pack to the screen
        my_tree1.pack()

        # Configure the scrollbar
        tree1_scroll.config(command=my_tree1.yview)

        # Define our columns
        my_tree1['columns'] = ("ID", "Name", "DoB", "Sex", "Major", "Salary")

        # Formate our columns
        my_tree1.column("#0", width = 0, stretch = NO)
        my_tree1.column("ID", anchor = W, width =100)
        my_tree1.column("Name", anchor = CENTER, width = 200)
        my_tree1.column("DoB", anchor = W, width = 200)
        my_tree1.column("Sex", anchor = W, width = 100)
        my_tree1.column("Major", anchor = W, width = 200)
        my_tree1.column("Salary", anchor = W, width = 200)


        # Create Headings
        my_tree1.heading("#0", text = "", anchor = CENTER)
        my_tree1.heading("ID", text = "ID", anchor=CENTER)
        my_tree1.heading("Name", text = "Name", anchor=CENTER)
        my_tree1.heading("DoB", text = "DoB", anchor=CENTER)
        my_tree1.heading("Sex", text = "Sex", anchor=CENTER)
        my_tree1.heading("Major", text = "Major", anchor=CENTER)
        my_tree1.heading("Salary", text = "Salary", anchor=CENTER)


        #?????????????????????????
        # Data from database
        #?????????????????????????
        data = []

        # Create striped row tags
        my_tree1.tag_configure("oddrow", background= "white")
        my_tree1.tag_configure("evenrow", background= "lightblue")


        # Insert data to treeview
        global count
        count = 0
        for record in data:
            if count % 2 == 0:
                my_tree1.insert(parent='', index='end', iid= count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags= ("evenrow",))              
            else:
                my_tree1.insert(parent='', index='end', iid= count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags= ("oddrow",))   
            count += 1

     

        add_frame = Frame(win)
        add_frame.pack()

        n1 = Label(add_frame, text="Name")
        n1.grid(row=0, column=0)

        dob = Label(add_frame, text="DoB")
        dob.grid(row=0, column = 1)

        sex = Label(add_frame, text = "Sex")
        sex.grid(row=0, column = 2)
        
        maj = Label(add_frame, text = "Major")
        maj.grid(row=0, column = 3)

        sal = Label(add_frame, text = "Salary")
        sal.grid(row=0, column = 4)


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ID = count
        
        # Name
        name_box = Entry(add_frame, width = 30)
        name_box.grid(row=1, column=0)

       
        dob_box = Entry(add_frame, width = 20)
        dob_box.grid(row=1, column=1)

       
        sex_box = Combobox(add_frame, width = 8)
        sex_box['values'] = ("Male", "Female")
        sex_box.current(0)
        sex_box.grid(row=1, column=2)

    
       
        maj_box = Entry(add_frame, width = 30)
        maj_box.grid(row=1, column=3)

       
        sal_box = Entry(add_frame, width = 30)
        sal_box.grid(row=1, column=4)




        # Add record
        def add_record():
            global count
            if count % 2 == 0:
                my_tree1.insert(parent='', index='end', iid= count, text='', values=(count+1, name_box.get(), dob_box.get(), sex_box.get(), maj_box.get(), sal_box.get()), tags= "evenrow",)

                # Append information to database here



            else:
                my_tree1.insert(parent='', index='end', iid= count, text='', values=(count+1, name_box.get(), dob_box.get(), sex_box.get(), maj_box.get(), sal_box.get()), tags = "oddrow",)

                # Append information to database here




            count += 1

            # Clear boxes
            name_box.delete(0, END)
            dob_box.delete(0, END)
            sex_box.delete(0, END)
            maj_box.delete(0, END)
            sal_box.delete(0, END)


        # Remove all
        def remove_all():
            for record in my_tree1.get_children():
                my_tree1.delete(record) 

            # Remove data away from database here   
        
        # Remove one selected
        def remove_one():
            x = my_tree1.selection()[0]
            my_tree1.delete(x)

            # Remove data away from database here   


        # Remove many selected
        def remove_many():
            x = my_tree1.selection()
            for record in x:
                my_tree1.delete(record)

            # Remove data away from database here   

        btn_frame = Frame(win)
        btn_frame.pack(pady = 20)


        # Buttons
        add_recordx = Button(btn_frame, text="Add Record", command= add_record)
        add_recordx.grid(row= 0 , column= 0, padx= 20)


        # Remove all
        remove_allx = Button(btn_frame, text = "Remove All Record", command = remove_all)
        remove_allx.grid(row = 0, column= 1, padx= 20)

        # Remove one
        remove_onex = Button(btn_frame, text= "Remove One Selected", command=remove_one)
        remove_onex.grid(row= 0, column= 2, padx= 20)

        # Remove many selected
        remove_manyx = Button(btn_frame, text = "Remove Many Selected", command= remove_many)
        remove_manyx.grid(row = 0, column= 3, padx= 20)

        
        #======================================================================================================
        #============================================= Nurses =================================================
        #======================================================================================================
        
        label_nurse= Label(win, text = "Nurse" ,font=('calibre',20, 'bold') )
        label_nurse.pack(pady= 20)

        # Create Treeview Frame
        tree2_frame = Frame(win)
        tree2_frame.pack()

        # Treeview scrollbar
        tree2_scroll = Scrollbar(tree2_frame)
        tree2_scroll.pack(side=RIGHT, fill= Y)

        # Create Treeview
        my_tree2 = Treeview(tree2_frame, yscrollcommand= tree2_scroll.set, selectmode='extended')


        # Pack to the screen
        my_tree2.pack()

        # Configure the scrollbar
        tree2_scroll.config(command=my_tree2.yview)

        # Define our columns
        my_tree2['columns'] = ("ID", "Name", "DoB", "Sex", "Salary")

        # Formate our columns
        my_tree2.column("#0", width = 0, stretch = NO)
        my_tree2.column("ID", anchor = W, width =100)
        my_tree2.column("Name", anchor = CENTER, width = 200)
        my_tree2.column("DoB", anchor = W, width = 200)
        my_tree2.column("Sex", anchor = W, width = 100)
        my_tree2.column("Salary", anchor = W, width = 200)


        # Create Headings
        my_tree2.heading("#0", text = "", anchor = CENTER)
        my_tree2.heading("ID", text = "ID", anchor=CENTER)
        my_tree2.heading("Name", text = "Name", anchor=CENTER)
        my_tree2.heading("DoB", text = "DoB", anchor=CENTER)
        my_tree2.heading("Sex", text = "Sex", anchor=CENTER)
        my_tree2.heading("Salary", text = "Salary", anchor=CENTER)


        #?????????????????????????
        # Data from database
        #?????????????????????????
        data2 = []

        # Create striped row tags
        my_tree2.tag_configure("oddrow", background= "white")
        my_tree2.tag_configure("evenrow", background= "lightblue")


        # Insert data to treeview
        global count2
        count2 = 0
        for record in data2:
            if count % 2 == 0:
                my_tree1.insert(parent='', index='end', iid= count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags= ("evenrow",))              
            else:
                my_tree1.insert(parent='', index='end', iid= count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags= ("oddrow",))   
            count += 1


        add_frame2 = Frame(win)
        add_frame2.pack()

        n1 = Label(add_frame2, text="Name")
        n1.grid(row=0, column=0)

        dob = Label(add_frame2, text="DoB")
        dob.grid(row=0, column = 1)

        sex = Label(add_frame2, text = "Sex")
        sex.grid(row=0, column = 2)

        sal = Label(add_frame2, text = "Salary")
        sal.grid(row=0, column = 3)


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ID = count
        
        # Name
        name_box2 = Entry(add_frame2, width = 30)
        name_box2.grid(row=1, column=0)

       
        dob_box2 = Entry(add_frame2, width = 20)
        dob_box2.grid(row=1, column=1)

       
        sex_box2 = Combobox(add_frame2, width = 8)
        sex_box2['values'] = ("Male", "Female")
        sex_box2.current(0)
        sex_box2.grid(row=1, column=2)
       
        sal_box2 = Entry(add_frame2, width = 30)
        sal_box2.grid(row=1, column=3)




        # Add record
        def add_record2():
            global count2
            if count2 % 2 == 0:
                my_tree2.insert(parent='', index='end', iid= count2, text='', values=(count2+1, name_box2.get(), dob_box2.get(), sex_box2.get(), sal_box2.get()), tags= "evenrow",)

                # Append information to database here



            else:
                my_tree2.insert(parent='', index='end', iid= count2, text='', values=(count2+1, name_box2.get(), dob_box2.get(), sex_box2.get(), sal_box2.get()), tags = "oddrow",)

                # Append information to database here




            count2 += 1

            # Clear boxes
            name_box2.delete(0, END)
            dob_box2.delete(0, END)
            sex_box2.delete(0, END)
            sal_box2.delete(0, END)


        # Remove all
        def remove_all2():
            for record in my_tree2.get_children():
                my_tree2.delete(record) 

            # Remove data away from database here   
        
        # Remove one selected
        def remove_one2():
            x = my_tree2.selection()[0]
            my_tree2.delete(x)

            # Remove data away from database here   


        # Remove many selected
        def remove_many2():
            x = my_tree2.selection()
            for record in x:
                my_tree2.delete(record)

            # Remove data away from database here   

        btn_frame2 = Frame(win)
        btn_frame2.pack(pady = 20)


        # Buttons
        add_recordx2 = Button(btn_frame2, text="Add Record", command= add_record2)
        add_recordx2.grid(row= 0 , column= 0, padx= 20)


        # Remove all
        remove_allx2 = Button(btn_frame2, text = "Remove All Record", command = remove_all2)
        remove_allx2.grid(row = 0, column= 1, padx= 20)

        # Remove one
        remove_onex2 = Button(btn_frame2, text= "Remove One Selected", command=remove_one2)
        remove_onex2.grid(row= 0, column= 2, padx= 20)

        # Remove many selected
        remove_manyx2 = Button(btn_frame2, text = "Remove Many Selected", command= remove_many2)
        remove_manyx2.grid(row = 0, column= 3, padx= 20)




        # Win loop
        win.mainloop()
