from tkinter import *
from tkinter.ttk import *

class Win_Patients:

    def __init__(self, driver):
        self.driver = driver


    # Function to manage patients
    def open_patient(self, root):
        # Create patien window
        win = Toplevel(root)
        win.title("Patients")

        # Rezise patient window
        win.geometry("1600x900")


        # Create Treeview Frame
        tree_frame = Frame(win)
        tree_frame.pack(pady=20)

        # Treeview scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill= Y)

        # Create Treeview
        my_tree = Treeview(tree_frame, yscrollcommand= tree_scroll.set, selectmode='extended')


        # Pack to the screen
        my_tree.pack()

        # Configure the scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define our columns
        my_tree['columns'] = ("ID", "Name", "DoB", "Sex", "Address", "Ill")

        # Formate our columns
        my_tree.column("#0", width = 0, stretch = NO)
        my_tree.column("ID", anchor = W, width =100)
        my_tree.column("Name", anchor = CENTER, width = 200)
        my_tree.column("DoB", anchor = W, width = 200)
        my_tree.column("Sex", anchor = W, width = 100)
        my_tree.column("Address", anchor = W, width = 200)
        my_tree.column("Ill", anchor = W, width = 200)


        # Create Headings
        my_tree.heading("#0", text = "", anchor = CENTER)
        my_tree.heading("ID", text = "ID", anchor=CENTER)
        my_tree.heading("Name", text = "Name", anchor=CENTER)
        my_tree.heading("DoB", text = "DoB", anchor=CENTER)
        my_tree.heading("Sex", text = "Sex", anchor=CENTER)
        my_tree.heading("Address", text = "Address", anchor=CENTER)
        my_tree.heading("Ill", text = "Ill", anchor=CENTER)


        #?????????????????????????
        # Data from database
        #?????????????????????????
        data = []

        # Create striped row tags
        my_tree.tag_configure("oddrow", background= "white")
        my_tree.tag_configure("evenrow", background= "lightblue")


        # Insert data to treeview
        global count
        count = 0
        for record in data:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid= count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags= ("evenrow",))              
            else:
                my_tree.insert(parent='', index='end', iid= count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags= ("oddrow",))   
            count += 1

        my_tree.pack(pady = 20)


        add_frame = Frame(win)
        add_frame.pack(pady = 20)

        n1 = Label(add_frame, text="Name")
        n1.grid(row=0, column=0)

        dob = Label(add_frame, text="DoB")
        dob.grid(row=0, column = 1)

        sex = Label(add_frame, text = "Sex")
        sex.grid(row=0, column = 2)
        
        adr = Label(add_frame, text = "Address")
        adr.grid(row=0, column = 3)

        il = Label(add_frame, text = "Ill")
        il.grid(row=0, column = 4)


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

    
       
        adr_box = Entry(add_frame, width = 30)
        adr_box.grid(row=1, column=3)

       
        ill_box = Entry(add_frame, width = 30)
        ill_box.grid(row=1, column=4)




        # Add record
        def add_record():
            global count
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid= count, text='', values=(count+1, name_box.get(), dob_box.get(), sex_box.get(), adr_box.get(), ill_box.get()), tags= "evenrow",)

                # Append information to database here



            else:
                my_tree.insert(parent='', index='end', iid= count, text='', values=(count+1, name_box.get(), dob.get(), sex_box.get(), adr_box.get(), ill_box.get()), tags = "oddrow",)

                # Append information to database here




            count += 1

            # Clear boxes
            name_box.delete(0, END)
            dob_box.delete(0, END)
            sex_box.delete(0, END)
            adr_box.delete(0, END)
            ill_box.delete(0, END)


        # Remove all
        def remove_all():
            for record in my_tree.get_children():
                my_tree.delete(record) 

            # Remove data away from database here   
        
        # Remove one selected
        def remove_one():
            x = my_tree.selection()[0]
            my_tree.delete(x)

            # Remove data away from database here   


        # Remove many selected
        def remove_many():
            x = my_tree.selection()
            for record in x:
                my_tree.delete(record)

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

        
        # Win loop
        win.mainloop()


        
    