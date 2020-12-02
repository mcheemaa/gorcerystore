#import modules
 
from tkinter import *

import os
import sqlite3
from sqlite3 import Error
import csv
from datetime import datetime
from PIL import ImageTk, Image

now = datetime.now() 

 
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("720x620")

    im = Image.open("/Users/mcheema/final_database/Images/groc.jpeg")
    img_fin = ImageTk.PhotoImage(im)

    register_screen.photo = img_fin

    background_label = Label(register_screen, image = img_fin)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
 
    global firstName
    global lastName
    global cpasscode
    global password
    global email
    global address
    global zipcode
    global city
    global phone
    
    firstName = StringVar()
    lastName = StringVar()
    cpasscode = StringVar()
    password = StringVar()
    email = StringVar()
    address = StringVar()
    zipcode = StringVar()
    city = StringVar()
    phone = StringVar()

    Label(register_screen, text="Please enter the details below ", font=("calibri", 12)).pack()
    Label(register_screen, text="").pack()
    firstName_lable = Label(register_screen, text="First Name * ")
    firstName_lable.pack()
    firstName_entry = Entry(register_screen, textvariable = firstName)
    firstName_entry.pack()
    

    lastName_lable = Label(register_screen, text="Last Name * ")
    lastName_lable.pack()
    lastName_entry = Entry(register_screen, textvariable = lastName)
    lastName_entry.pack()

    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable = email)
    email_entry.pack()

    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable = password, show = '*')
    password_entry.pack()
    
    cpasscode_lable = Label(register_screen, text="Passcode * ")
    cpasscode_lable.pack()
    cpasscode_entry = Entry(register_screen, textvariable = cpasscode)
    cpasscode_entry.pack()

    address_lable = Label(register_screen, text="Address * ")
    address_lable.pack()
    address_entry = Entry(register_screen, textvariable = address)
    address_entry.pack()
    
    zipcode_lable = Label(register_screen, text="Zipcode * ")
    zipcode_lable.pack()
    zipcode_entry = Entry(register_screen, textvariable = zipcode)
    zipcode_entry.pack()
    
    city_lable = Label(register_screen, text="City * ")
    city_lable.pack()
    city_entry = Entry(register_screen, textvariable = city)
    city_entry.pack()
    
    phone_lable = Label(register_screen, text="Phone * ")
    phone_lable.pack()
    phone_entry = Entry(register_screen, textvariable = phone)
    phone_entry.pack()
    
    
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():


    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("720x620")

    im = Image.open("/Users/mcheema/final_database/Images/groc.jpeg")
    img_fin = ImageTk.PhotoImage(im)

    login_screen.photo = img_fin

    background_label = Label(login_screen, image = img_fin)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
 

    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global email_verify
    global password_verify
 
    email_verify = StringVar()
    password_verify = StringVar()
 
    global email_login_entry
    global password_login_entry
 
    Label(login_screen, text="Email * ").pack()
    email_login_entry = Entry(login_screen, textvariable=email_verify)
    email_login_entry.pack()


    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
 
def register_user():

    firstName_val = firstName.get()
    lastName_val = lastName.get()
    cpasscode_val = cpasscode.get()
    password_val = password.get()
    email_val = email.get()
    address_val = address.get()
    zipcode_val = zipcode.get()
    city_val = city.get()
    phone_val = phone.get()

    joined = now.strftime("%m/%d/%Y")


    with sqlite3.connect('smgroceries.db') as conn:
            cur = conn.cursor()
            
            try:
                conn.execute('''
                INSERT INTO Customers (cid, firstName, lastName, cpasscode, password, email, address, zipcode, city, phone, cjoined)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
                ''',
                (502, firstName_val, lastName_val, cpasscode_val, password_val, email_val, address_val, zipcode_val, city_val, phone_val, joined))

                conn.commit() 

                Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

            except:
                conn.rollback()
                Label(register_screen, text="Registration Failed", fg="green", font=("calibri", 11)).pack()


 
 
def login_verify():

    password_val = password_verify.get()
    email_val = email_verify.get()

    email_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    conn = sqlite3.connect('smgroceries.db')
    cur = conn.cursor()
    cur.execute("select email, password from Customers where email = '"+email_val+"'")
    user = cur.fetchall()
    #print(user)
    
    
    for i in user:
        #print(i[0], " ", i[1])
        if email_val == i[0] and password_val == i[1]:
            login_sucess()
        else:
            password_not_recognised() 
 
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="Start Shopping", command=frontpage).pack()
 
def frontpage():


    global displaypage
    displaypage = Toplevel(login_screen)
    displaypage.title("Samit & Muhammad's Grocery Store ")
    displaypage.geometry("720x620")

    im = Image.open("/Users/mcheema/final_database/Images/inside.jpg")
    img_fin = ImageTk.PhotoImage(im)

    displaypage.photo = img_fin

    background_label = Label(displaypage, image = img_fin)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)



    '''beerimg = Image.open("/Users/mcheema/final_database/Images/beer.png")
    beerres = beerimg.resize((250, 250), Image.ANTIALIAS)
    fin = ImageTk.PhotoImage(beerres)
    displaypage.photo = fin'''

    conn = sqlite3.connect('smgroceries.db')
    cur = conn.cursor()
    cur.execute("select catName from Categories")
    user = cur.fetchall()
    #print(user)

    #for i in user:

    Label(displaypage, text="").pack()
    Button(displaypage, text= "Beer, Wine & Spirits Section", command = beer).pack()

    Label(displaypage, text="").pack()
    Button(displaypage, text= "Bread & Bakery Section", command = bread).pack()

    Label(displaypage, text="").pack()
    Button(displaypage, text= "Canned Goods & Soups Section", command = canned).pack()

    Label(displaypage, text="").pack()
    Button(displaypage, text= "Cookies, Snacks & Candy Section", command = cookies).pack()

    Label(displaypage, text="").pack()
    Button(displaypage, text= "Flowers Section", command = flowers).pack()


    Label(displaypage, text="").pack()
    Button(displaypage, text= "Meat & Seafood Section", command = meat).pack()

    Label(displaypage, text="").pack()
    Button(displaypage, text= "Produce: Fruits & Vegetables Section", command = produce).pack()

    Label(displaypage, text="").pack()
    Button(displaypage, text= "Pet Care Section", command = pet).pack()

