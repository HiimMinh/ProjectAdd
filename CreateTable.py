from tkinter import *
from tkinter.ttk import *
import sqlite3

# Databases

# Create a database or connect to one
conn = sqlite3.connect("hospital.db")

# Create cursor
c = conn.cursor()

# Create Patient table
# p_id = oid
c.execute("""CREATE TABLE patients (
    p_id INTEGER PRIMARY KEY AUTOINCREMENT,            
    p_name text,
    p_dob text,
    p_sex text,
    p_address text,
    p_ill text

)
        """)

# Create Doctor table
# doc_id = oid
c.execute("""CREATE TABLE doctors (
    doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_name text,
    doc_dob text,
    doc_sex text,
    doc_major text,
    doc_salary integer

)
        """)

# Create Nurse table
# nur_id = oid
c.execute("""CREATE TABLE nurses (
    nur_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nur_name text,
    nur_dob text,
    nur_sex text,
    nur_salary integer,
    doc_id

)
        """)

# Create Room table
c.execute("""CREATE TABLE rooms (
    r_id INTEGER PRIMARY KEY AUTOINCREMENT,
    r_name text
    
)
        """)

# Create Bed table
c.execute("""CREATE TABLE bed (
    b_id INTEGER PRIMARY KEY AUTOINCREMENT,
    

    r_name text

)
        """)

# Create Bill table
c.execute("""CREATE TABLE bills (
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_values integer,
    p_id integer

)
        """)

# Create Medicine table
c.execute("""CREATE TABLE medicines (
   m_name text,
   m_quantity integer,
   m_values integer

)
        """)

# Create Doctor Service Times table
c.execute("""CREATE TABLE doc_ser_times (
    doc_id integer,
    p_id integer,
    service_times integer

)
        """)

# Create Nurse Service Times table
c.execute("""CREATE TABLE nur_ser_times (
    nur_id integer,
    p_id integer,
    service_times integer

)
        """)

# Create Nurse Work Times table
c.execute("""CREATE TABLE nur_work_times (
    nur_id integer,
    r_id integer,
    r_name text

)
        """)


