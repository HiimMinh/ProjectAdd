from tkinter import *
from tkinter.ttk import *
import sqlite3

# Databases

# Create a database or connect to one
conn = sqlite3.connect("hospital.db")

# Create cursor
c = conn.cursor()

# Create Patient table
c.execute("""CREATE TABLE IF NOT EXISTS patients (
    p_id INTEGER PRIMARY KEY AUTOINCREMENT,            
    p_name TEXT NOT NULL,
    p_dob TEXT NULL,
    p_sex TEXT,
    p_address NULL,
    p_ill NOT NULL

)
        """)

# Create Doctor table
c.execute("""CREATE TABLE IF NOT EXISTS doctors (
    doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_name TEXT NOT NULL,
    doc_dob TEXT NULL,
    doc_sex TEXT,
    doc_major NOT NULL,
    doc_salary INTEGER NULL

)
        """)

# Create Nurse table
c.execute("""CREATE TABLE IF NOT EXISTS nurses (
    nur_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nur_name TEXT NOT NULL,
    nur_dob TEXT NULL,
    nur_sex TEXT,
    nur_salary INTEGER NULL,
    docsp_id INTEGER NOT NULL,
    FOREIGN KEY (docsp_id)
        REFERENCES doctors(doc_id) 
                ON UPDATE CASCADE 
                ON DELETE CASCADE
  
        )
        """);

# Create Room table
c.execute("""CREATE TABLE IF NOT EXISTS rooms (
    r_id INTEGER PRIMARY KEY AUTOINCREMENT,
    r_name TEXT NOT NULL
    
)
        """)

# Create Bed table
c.execute("""CREATE TABLE IF NOT EXISTS beds (
    bed_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bed_r_name TEXT NOT NULL,
    bed_r_id INTEGER NOT NULL,
    bed_p_id INTEGER NOT NULL,
    FOREIGN KEY (bed_r_name)
        REFERENCES rooms (r_name)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    FOREIGN KEY (bed_r_id)
        REFERENCES rooms (r_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    FOREIGN KEY (bed_p_id)
        REFERENCES patients (p_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE 
        )     
        """)

# Create Bill table
c.execute("""CREATE TABLE IF NOT EXISTS bills (
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_values INTEGER,
    bill_p_id INTEGER NOT NULL,
    FOREIGN KEY (bill_p_id)
        REFERENCES patients (p_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE

)
        """)

# Create Medicine table
c.execute("""CREATE TABLE IF NOT EXISTS medicines (
   med_id INTEGER PRIMARY KEY NOT NULL,
   med_name TEXT NOT NULL,
   med_quantity INTEGER NOT NULL,
   med_price INTEGER NOT NULL

)
        """)

# Create Doctor Service Times table
c.execute("""CREATE TABLE IF NOT EXISTS doc_ser_times (
    doc_ser_id INTEGER NOT NULL,
    doc_ser_p_id INTEGER NOT NULL,
    doc_ser_times INTEGER NULL,
    FOREIGN KEY (doc_ser_id) 
        REFERENCES doctors (doc_id) 
                ON UPDATE CASCADE 
                ON DELETE CASCADE,               
    FOREIGN KEY (doc_ser_p_id)
        REFERENCES patients (p_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE

                )
        """)

# Create Nurse Service Times table
c.execute("""CREATE TABLE IF NOT EXISTS nur_ser_times (
    nur_ser_id INTEGER NOT NULL,
    nur_ser_p_id INTEGER NOT NULL,
    nur_service_times INTEGER NULL,
    FOREIGN KEY (nur_ser_id)
        REFERENCES nurses (nur_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    FOREIGN KEY (nur_ser_p_id)
        REFERENCES patients (p_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE

)
        """)

# Create Nurse Work Times table
c.execute("""CREATE TABLE IF NOT EXISTS nur_work_times (
    nur_work_id INTEGER NOT NULL,
    nur_r_id INTEGER NOT NULL,
    FOREIGN KEY (nur_work_id)
        REFERENCES nurses (nur_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    FOREIGN KEY (nur_r_id)
        REFERENCES rooms (r_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE

)
        """)


