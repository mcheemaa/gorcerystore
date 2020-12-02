
import sqlite3
from sqlite3 import Error
import csv

import pandas as pd

def db_connect():
    
    
    conn = None
    try:
        conn = sqlite3.connect("smgroceries.db")
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table):
    
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as e:
        print(e)


def main():
    

    customers = '''CREATE TABLE IF NOT EXISTS Customers (
                                    cid INTEGER PRIMARY KEY autoincrement,
                                    firstName TEXT,
                                    lastName TEXT,
                                    cpasscode TEXT,
                                    password TEXT,
		                            email TEXT unique,
		                            address TEXT,
		                            zipcode TEXT,
		                            city TEXT,
                                    phone TEXT,
                                    cjoined NVARCHAR(50) NOT NULL
                                    );'''


    categories = '''CREATE TABLE IF NOT EXISTS Categories (
                                    catid INTEGER PRIMARY KEY,
                                    catName TEXT,
                                    image TEXT
                                    );'''


    products = '''CREATE TABLE IF NOT EXISTS Products (
                                    pid INTEGER PRIMARY KEY autoincrement,
                                    pName TEXT,
                                    price REAL,
                                    description TEXT,
                                    image TEXT,
		                            stock INTEGER,
		                            catid INTEGER,
                                    FOREIGN KEY(catid) REFERENCES categories(catid)
                                    );'''


    customer_cart = '''CREATE TABLE IF NOT EXISTS Cart (
                                    cid integer PRIMARY KEY,
                                    pid INTEGER,
                                    quantity INTEGER,
                                    FOREIGN KEY(cid) REFERENCES Customers(cid),
                                    FOREIGN KEY(pid) REFERENCES Products(pid)
                                    );'''


    # create a database connection
    conn = db_connect()

    # create tables
    if conn is not None:
        # create customers table
        create_table(conn, customers)

        # create categories table
        create_table(conn, categories)

        # create products table
        create_table(conn, products)

        # create customer_cart table
        create_table(conn, customer_cart)

    else:
        print("Error! cannot create the database connection.")


    '''data = pd.read_csv ('products_data.csv')   
    dataf = pd.DataFrame(data, columns= ['pName', 'price', 'description', 'image', 'stock', 'catid'])

    cust = 0

    for row in dataf.itertuples():
        conn.execute(' INSERT INTO Products (pid, pName, price, description, image, stock, catid) VALUES (?,?,?,?,?,?,?)', (cust, 
        row.pName,
        row.price, row.description, row.image, row.stock, row.catid)) 
        cust = cust + 1
        conn.commit()'''



    '''for row in dataf.itertuples():
        conn.execute(' INSERT INTO Categories (catid, catName, image) VALUES (?,?,?)', (cust, row.catName, row.image)) 
        cust = cust + 1
        conn.commit()'''

    ''' for row in dataf.itertuples():
        conn.execute('
                INSERT INTO Customers (cid, firstName, lastName, cpasscode, password, email, address, zipcode, city, phone, cjoined)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
                ',
                (cust,
                row.firstName, 
                row.lastName,
                row.cpasscode,
                row.password,
                row.email,
                row.address,
                row.zipcode,
                row.city,
                row.phone,
                row.cjoined)
                )

        cust = cust + 1
        conn.commit() '''

if __name__ == '__main__':
    main()