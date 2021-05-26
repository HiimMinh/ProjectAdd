from tkinter import *
from tkinter.ttk import *
import sqlite3

class Win_Patients:

    def __init__(self, driver):
        self.driver = driver

    # sqlite3.paramstyle = 'named'
    #======================================================================================================
    #============================================= Patients =================================================
    #======================================================================================================

    # Function to manage patients
    def open_patient(self, root):
        # Databases
        # Create a database or connect to one
        conn = sqlite3.connect("hospital.db")

        # Create cursor
        c = conn.cursor()

        # Create patien window
        win = Toplevel(root)
        win.title("Patients")

        # Rezise patient window
        win.geometry("1024x768")


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
        my_tree.column("ID", anchor = CENTER, width =100)
        my_tree.column("Name", anchor = CENTER, width = 200)
        my_tree.column("DoB", anchor = CENTER, width = 200)
        my_tree.column("Sex", anchor = CENTER, width = 100)
        my_tree.column("Address", anchor = CENTER, width = 200)
        my_tree.column("Ill", anchor = CENTER, width = 200)


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

        # Create striped row tags
        my_tree.tag_configure("oddrow", background= "white")
        my_tree.tag_configure("evenrow", background= "lightblue")

        # # Query the database
        # c.execute("SELECT *, oid FROM patients")
        # records = c.fetchall()

        # # Insert data to treeview
        # global count
        # count = 0
        # for record in records:
        #     if count % 2 == 0:
        #         my_tree.insert(parent='', index='end', iid= count, text='', values=(record[5], record[0], record[1], record[2], record[3], record[4]), tags= ("evenrow",))              
        #     else:
        #         my_tree.insert(parent='', index='end', iid= count, text='', values=(record[5], record[0], record[1], record[2], record[3], record[4]), tags= ("oddrow",))   
        #     count += 1

        my_tree.pack(pady = 20)


        add_frame = LabelFrame(win, text= "Patient Record")
        add_frame.pack(fill="x", expand="yes", padx= 20)

        id1 = Label(add_frame, text="ID")
        id1.grid(row=0, column=5, padx= 10, pady= 10)

        name = Label(add_frame, text="Name")
        name.grid(row=0, column=0, padx= 10, pady= 10)

        dob = Label(add_frame, text="DoB")
        dob.grid(row=0, column = 1, padx= 10, pady= 10)

        sex = Label(add_frame, text = "Sex")
        sex.grid(row=0, column = 2, padx= 10, pady= 10)
        
        adr = Label(add_frame, text = "Address")
        adr.grid(row=0, column = 3, padx= 10, pady= 10)

        il = Label(add_frame, text = "Ill")
        il.grid(row=0, column = 4, padx= 10, pady= 10)


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ID
        id1_box = Entry(add_frame)
        id1_box.grid(row=1, column=5, padx= 10, pady= 10)
        
        # Name
        name_box = Entry(add_frame)
        name_box.grid(row=1, column=0, padx= 10, pady= 10)

       
        dob_box = Entry(add_frame)
        dob_box.grid(row=1, column=1, padx= 10, pady= 10)

       
        sex_box = Combobox(add_frame)
        sex_box['values'] = ("Male", "Female")
        sex_box.current(0)
        sex_box.grid(row=1, column=2, padx= 10, pady= 10)

        adr_box = Entry(add_frame, width= 30)
        adr_box.grid(row=1, column=3, padx= 10, pady= 10)

       
        ill_box = Entry(add_frame)
        ill_box.grid(row=1, column=4, padx= 10, pady= 10)


        # Select Record
        def select_record(e):
            # Clear boxes
            name_box.delete(0, END)
            dob_box.delete(0, END)
            sex_box.delete(0, END)
            adr_box.delete(0, END)
            ill_box.delete(0, END)
            id1_box.delete(0, END)

            # Grab record Number
            selected = my_tree.focus()

            # Grab record values
            values = my_tree.item(selected, 'values')

            # Output to entry boxes
            id1_box.insert(0, values[0])
            name_box.insert(0, values[1])
            dob_box.insert(0, values[2])
            sex_box.insert(0, values[3])
            adr_box.insert(0, values[4])
            ill_box.insert(0, values[5])

        # Update Record 
        def update_record():
            
            #Grab the record Number
            selected = my_tree.focus()

            # Update record
            my_tree.item(selected, text='', values=(id1_box.get(),name_box.get(), dob_box.get(), sex_box.get(), adr_box.get(), ill_box.get()))

            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            c.execute("""UPDATE patients SET
                    p_id = :p_id,
                    p_name = :p_name,
                    p_dob = :p_dob,
                    p_sex = :p_sex,
                    p_address = :p_address,
                    p_ill = :p_ill

                    WHERE p_id = :p_id""",
                    {   
                        'p_id' : id1_box.get(),
                        'p_name': name_box.get(),
                        'p_dob' : dob_box.get(),
                        'p_sex' : sex_box.get(),
                        'p_address' : adr_box.get(),
                        'p_ill' : ill_box.get()
                        
                    }
                    )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            # Pull data before running program
            query_database()

            # Clear boxes
            name_box.delete(0, END)
            dob_box.delete(0, END)
            sex_box.delete(0, END)
            adr_box.delete(0, END)
            ill_box.delete(0, END)
            id1_box.delete(0, END)

        # Add Record to Database
        def add_record():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Add New Record
            c.execute("INSERT INTO patients (p_name, p_dob, p_sex, p_address, p_ill) Values (:p_name, :p_dob, :p_sex, :p_address, :p_ill)",
            {   
                'p_name' : name_box.get(),
                'p_dob' : dob_box.get(),
                'p_sex' : sex_box.get(),
                'p_address' : adr_box.get(),
                'p_ill' : ill_box.get(),
            }
            )
            # global count
            # if count % 2 == 0:
            #     my_tree.insert(parent='', index='end', iid= count, text='', values=(count+1, name_box.get(), dob_box.get(), sex_box.get(), adr_box.get(), ill_box.get()), tags= "evenrow",)

            # else:
            #     my_tree.insert(parent='', index='end', iid= count, text='', values=(count+1, name_box.get(), dob.get(), sex_box.get(), adr_box.get(), ill_box.get()), tags = "oddrow",)


            # count += 1
            
            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            

            # Clear The Treeview Table
            my_tree.delete(*my_tree.get_children())

            # Run to pull data from database on start
            query_database()

            # Clear boxes
            name_box.delete(0, END)
            dob_box.delete(0, END)
            sex_box.delete(0, END)
            adr_box.delete(0, END)
            ill_box.delete(0, END)
            
        # Show records upon running program
        def query_database():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Query the database
            c.execute("SELECT * FROM patients")
            records = c.fetchall()
            
            # Loop Thru Results
            global count
            count = 0
            for record in records:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3], record[4], record[5]) , tags= ("evenrow",))              
                else:
                    my_tree.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3], record[4], record[5]) , tags= ("oddrow",))
                count += 1

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

        # Remove all
        def remove_all():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            for record in my_tree.get_children():
                my_tree.delete(record) 

            c.execute("DELETE from patients")

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()  

            # # Clear The Treeview Table
            # my_tree.delete(*my_tree.get_children())

            # Run to pull data from database on start
            query_database()
        
        # Remove one selected
        def remove_one():
            x = my_tree.selection()[0]
            my_tree.delete(x)

            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            c.execute("DELETE from patients WHERE oid=" + id1_box.get())

            # Clear boxes
            id1_box.delete(0, END)
            name_box.delete(0, END)
            dob_box.delete(0, END)
            sex_box.delete(0, END)
            adr_box.delete(0, END)
            ill_box.delete(0, END)

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()  

            # Clear The Treeview Table
            my_tree.delete(*my_tree.get_children())

            # Run to pull data from database on start
            query_database()

        # Remove many selected
        def remove_many():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            x = my_tree.selection()
            for record in x:
                my_tree.delete(record)
                c.execute("DELETE from patients WHERE p_id=" + record[0])
            
            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()  

            # Clear The Treeview Table
            my_tree.delete(*my_tree.get_children())

            # Run to pull data from database on start
            query_database()


        # Buttons Frame
        btn_frame = LabelFrame(win, text= "Patient Command")
        btn_frame.pack(fill ="x", expand="yes", padx=20)
        # Buttons
        # Add Record
        add_recordx = Button(btn_frame, text="Add Record", command= add_record)
        add_recordx.grid(row= 0 , column= 0, padx= 10, pady= 10)

        # Show Records
        update_record = Button(btn_frame, text = "Update Record", command= update_record)
        update_record.grid(row = 0, column= 1, padx= 10, pady= 10)

        # Remove All
        remove_allx = Button(btn_frame, text = "Remove All Record", command = remove_all)
        remove_allx.grid(row = 0, column= 2, padx= 10, pady= 10)

        # Remove One
        remove_onex = Button(btn_frame, text= "Remove One Selected", command=remove_one)
        remove_onex.grid(row= 0, column= 3, padx= 10, pady= 10)

        # Remove Many Selected
        remove_manyx = Button(btn_frame, text = "Remove Many Selected", command= remove_many)
        remove_manyx.grid(row = 0, column= 4, padx= 10, pady= 10)

        
        # Bind the treeview
        my_tree.bind("<ButtonRelease-1>", select_record)

        # Pull data before running program
        query_database()

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        # Win loop
        win.mainloop()


        
    