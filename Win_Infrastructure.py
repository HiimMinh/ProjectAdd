from tkinter import *
from tkinter.ttk import *
import sqlite3

class Win_Infrastructure:
    def __init__(self, driver):
        self.driver = driver


    # Function to manage infrastructure
    def open_inf(self, root):
        # Create infrastructure window
        win = Toplevel(root)
        win.title("Infrastructure")
        # Rezise patient window
        win.geometry("1600x900")

        #======================================================================================================
        #============================================= Rooms =================================================
        #======================================================================================================
        # Databases
        # Create a database or connect to one
        conn = sqlite3.connect("hospital.db")

        # Create cursor
        c = conn.cursor()

        # Create Treeview Frame
        tree1_frame = Frame(win)
        tree1_frame.pack()

        # Add some style
        style2 = Style()
        style2.configure("Treeview",
                rowheight = 15)
                

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
        my_tree1['columns'] = ("ID", "Name")

        # Formate our columns
        my_tree1.column("#0", width = 0, stretch = NO)
        my_tree1.column("ID", anchor = W, width =100)
        my_tree1.column("Name", anchor = CENTER, width = 200)
       

        # Create Headings
        my_tree1.heading("#0", text = "", anchor = CENTER)
        my_tree1.heading("ID", text = "ID", anchor=CENTER)
        my_tree1.heading("Name", text = "Name", anchor=CENTER)
        
        # Create striped row tags
        my_tree1.tag_configure("oddrow", background= "white")
        my_tree1.tag_configure("evenrow", background= "lightblue")

        # Room Record Frame
        add_frame = LabelFrame(win, text = "Room Record")
        add_frame.pack(fill="x", expand="yes", padx= 20)

        id1 = Label(add_frame, text="ID")
        id1.grid(row=0, column=0, padx= 10, pady= 5)

        name1 = Label(add_frame, text="Name")
        name1.grid(row=0, column = 1, padx= 10, pady= 5)

    

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Room ID
        id1_box = Entry(add_frame)
        id1_box.grid(row=1, column=0, padx= 10, pady= 5)

        # Room Name
        name1_box = Entry(add_frame)
        name1_box.grid(row=1, column=1, padx= 10, pady= 5)

        # Select Record
        def select_record1(e):
            # Clear boxes
            id1_box.delete(0, END)
            name1_box.delete(0, END)

            # Grab record Number
            selected = my_tree1.focus()

            # Grab record values
            values = my_tree1.item(selected, 'values')

            # Output to entry boxes
            id1_box.insert(0, values[0])
            name1_box.insert(0, values[1])

        # Update Record 
        def update_record1():
            
            #Grab the record Number
            selected = my_tree1.focus()

            # Update record
            my_tree1.item(selected, text='', values=(id1_box.get(),name1_box.get()))

            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            c.execute("""UPDATE rooms SET
                    r_id = :r_id,
                    r_name = :r_name
                   
                    WHERE r_id = :r_id""",
                    {   
                        'r_id' : id1_box.get(),
                        'r_name': name1_box.get()
                       
                    }
                    )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            # Pull data before running program
            query_database1()


        # Add record
        def add_record1():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Add New Record
            c.execute("INSERT INTO rooms (r_id, r_name) Values (:r_id, :r_name)",
            {   
                'r_id' : id1_box.get(),
                'r_name' : name1_box.get()
            }
            )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()
           
            # Clear boxes
            id1_box.delete(0, END)
            name1_box.delete(0, END)
           
            # Clear The Treeview Table
            my_tree1.delete(*my_tree1.get_children())

            # Run to pull data from database on start
            query_database1()


        # Show records upon running program
        def query_database1():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Query the database
            c.execute("SELECT * FROM rooms")
            records = c.fetchall()
            
            # Loop Thru Results
            global count
            count = 0
            for record in records:
                if count % 2 == 0:
                    my_tree1.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1]) , tags= ("evenrow",))              
                else:
                    my_tree1.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1]) , tags= ("oddrow",))
                count += 1

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

        # Remove all
        def remove_all1():
            for record in my_tree1.get_children():
                my_tree1.delete(record) 

            # Remove data away from database here   
        
        # Remove one selected
        def remove_one1():
            x = my_tree1.selection()[0]
            my_tree1.delete(x)

            # Remove data away from database here   


        # Remove many selected
        def remove_many1():
            x = my_tree1.selection()
            for record in x:
                my_tree1.delete(record)

            # Remove data away from database here   

        btn_frame1 = LabelFrame(win, text= "Room Command")
        btn_frame1.pack(fill ="x", expand="yes", padx=20)


        # Buttons
        add_record1 = Button(btn_frame1, text="Add Record", command= add_record1)
        add_record1.grid(row= 0 , column= 0, padx= 10, pady= 5)

        # Update Records
        update_record = Button(btn_frame1, text = "Update Record", command= update_record1)
        update_record.grid(row = 0, column= 1, padx= 10, pady= 5)

        # Remove all
        remove_all1 = Button(btn_frame1, text = "Remove All Record", command = remove_all1)
        remove_all1.grid(row = 0, column= 2, padx= 10, pady= 5)

        # Remove one
        remove_one1 = Button(btn_frame1, text= "Remove One Selected", command=remove_one1)
        remove_one1.grid(row= 0, column= 3, padx= 10, pady= 5)

        # Remove many selected
        remove_many1 = Button(btn_frame1, text = "Remove Many Selected", command= remove_many1)
        remove_many1.grid(row = 0, column= 4, padx= 10, pady= 5)

        # Bind the treeview
        my_tree1.bind("<ButtonRelease-1>", select_record1)

        # Pull data before running program
        query_database1()

        #======================================================================================================
        #============================================= Beds =================================================
        #======================================================================================================
        
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
        my_tree2['columns'] = ("Bed ID", "Room Name", "Room ID", "Patient ID")

        # Formate our columns
        my_tree2.column("#0", width = 0, stretch = NO)
        my_tree2.column("Bed ID", anchor = W, width =100)
        my_tree2.column("Room Name", anchor = CENTER, width = 200)
        my_tree2.column("Room ID", anchor = W, width = 200)
        my_tree2.column("Patient ID", anchor = W, width = 100)
     

        # Create Headings
        my_tree2.heading("#0", text = "", anchor = CENTER)
        my_tree2.heading("Bed ID", text = "Bed ID", anchor=CENTER)
        my_tree2.heading("Room Name", text = "Room Name", anchor=CENTER)
        my_tree2.heading("Room ID", text = "Room ID", anchor=CENTER)
        my_tree2.heading("Patient ID", text = "Patient ID", anchor=CENTER)
      
        # Create striped row tags
        my_tree2.tag_configure("oddrow", background= "white")
        my_tree2.tag_configure("evenrow", background= "lightblue")

        my_tree2.pack(pady= 10)


        add_frame2 = LabelFrame(win, text= "Bed Record")
        add_frame2.pack(fill="x", expand="yes", padx= 20)

        bed_id = Label(add_frame2, text="Bed ID")
        bed_id.grid(row=0, column=0)

        room_name = Label(add_frame2, text="Room Name")
        room_name.grid(row=0, column = 1)

        room_id = Label(add_frame2, text="Room ID")
        room_id.grid(row=0, column = 2)

        patient_id = Label(add_frame2, text = "Patient ID")
        patient_id.grid(row=0, column = 3)

        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ID
        bed_id_box = Entry(add_frame2)
        bed_id_box.grid(row=1, column=0, padx= 10, pady= 5)

        # Room Name
        room_name_box = Entry(add_frame2)
        room_name_box.grid(row=1, column=1, padx= 10, pady= 5)

        # Room ID
        room_id_box = Entry(add_frame2)
        room_id_box.grid(row=1, column=2, padx= 10, pady= 5)

        # Patient ID
        patient_id_box = Entry(add_frame2)
        patient_id_box.grid(row=1, column=3, padx= 10, pady= 5)
       
        # Select Record
        def select_record2(e):
            # Clear boxes
            bed_id_box.delete(0, END)
            room_name_box.delete(0, END)
            room_id_box.delete(0, END)
            patient_id_box.delete(0, END)

            # Grab record Number
            selected = my_tree2.focus()

            # Grab record values
            values = my_tree2.item(selected, 'values')

            # Output to entry boxes
            bed_id_box.insert(0, values[0])
            room_name_box.insert(0, values[1])
            room_id_box.insert(0, values[2])
            patient_id_box.insert(0, values[3])


        # Update Record 
        def update_record2():
            
            #Grab the record Number
            selected = my_tree2.focus()

            # Update record
            my_tree2.item(selected, text='', values=(bed_id_box.get(),room_name_box.get(), room_id_box.get(), patient_id_box.get()))

            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Still lack of foreign key!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            c.execute("""UPDATE beds SET
                    bed_id = :bed_id,
                    bed_r_name = :bed_r_name,
                    bed_r_id = :bed_r_id,
                    bed_p_id = :bed_p_id,
                
                    WHERE bed_id = :bed_id""",
                    {   
                        'bed_id' : bed_id_box.get(),
                        'bed_r_name': room_name_box.get(),
                        'bed_r_id' : room_id_box.get(),
                        'bed_p_id' : patient_id_box.get(),
                        
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
            c.execute("INSERT INTO beds (bed_r_name, bed_r_id, bed_p_id) Values (:bed_r_name, :bed_r_id, :bed_p_id)",
            {   
                'bed_r_name' : room_name_box.get(),
                'bed_r_id' : room_id_box.get(),
                'bed_p_id' : patient_id_box.get(),
            }
            )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()


            # Clear boxes
            room_name_box.delete(0, END)
            room_id_box.delete(0, END)
            patient_id_box.delete(0, END)

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
            c.execute("SELECT * FROM beds")
            records = c.fetchall()
            
            # Loop Thru Results
            global count
            count = 0
            for record in records:
                if count % 2 == 0:
                    my_tree2.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3]) , tags= ("evenrow",))              
                else:
                    my_tree2.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3]) , tags= ("oddrow",))
                count += 1

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

        # Remove all
        def remove_all2():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            for record in my_tree2.get_children():
                my_tree2.delete(record) 
                c.execute("DELETE from beds WHERE bed_id=" + record[0])   

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()  

            # Clear The Treeview Table
            my_tree2.delete(*my_tree2.get_children())

            # Run to pull data from database on start
            query_database2()

        # Remove one selected
        def remove_one2():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            x = my_tree2.selection()[0]
            my_tree2.delete(x)

            c.execute("DELETE from nurses WHERE nur_id=" + bed_id_box.get())

            # Clear boxes
            bed_id_box.delete(0, END)
            room_name_box.delete(0, END)
            room_id_box.delete(0, END)
            patient_id_box.delete(0, END)

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()  

            # Clear The Treeview Table
            my_tree2.delete(*my_tree2.get_children())

            # Run to pull data from database on start
            query_database2()

        # Remove many selected
        def remove_many2():
            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            x = my_tree2.selection()
            for record in x:
                my_tree2.delete(record)
                c.execute("DELETE from beds WHERE bed_id=" + record[0])

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()  

            # Clear The Treeview Table
            my_tree2.delete(*my_tree2.get_children())

            # Run to pull data from database on start
            query_database2()
        
        # Buttons frame
        btn_frame2 = LabelFrame(win, text= "Bed Command")
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
        
        # Win loop
        win.mainloop()
