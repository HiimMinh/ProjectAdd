from tkinter import *
from tkinter.ttk import *
import sqlite3

class Win_Employees:
    def __init__(self, driver):
        self.driver = driver


    # Function to manage employees
    def open_employees(self, root):
        # Create patien window
        win = Toplevel(root)
        win.title("Employee")
        # Rezise patient window
        win.geometry("1600x900")


        #======================================================================================================
        #============================================= Doctors ================================================
        #======================================================================================================
        # Databases
        # Create a database or connect to one
        conn = sqlite3.connect("hospital.db")

        # Create cursor
        c = conn.cursor()
        

        # # Create scroll bar for the screen
        # scroll_frame = Frame(win)
        # scroll_frame.pack(fill=BOTH, expand=1)

        # my_scrollbar = Scrollbar(scroll_frame, orient= VERTICAL)
        # my_scrollbar.pack(side=RIGHT, fill= Y)
       
        # Create Treeview Frame
        tree1_frame = Frame(win)
        tree1_frame.pack()

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
        

        # Create striped row tags
        my_tree1.tag_configure("oddrow", background= "white")
        my_tree1.tag_configure("evenrow", background= "lightblue")

     
        add_frame = LabelFrame(win, text = "Doctor Record")
        add_frame.pack(fill="x", expand="yes", padx= 20)

        id1 = Label(add_frame, text="ID")
        id1.grid(row=0, column=5, padx= 10, pady= 5)

        n1 = Label(add_frame, text="Name")
        n1.grid(row=0, column=0, padx= 10, pady= 5)

        dob = Label(add_frame, text="DoB")
        dob.grid(row=0, column = 1, padx= 10, pady= 5)

        sex = Label(add_frame, text = "Sex")
        sex.grid(row=0, column = 2, padx= 10, pady= 5)
        
        maj = Label(add_frame, text = "Major")
        maj.grid(row=0, column = 3, padx= 10, pady= 5)

        sal = Label(add_frame, text = "Salary")
        sal.grid(row=0, column = 4, padx= 10, pady= 5)

        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ID
        id1_box = Entry(add_frame)
        id1_box.grid(row=1, column=5, padx= 10, pady= 5)

        # Name
        name_box = Entry(add_frame)
        name_box.grid(row=1, column=0, padx= 10, pady= 5)

        dob_box = Entry(add_frame)
        dob_box.grid(row=1, column=1, padx= 10, pady= 5)

        sex_box = Combobox(add_frame)
        sex_box['values'] = ("Male", "Female")
        sex_box.current(0)
        sex_box.grid(row=1, column=2, padx= 10, pady= 5)

        maj_box = Entry(add_frame)
        maj_box.grid(row=1, column=3, padx= 10, pady= 5)

        sal_box = Entry(add_frame)
        sal_box.grid(row=1, column=4, padx= 10, pady= 5)

        

        # Select Record
        def select_record(e):
            # Clear boxes
            name_box.delete(0, END)
            dob_box.delete(0, END)
            sex_box.delete(0, END)
            maj_box.delete(0, END)
            sal_box.delete(0, END)
            id1_box.delete(0, END)
            

            # Grab record Number
            selected = my_tree1.focus()

            # Grab record values
            values = my_tree1.item(selected, 'values')

            # Output to entry boxes
            id1_box.insert(0, values[0])
            name_box.insert(0, values[1])
            dob_box.insert(0, values[2])
            sex_box.insert(0, values[3])
            maj_box.insert(0, values[4])
            sal_box.insert(0, values[5])
            

        # Update Record 
        def update_record():
            
            #Grab the record Number
            selected = my_tree1.focus()

            # Update record
            my_tree1.item(selected, text='', values=(id1_box.get(),name_box.get(), dob_box.get(), sex_box.get(), maj_box.get(), sal_box.get()))

            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            c.execute("""UPDATE doctors SET
                    doc_id = :doc_id,
                    doc_name = :doc_name,
                    doc_dob = :doc_dob,
                    doc_sex = :doc_sex,
                    doc_major = :doc_major,
                    doc_salary = :doc_salary

                    WHERE doc_id = :doc_id""",
                    {   
                        'doc_id' : id1_box.get(),
                        'doc_name': name_box.get(),
                        'doc_dob' : dob_box.get(),
                        'doc_sex' : sex_box.get(),
                        'doc_major' : maj_box.get(),
                        'doc_salary' :sal_box.get()
                        
                    }
                    )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            # Pull data before running program
            query_database()




        # Add record
        def add_record():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Add New Record
            c.execute("INSERT INTO doctors (doc_name, doc_dob, doc_sex, doc_major, doc_salary) Values (:doc_name, :doc_dob, :doc_sex, :doc_major, :doc_salary)",
            {   
                'doc_name' : name_box.get(),
                'doc_dob' : dob_box.get(),
                'doc_sex' : sex_box.get(),
                'doc_major' : maj_box.get(),
                'doc_salary' : sal_box.get(),
            }
            )
          
            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            # Clear boxes
            name_box.delete(0, END)
            dob_box.delete(0, END)
            sex_box.delete(0, END)
            maj_box.delete(0, END)
            sal_box.delete(0, END)

            # Clear The Treeview Table
            my_tree1.delete(*my_tree1.get_children())

            # Run to pull data from database on start
            query_database()

        # Show records upon running program
        def query_database():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Query the database
            c.execute("SELECT * FROM doctors")
            records = c.fetchall()
            
            # Loop Thru Results
            global count
            count = 0
            for record in records:
                if count % 2 == 0:
                    my_tree1.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3], record[4], record[5]) , tags= ("evenrow",))              
                else:
                    my_tree1.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3], record[4], record[5]) , tags= ("oddrow",))
                count += 1

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()



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

        # Buttons frame
        btn_frame = LabelFrame(win, text= "Doctor Command")
        btn_frame.pack(fill ="x", expand="yes", padx=20)

        # Buttons
        add_recordx = Button(btn_frame, text="Add Record", command= add_record)
        add_recordx.grid(row= 0 , column= 0, padx= 10, pady= 10)

        # Show Records
        update_record = Button(btn_frame, text = "Update Record", command= update_record)
        update_record.grid(row = 0, column= 1, padx= 10, pady= 10)

        # Remove all
        remove_allx = Button(btn_frame, text = "Remove All Record", command = remove_all)
        remove_allx.grid(row = 0, column= 2, padx= 10, pady= 10)

        # Remove one
        remove_onex = Button(btn_frame, text= "Remove One Selected", command=remove_one)
        remove_onex.grid(row= 0, column= 3, padx= 10, pady= 10)

        # Remove many selected
        remove_manyx = Button(btn_frame, text = "Remove Many Selected", command= remove_many)
        remove_manyx.grid(row = 0, column= 4, padx= 10, pady= 10)

        # Bind the treeview
        my_tree1.bind("<ButtonRelease-1>", select_record)

        #======================================================================================================
        #============================================= Nurses =================================================
        #======================================================================================================
        
        # label_nurse= Label(win, text = "Nurse" ,font=('calibre',20, 'bold') )
        # label_nurse.pack(pady= 20)

        # Add some style
        style2 = Style()
        style2.configure("Treeview",
                rowheight = 15)
                
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
        my_tree2['columns'] = ("ID", "Name", "DoB", "Sex", "Salary", "Support doctor ID")

        # Formate our columns
        my_tree2.column("#0", width = 0, stretch = NO)
        my_tree2.column("ID", anchor = W, width =100)
        my_tree2.column("Name", anchor = CENTER, width = 200)
        my_tree2.column("DoB", anchor = W, width = 200)
        my_tree2.column("Sex", anchor = W, width = 100)
        my_tree2.column("Salary", anchor = W, width = 200)
        my_tree2.column("Support doctor ID", anchor = W, width = 50)

        # Create Headings
        my_tree2.heading("#0", text = "", anchor = CENTER)
        my_tree2.heading("ID", text = "ID", anchor=CENTER)
        my_tree2.heading("Name", text = "Name", anchor=CENTER)
        my_tree2.heading("DoB", text = "DoB", anchor=CENTER)
        my_tree2.heading("Sex", text = "Sex", anchor=CENTER)
        my_tree2.heading("Salary", text = "Salary", anchor=CENTER)
        my_tree2.heading("Support doctor ID", text = "Support doctor ID", anchor=CENTER)

        #?????????????????????????
        
        
        
        #?????????????????????????

        # Create striped row tags
        my_tree2.tag_configure("oddrow", background= "white")
        my_tree2.tag_configure("evenrow", background= "lightblue")

        my_tree2.pack(pady= 10)
       
        add_frame2 = LabelFrame(win, text= "Nurse Record")
        add_frame2.pack(fill="x", expand="yes", padx= 20)

        id2 = Label(add_frame2, text="ID")
        id2.grid(row=0, column=4, padx= 10, pady= 5)

        name2 = Label(add_frame2, text="Name")
        name2.grid(row=0, column=0, padx= 10, pady= 5)

        dob2 = Label(add_frame2, text="DoB")
        dob2.grid(row=0, column = 1, padx= 10, pady= 5)

        sex2 = Label(add_frame2, text = "Sex")
        sex2.grid(row=0, column = 2, padx= 10, pady= 5)

        sal2 = Label(add_frame2, text = "Salary")
        sal2.grid(row=0, column = 3, padx= 10, pady= 5)

        doctorsp_id_label = Label(add_frame2, text = "Support doctor ID")
        doctorsp_id_label.grid(row=0, column = 5, padx= 10, pady= 5)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ID
        id_box2 = Entry(add_frame2)
        id_box2.grid(row=1, column=4, padx= 10, pady= 5)

        # Name
        name_box2 = Entry(add_frame2)
        name_box2.grid(row=1, column=0, padx= 10, pady= 5)

       
        dob_box2 = Entry(add_frame2)
        dob_box2.grid(row=1, column=1, padx= 10, pady= 5)

       
        sex_box2 = Combobox(add_frame2)
        sex_box2['values'] = ("Male", "Female")
        sex_box2.current(0)
        sex_box2.grid(row=1, column=2, padx= 10, pady= 5)
       
        sal_box2 = Entry(add_frame2)
        sal_box2.grid(row=1, column=3, padx= 10, pady= 5)
        
        doctorsp_id_box = Entry(add_frame2)
        doctorsp_id_box.grid(row=1, column=5, padx= 10, pady= 5)

        # Select Record
        def select_record2(e):
            # Clear boxes
            name_box2.delete(0, END)
            dob_box2.delete(0, END)
            sex_box2.delete(0, END)
            sal_box2.delete(0, END)
            id_box2.delete(0, END)
            doctorsp_id_box.delete(0 , END)
        
            # Grab record Number
            selected = my_tree2.focus()

            # Grab record values
            values = my_tree2.item(selected, 'values')

            # Output to entry boxes
            id_box2.insert(0, values[0])
            name_box2.insert(0, values[1])
            dob_box2.insert(0, values[2])
            sex_box2.insert(0, values[3])
            sal_box2.insert(0, values[4])
            doctorsp_id_box.insert(0, values[5])

        # Update Record 
        def update_record2():
            
            #Grab the record Number
            selected = my_tree2.focus()

            # Update record
            my_tree2.item(selected, text='', values=(id_box2.get(),name_box2.get(), dob_box2.get(), sex_box2.get(), sal_box2.get(), doctorsp_id_box.get()))

            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            c.execute("""UPDATE nurses SET
                    nur_id = :nur_id,
                    nur_name = :nur_name,
                    nur_dob = :nur_dob,
                    nur_sex = :nur_sex,
                    nur_salary = :nur_salary
                    docsp_id = :docsp_id

                    WHERE nur_id = :nur_id""",
                    {   
                        'p_id' : id_box2.get(),
                        'p_name': name_box2.get(),
                        'p_dob' : dob_box2.get(),
                        'p_sex' : sex_box2.get(),
                        'p_salary' : sal_box2.get(),
                        'docsp_id' : doctorsp_id_box.get()
                    }
                    )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            # Pull data before running program
            query_database2()

        # Add record
        def add_record2():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Add New Record
            c.execute("INSERT INTO nurses (nur_name, nur_dob, nur_sex, nur_salary, docsp_id) Values (:nur_name, :nur_dob, :nur_sex, :nur_salary, :docsp_id)",
            {   
                'nur_name' : name_box2.get(),
                'nur_dob' : dob_box2.get(),
                'nur_sex' : sex_box2.get(),
                'nur_salary' : sal_box2.get(),
                'docsp_id' : doctorsp_id_box.get()
            }
            )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            # Clear boxes
            name_box2.delete(0, END)
            dob_box2.delete(0, END)
            sex_box2.delete(0, END)
            sal_box2.delete(0, END)
            doctorsp_id_box.delete(0, END)

            # Clear The Treeview Table
            my_tree2.delete(*my_tree2.get_children())

            # Run to pull data from database on start
            query_database2()
        
        # Show records upon running program
        def query_database2():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Query the database
            c.execute("SELECT * FROM nurses")
            records2 = c.fetchall()
            
            # Loop Thru Results
            global count
            count = 0
            for record in records2:
                if count % 2 == 0:
                    my_tree2.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3], record[4], record[5]) , tags= ("evenrow",))              
                else:
                    my_tree2.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3], record[4], record[5]) , tags= ("oddrow",))            
                count += 1

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

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

        # Buttons Frame
        btn_frame2 = LabelFrame(win, text= "Nurse Command" )
        btn_frame2.pack(fill ="x", expand="yes", padx=20)

        # Buttons
        add_recordx2 = Button(btn_frame2, text="Add Record", command= add_record2)
        add_recordx2.grid(row= 0 , column= 0, padx= 10, pady= 5)

        # Show Records
        update_record2 = Button(btn_frame2, text = "Update Record", command= update_record2)
        update_record2.grid(row = 0, column= 1, padx= 10, pady= 5)

        # Remove all
        remove_allx2 = Button(btn_frame2, text = "Remove All Record", command = remove_all2)
        remove_allx2.grid(row = 0, column= 2, padx= 10, pady= 5)

        # Remove one
        remove_onex2 = Button(btn_frame2, text= "Remove One Selected", command=remove_one2)
        remove_onex2.grid(row= 0, column= 3, padx= 10, pady= 5)

        # Remove many selected
        remove_manyx2 = Button(btn_frame2, text = "Remove Many Selected", command= remove_many2)
        remove_manyx2.grid(row = 0, column= 4, padx= 10, pady= 5)

        # Bind the treeview
        my_tree2.bind("<ButtonRelease-1>", select_record2)


        # Pull data before running program
        query_database2()
        query_database()

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        # Win loop
        win.mainloop()
