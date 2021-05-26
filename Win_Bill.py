from tkinter import *
from tkinter.ttk import *
import sqlite3

class Win_Bill:
    def __init__(self, driver):
        self.driver = driver

    
    # Function to manage patients
    def open_bill(self, root):
        # Create patien window
        win = Toplevel(root)
        win.title("Patients")

        # Rezise patient window
        win.geometry("1600x900")


        #======================================================================================================
        #============================================= Medicine =================================================
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
        my_tree1['columns'] = ("ID", "Name", "Quantity", "Price/box")

        # Formate our columns
        my_tree1.column("#0", width = 0, stretch = NO)
        my_tree1.column("ID", anchor = W, width =100)
        my_tree1.column("Name", anchor = CENTER, width = 200)
        my_tree1.column("Quantity", anchor = CENTER, width = 100)
        my_tree1.column("Price/box", anchor = CENTER, width = 100)
       

        # Create Headings
        my_tree1.heading("#0", text = "", anchor = CENTER)
        my_tree1.heading("ID", text = "ID", anchor=CENTER)
        my_tree1.heading("Name", text = "Name", anchor=CENTER)
        my_tree1.heading("Quantity", text = "Quantity", anchor=CENTER)
        my_tree1.heading("Price/box", text = "Price/box", anchor=CENTER)
        
        # Create striped row tags
        my_tree1.tag_configure("oddrow", background= "white")
        my_tree1.tag_configure("evenrow", background= "lightblue")

        # Medicine Record Frame
        add_frame = LabelFrame(win, text = "Medicine Record")
        add_frame.pack(fill="x", expand="yes", padx= 20)

        med_id = Label(add_frame, text="ID")
        med_id.grid(row=0, column=0, padx= 10, pady= 5)

        med_name = Label(add_frame, text="Name")
        med_name.grid(row=0, column = 1, padx= 10, pady= 5)

        med_quantity = Label(add_frame, text="Quantity")
        med_quantity.grid(row=0, column = 2, padx= 10, pady= 5)

        med_price = Label(add_frame, text="Price/box")
        med_price.grid(row=0, column = 3, padx= 10, pady= 5)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Medicine ID
        med_id_box = Entry(add_frame)
        med_id_box.grid(row=1, column=0, padx= 10, pady= 5)

        # Medicine Name
        med_name_box = Entry(add_frame)
        med_name_box.grid(row=1, column=1, padx= 10, pady= 5)

        # Medicine Quantity
        med_quantity_box = Entry(add_frame)
        med_quantity_box.grid(row=1, column=2, padx= 10, pady= 5)
        # Medicine Price
        med_price_box = Entry(add_frame)
        med_price_box.grid(row=1, column=3, padx= 10, pady= 5)

        # Select Record
        def select_record1(e):
            # Clear boxes
            med_id_box.delete(0, END)
            med_name_box.delete(0, END)
            med_quantity_box.delete(0, END)
            med_price_box.delete(0, END)

            # Grab record Number
            selected = my_tree1.focus()

            # Grab record values
            values = my_tree1.item(selected, 'values')

            # Output to entry boxes
            med_id_box.insert(0, values[0])
            med_name_box.insert(0, values[1])
            med_quantity_box.insert(0, values[2])
            med_price_box.insert(0, values[3])

        # Update Record 
        def update_record1():
            
            #Grab the record Number
            selected = my_tree1.focus()

            # Update record
            my_tree1.item(selected, text='', values=(med_id_box.get(),med_name_box.get(),med_quantity_box.get(),med_price_box.get()))

            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            c.execute("""UPDATE medicines SET
                    med_id = :med_id
                    med_name = :med_name,
                    med_quantity = :med_quantity
                    med_price = :med_price
                   
                    WHERE med_id = :med_id""",
                    {   
                        'med_id' : med_id_box.get(),
                        'med_name': med_name_box.get(),
                        'med_quantity' : med_quantity.get(),
                        'med_price' : med_price_box.get()
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
            c.execute("INSERT INTO medicines (med_name, med_quantity, med_price) Values (:med_name, :med_quantity, :med_price)",
            {   
                'med_name' : med_name_box.get(),
                'med_quantity' : med_quantity_box.get(),
                'med_price' : med_price_box.get()
            }
            )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()
           
            # Clear boxes
            med_id_box.delete(0, END)
            med_name_box.delete(0, END)
           
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
            c.execute("SELECT * FROM medicines")
            records = c.fetchall()
            
            # Loop Thru Results
            global count
            count = 0
            for record in records:
                if count % 2 == 0:
                    my_tree1.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3]) , tags= ("evenrow",))              
                else:
                    my_tree1.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2], record[3]) , tags= ("oddrow",))
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

        btn_frame1 = LabelFrame(win, text= "Medicine Command")
        btn_frame1.pack(fill ="x", expand="yes", padx=20)

        # Buttons
        add_record1 = Button(btn_frame1, text="Add Record", command= add_record1)
        add_record1.grid(row= 0 , column= 0, padx= 10, pady= 5)

        # Update Records
        update_record1 = Button(btn_frame1, text = "Update Record", command= update_record1)
        update_record1.grid(row = 0, column= 1, padx= 10, pady= 5)

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
        #============================================= Bills =================================================
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
        my_tree2['columns'] = ("ID", "Values", "Patient ID")

        # Formate our columns
        my_tree2.column("#0", width = 0, stretch = NO)
        my_tree2.column("ID", anchor = W, width =100)
        my_tree2.column("Values", anchor = CENTER, width = 100)
        my_tree2.column("Patient ID", anchor = W, width = 100)
     

        # Create Headings
        my_tree2.heading("#0", text = "", anchor = CENTER)
        my_tree2.heading("ID", text = "ID", anchor=CENTER)
        my_tree2.heading("Values", text = "Values", anchor=CENTER)
        my_tree2.heading("Patient ID", text = "Patient ID", anchor=CENTER)
      
        # Create striped row tags
        my_tree2.tag_configure("oddrow", background= "white")
        my_tree2.tag_configure("evenrow", background= "lightblue")

        my_tree2.pack(pady= 5 )


        add_frame2 = LabelFrame(win, text= "Bill Record")
        add_frame2.pack(fill="x", expand="yes", padx= 20)

        bill_id = Label(add_frame2, text="ID")
        bill_id.grid(row=0, column=0)

        bill_values = Label(add_frame2, text="Values")
        bill_values.grid(row=0, column = 1)

        patient_id = Label(add_frame2, text = "Patient ID")
        patient_id.grid(row=0, column = 2)

        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Bill ID
        bill_id_box = Entry(add_frame2)
        bill_id_box.grid(row=1, column=0, padx= 10, pady= 5)

        # Bill Values
        bill_values_box = Entry(add_frame2)
        bill_values_box.grid(row=1, column=1, padx= 10, pady= 5)

        # Patient ID
        patient_id_box = Entry(add_frame2)
        patient_id_box.grid(row=1, column=2, padx= 10, pady= 5)
       
        # Select Record
        def select_record2(e):
            # Clear boxes
            bill_id_box.delete(0, END)
            bill_values_box.delete(0, END)
            patient_id_box.delete(0, END)

            # Grab record Number
            selected = my_tree2.focus()

            # Grab record values
            values = my_tree2.item(selected, 'values')

            # Output to entry boxes
            bill_id_box.insert(0, values[0])
            bill_values_box.insert(0, values[1])
            patient_id_box.insert(0, values[2])


        # Update Record 
        def update_record2():
            
            #Grab the record Number
            selected = my_tree2.focus()

            # Update record
            my_tree2.item(selected, text='', values=(bill_id_box.get(),bill_values_box.get(), patient_id_box.get()))

            # Create a database or connect to one
            conn = sqlite3.connect("hospital.db")

            # Create cursor
            c = conn.cursor()

            # Still lack of foreign key!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            c.execute("""UPDATE bills SET
                    bill_id = :bill_id,
                    bill_values = :bill_values,
                    bill_p_id = :bill_p_id
                
                    WHERE bill_id = :bill_id""",
                    {   
                        'bill_id' : bill_id_box.get(),
                        'bill_values': bill_values_box.get(),
                        'bill_p_id' : patient_id_box.get(),
                        
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
            c.execute("INSERT INTO bills (bill_values, bill_p_id) Values (:bill_values, :bill_p_id)",
            {   
                'bill_values' : bill_values_box.get(),
                'bill_p_id' : patient_id_box.get(),
              
            }
            )

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()


            # Clear boxes
            bill_id_box.delete(0, END)
            bill_values_box.delete(0, END)
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
            c.execute("SELECT * FROM bills")
            records = c.fetchall()
            
            # Loop Thru Results
            global count
            count = 0
            for record in records:
                if count % 2 == 0:
                    my_tree2.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2]) , tags= ("evenrow",))              
                else:
                    my_tree2.insert(parent='', index='end', iid= count , text=f'count', values=(record[0], record[1], record[2]) , tags= ("oddrow",))
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
        
        # Buttons frame
        btn_frame2 = LabelFrame(win, text= "Bill Command")
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