def beer():

    global beersec
    beersec = Toplevel(displaypage)
    beersec.title("Beer, Wine & Spirits Section ")
    beersec.geometry("720x620")


    beerimg = Image.open("/Users/mcheema/final_database/Images/miller.jpg")
    fin = ImageTk.PhotoImage(beerimg)
    beersec.photo = fin

    background_label = Label(beersec, image = fin)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    conn = sqlite3.connect('smgroceries.db')
    cur = conn.cursor()
    cur.execute("select * from Products")
    user = cur.fetchall()
    
    cur.execute("select catid from Categories where catName == 'Beer, Wine & Spirits'")
    check = cur.fetchall()
    cat_id = check[0][0]
    
    for i in user:
        if i[6] == cat_id:
            Label(beersec, text="").pack()
            #print(i[1])
            name = i[1]
            Button(beersec, text= i[1] + "  Price: " + str(i[2]) + " \nDesc: " + i[3]).pack()

    



def description(pNam):
    
    global desc
    desc = Toplevel(beersec)
    desc.title(pNam)
    desc.geometry("600x200")

    conn = sqlite3.connect('smgroceries.db')
    cur = conn.cursor()
    cur.execute("select * from Products")
    user = cur.fetchall()
    

    print (pNam)

    return



def bread():
    global breadsec
    breadsec = Toplevel(displaypage)
    breadsec.title("Bread & Bakery Section ")
    breadsec.geometry("720x620")


    breadimg = Image.open("/Users/mcheema/final_database/Images/bread.jpg")
    fin = ImageTk.PhotoImage(breadimg)
    breadsec.photo = fin

    background_label = Label(breadsec, image = fin)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    conn = sqlite3.connect('smgroceries.db')
    cur = conn.cursor()
    cur.execute("select * from Products")
    user = cur.fetchall()
    
    cur.execute("select catid from Categories where catName == 'Bread & Bakery'")
    check = cur.fetchall()
    cat_id = check[0][0]
    
    for i in user:
        if i[6] == cat_id:
            Label(breadsec, text="").pack()
            #print(i[1])
            name = i[1]
            Button(breadsec, text= i[1] + "  Price: " + str(i[2]) + " \nDesc: " + i[3]).pack()

    

    return
def canned():
    global cannedsec
    cannedsec = Toplevel(displaypage)
    cannedsec.title("Canned Goods & Soups Section ")
    cannedsec.geometry("720x620")


    cannedimg = Image.open("/Users/mcheema/final_database/Images/canned.jpg")
    fin = ImageTk.PhotoImage(cannedimg)
    breadsec.photo = fin

    background_label = Label(cannedsec, image = fin)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    conn = sqlite3.connect('smgroceries.db')
    cur = conn.cursor()
    cur.execute("select * from Products")
    user = cur.fetchall()
    
    cur.execute("select catid from Categories where catName == 'Canned Goods & Soups'")
    check = cur.fetchall()
    cat_id = check[0][0]
    
    for i in user:
        if i[6] == cat_id:
            Label(cannedsec, text="").pack()
            #print(i[1])
            name = i[1]
            Button(cannedsec, text= i[1] + "  Price: " + str(i[2]) + " \nDesc: " + i[3]).pack()

def cookies():
    global coksec
    coksec = Toplevel(displaypage)
    coksec.title("Cookies, Snacks & Candy Section ")
    coksec.geometry("720x620")


    cokimg = Image.open("/Users/mcheema/final_database/Images/cookies.jpg")
    fin = ImageTk.PhotoImage(cokimg)
    coksec.photo = fin

    background_label = Label(coksec, image = fin)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    conn = sqlite3.connect('smgroceries.db')
    cur = conn.cursor()
    cur.execute("select * from Products")
    user = cur.fetchall()
    
    cur.execute("select catid from Categories where catName == 'Cookies, Snacks & Candy'")
    check = cur.fetchall()
    cat_id = check[0][0]
    
    for i in user:
        if i[6] == cat_id:
            Label(coksec, text="").pack()
            #print(i[1])
            name = i[1]
            Button(coksec, text= i[1] + "  Price: " + str(i[2]) + " \nDesc: " + i[3]).pack()

def flowers():
    return
def meat():
    return

def produce():
    return

def pet():
    return





def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 

 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("720x620")
    main_screen.title("Samit & Muhammad's Grocery Store ")

    im = Image.open("/Users/mcheema/final_database/Images/groc.jpeg")
    img_fin = ImageTk.PhotoImage(im)

    main_screen.photo = img_fin

    background_label = Label(main_screen, image = img_fin)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
   
    Label(main_screen, text="Please Sign In Or Register ", bg="blue", width="300", height="2", font=("Calibri", 18)).pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", height="2", width="30", command = login).pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
