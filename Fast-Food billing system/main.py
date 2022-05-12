from tkinter import *
from data import *
from tkinter import ttk
from datetime import datetime
import random
from PIL import ImageTk, Image
import os
import tkinter.font as font
import unittest

selected_items = []
r = random.randint(10000, 999999)


#button styling :hover
def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))






# Showing the list of deleted items
def saldellist(tree):
    tree.delete(*tree.get_children())
    rows = get_all_deleted()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3]))


# View deleted bills
def deleted_bills(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    tree = ttk.Treeview(t)
    labelFont1 = font.Font(family='Courier New bold', size=25)
    labelFont2 = font.Font(family='Courier New bold', size=20)
    buttonFont = font.Font(family='Verdana', size=10, weight='bold')
    b = Button(t, text="SHOW", command=lambda: saldellist(
        tree), fg="white", bg="#027FBE")
    lname = Label(t, text="LIST OF BILLS DELETED", fg="white", bg="#212121")
    tree["columns"] = ("one", "two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("one", text="EMPLOYEE ID")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    tree.column("three", anchor=CENTER)
    b.pack()
    tree.pack()
    
    b.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=2, width=6)
    lname.config(font=labelFont1,padx=6,anchor="center",pady=3, bd=2, width=20)
    b.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    tree.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    lname.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    changeOnHover(b,"#004CAF", "#027FBE")
    return t


# Check and delete bill
def delete_bill(ref):
    if ref and ref.isnumeric():
        delete_bill_db(int(ref))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Showing the list of sales for specific user
def sal_del(tree, username):
    tree.delete(*tree.get_children())
    rows = get_all_sales_related(int(username))
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[2], i[3]))


# Remove and check bill page
def remove_bill(tab_main, username):
    buttonFont = font.Font(family='Verdana', size=10, weight='bold')
    t = Frame(tab_main, background="#D9D7BE")
    l = Label(t, text="ENTER REFNO:", fg="white", bg="#212121")
    e = Entry(t)
    b1 = Button(t, text="DELETE", fg="white", bg="#027FBE",
               command=lambda: delete_bill(e.get()))
    l.pack()
    e.pack()
    b1.pack()
    tree = ttk.Treeview(t)
    tree["columns"] = ("two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    tree.column("three", anchor=CENTER)
    b2 = Button(t, text="SHOW", command=lambda: sal_del(
        tree, username), fg="white", bg="#027FBE")
    b2.pack()
    tree.pack()
    b1.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=4, width=6)
    b1.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    tree.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    l.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    e.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    b2.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=4, width=3)
    b2.place(relx = 0.63, rely = 0.2, anchor = CENTER)
    changeOnHover(b1,"#B20000", "#027FBE")
    changeOnHover(b2,"#004CAF", "#027FBE")
    
    return t


# Check and edit price
def ck_and_edit_price(item, price):
    if item and price.isnumeric():
        update_price(item, int(price))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Change price of item
def change_price_of_item(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    rows = get_items()
    options = []
    for i in rows:
        options.append(i[1])
    clicked = StringVar()
    if(len(options)):
        clicked.set(options[0])
        drop = OptionMenu(t, clicked, *options)
        l = Label(t, text="ENTER NEW PRICE:", fg="white", bg="#212121")
        c = Entry(t)
        b = Button(t, text="UPDATE PRICE", command=lambda: ck_and_edit_price(
            clicked.get(), c.get()), fg="white", bg="#1966ff")
        drop.pack()
        l.pack()
        c.pack()
        b.pack()
    return t


# Check and delete item
def exec_del_item(iid):
    if iid.isnumeric():
        remove_item(int(iid))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Delete item
'''def delete_item(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    l1 = Label(t, text="Enter item id: ", fg="white", bg="#212121")
    e1 = Entry(t)
    b = Button(t, text="REMOVE", command=lambda: exec_del_item(
        e1.get()), fg="white", bg="#1966ff")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    b.grid(row=2, column=1)
    return t'''


# Check and delete employee
def exec_del_user(uid):
    if uid.isnumeric():
        remove_user(int(uid))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Delete employee
'''def delete_user(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    l1 = Label(t, text="Enter user id: ", fg="white", bg="#212121")
    e1 = Entry(t)
    b = Button(t, text="REMOVE", command=lambda: exec_del_user(
        e1.get()), fg="white", bg="#1966ff")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    b.grid(row=2, column=1)
    return t'''


# Validate and add item
def ck_and_add_item(itemid, name, cost):
    row = ck_item_exists(itemid)
    if name and itemid.isnumeric() and cost.isnumeric() and row == None:
        add_item_to_db_data(int(itemid), name, int(cost))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Add items to database
'''def add_item_to_db(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    l1 = Label(t, text="Enter item id: ", fg="white", bg="#212121")
    e1 = Entry(t)
    l2 = Label(t, text="Enter name: ", fg="white", bg="#212121")
    e2 = Entry(t)
    l3 = Label(t, text="Enter cost: ", fg="white", bg="#212121")
    e3 = Entry(t)
    b = Button(t, text="ADD", command=lambda: ck_and_add_item(e1.get(), e2.get(), e3.get()),
               fg="white", bg="#1966ff")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    b.grid(row=4, column=1)
    return t'''


# Showing the list of items
def show_item_list(tree):
    tree.delete(*tree.get_children())
    rows = get_items()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2]))


# List items
def list_items(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    tree = ttk.Treeview(t)
    labelFont1 = font.Font(family='Courier New bold', size=25)
    labelFont2 = font.Font(family='Courier New bold', size=20)
    
    buttonFont = font.Font(family='Verdana', size=10, weight='bold')
    b1 = Button(t, text="SHOW", command=lambda: show_item_list(
        tree), fg="white", bg="#027FBE")
    tree["columns"] = ("one", "two")
    tree.heading("#0", text="ID")
    tree.heading("one", text="NAME")
    tree.heading("two", text="COST")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    lname1 = Label(t, text="MENU", fg="white", bg="#212121")
    

    
    
    lname1.pack()
    b1.pack()
    tree.pack()
    b1.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=2, width=6)
    lname1.config(font=labelFont1,padx=6,anchor="center",pady=3, bd=2, width=20)
    b1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    tree.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    lname1.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    changeOnHover(b1,"#004CAF", "#027FBE")
    
    #NEW ITEM
    l1 = Label(t, text="Enter item id: ", fg="white", bg="#212121")
    e1 = Entry(t)
    l2 = Label(t, text="Enter name: ", fg="white", bg="#212121")
    e2 = Entry(t)
    l3 = Label(t, text="Enter cost: ", fg="white", bg="#212121")
    e3 = Entry(t)
    b2 = Button(t, text="ADD", command=lambda: ck_and_add_item(e1.get(), e2.get(), e3.get()),
               fg="white", bg="#027FBE")
    lname2 = Label(t, text="ADD ITEM", fg="white", bg="#212121")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    b2.grid(row=4, column=1)
    b2.place(relx = 0.2, rely = 0.8, anchor = CENTER)
    l1.place(relx = 0.13, rely = 0.65, anchor = CENTER)
    l2.place(relx = 0.13, rely = 0.7, anchor = CENTER)
    l3.place(relx = 0.13, rely = 0.75, anchor = CENTER)
    e1.place(relx = 0.25, rely = 0.65, anchor = CENTER)
    e2.place(relx = 0.25, rely = 0.7, anchor = CENTER)
    e3.place(relx = 0.25, rely = 0.75, anchor = CENTER)
    lname2.place(relx = 0.2, rely = 0.6, anchor = CENTER)
    lname2.config(font=labelFont1,padx=6,anchor="center",pady=3, bd=2, width=10)
    changeOnHover(b2,"#004CAF", "#027FBE")
    
    #DELETE
    
    l4 = Label(t, text="Enter item id: ", fg="white", bg="#212121")
    e4 = Entry(t)
    b3 = Button(t, text="REMOVE", command=lambda: exec_del_item(
        e1.get()), fg="white", bg="#027FBE")
    lname3 = Label(t, text="DELETE ITEM", fg="white", bg="#212121")
    l4.grid(row=0, column=0)
    e4.grid(row=0, column=1)
    b3.grid(row=2, column=1)
    
    b3.place(relx = 0.6, rely = 0.7, anchor = CENTER)
    e4.place(relx = 0.65, rely = 0.65, anchor = CENTER)
    l4.place(relx = 0.53, rely = 0.65, anchor = CENTER)
    lname3.place(relx = 0.6, rely = 0.597, anchor = CENTER)
    lname3.config(font=labelFont1,padx=6,anchor="center",pady=3, bd=2, width=10)
    changeOnHover(b3,"#B20000", "#027FBE")
    
    return t


# Validate and add employee
def ck_and_add(username, name, password, phno):
    row = get_user_details(username)
    if name and password and username.isnumeric() and phno.isnumeric() and row == None:
        add_user_to_db(int(username), name, password, int(phno))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Add employee
'''def add_user(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    l1 = Label(t, text="Enter user id: ", fg="white", bg="#212121")
    e1 = Entry(t)
    l2 = Label(t, text="Enter name: ", fg="white", bg="#212121")
    e2 = Entry(t)
    l3 = Label(t, text="Enter user password: ", fg="white", bg="#212121")
    e3 = Entry(t)
    l4 = Label(t, text="Enter PHNO: ", fg="white", bg="#212121")
    e4 = Entry(t)
    b = Button(t, text="ADD", command=lambda: ck_and_add(e1.get(), e2.get(), e3.get(), e4.get()),
               fg="white", bg="#1966ff")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    l4.grid(row=3, column=0)
    e4.grid(row=3, column=1)
    b.grid(row=4, column=1)
    return t'''


# Showing the list of sales
def sal(tree):
    tree.delete(*tree.get_children())
    rows = get_all_sales()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3]))

# Showing the bills to employee    
def sal_emp(tree,username):
    tree.delete(*tree.get_children())
    rows = get_all_sales_emp(int(username))
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3]))


# List sales
def sales(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    tree = ttk.Treeview(t)
    b = Button(t, text="SHOW", command=lambda: sal(
        tree), fg="white", bg="#1966ff")
    tree["columns"] = ("one", "two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("one", text="EMPLOYEE ID")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    tree.column("three", anchor=CENTER)
    b.pack()
    tree.pack()
    return t


# Showing the list of employees
def s(tree):
    tree.delete(*tree.get_children())
    rows = get_all_employees()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[3]))


# List employees
def list_emp(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    tree = ttk.Treeview(t)
    labelFont1 = font.Font(family='Courier New bold', size=25)
    labelFont2 = font.Font(family='Courier New bold', size=20)
    
    buttonFont = font.Font(family='Verdana', size=10, weight='bold')
    b1 = Button(t, text="SHOW", command=lambda: s(
        tree), fg="white", bg="#027FBE")
    tree["columns"] = ("one", "two")
    tree.heading("#0", text="ID")
    tree.heading("one", text="NAME")
    tree.heading("two", text="PHNO")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    lname1 = Label(t, text="EMPLOYEE DETAILS", fg="white", bg="#212121")
    b1.pack()
    tree.pack()
    lname1.pack()
    b1.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=2, width=6)
    lname1.config(font=labelFont1,padx=6,anchor="center",pady=3, bd=2, width=20)
    b1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    tree.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    lname1.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    changeOnHover(b1,"#004CAF", "#027FBE")
    
    
    
    #ADD EMPLOYEE
    l1 = Label(t, text="Enter user id: ", fg="white", bg="#212121")
    e1 = Entry(t)
    l2 = Label(t, text="Enter name: ", fg="white", bg="#212121")
    e2 = Entry(t)
    l3 = Label(t, text="Enter user password: ", fg="white", bg="#212121")
    e3 = Entry(t)
    l4 = Label(t, text="Enter PHNO: ", fg="white", bg="#212121")
    e4 = Entry(t)
    b2 = Button(t, text="ADD", command=lambda: ck_and_add(e1.get(), e2.get(), e3.get(), e4.get()),
               fg="white", bg="#027FBE")
    lname2 = Label(t, text="ADD EMPLOYEE", fg="white", bg="#212121")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    l4.grid(row=3, column=0)
    e4.grid(row=3, column=1)
    b2.grid(row=4, column=1)
    b2.place(relx = 0.2, rely = 0.85, anchor = CENTER)
    l1.place(relx = 0.13, rely = 0.65, anchor = CENTER)
    l2.place(relx = 0.13, rely = 0.7, anchor = CENTER)
    l3.place(relx = 0.13, rely = 0.75, anchor = CENTER)
    l4.place(relx = 0.13, rely = 0.8, anchor = CENTER)
    e1.place(relx = 0.25, rely = 0.65, anchor = CENTER)
    e2.place(relx = 0.25, rely = 0.7, anchor = CENTER)
    e3.place(relx = 0.25, rely = 0.75, anchor = CENTER)
    e4.place(relx = 0.25, rely = 0.8, anchor = CENTER)
    lname2.place(relx = 0.2, rely = 0.6, anchor = CENTER)
    lname2.config(font=labelFont1,padx=6,anchor="center",pady=3, bd=2, width=13)
    changeOnHover(b2,"#004CAF", "#027FBE")
    
    
    
    
    #DELETE EMPLOYEE
    l5 = Label(t, text="Enter user id: ", fg="white", bg="#212121")
    e5 = Entry(t)
    b3 = Button(t, text="REMOVE", command=lambda: exec_del_user(
        e1.get()), fg="white", bg="#027FBE")
    lname3 = Label(t, text="DELETE EMPLOYEE", fg="white", bg="#212121")
    l5.grid(row=0, column=0)
    e5.grid(row=0, column=1)
    b3.grid(row=2, column=1)
    b3.place(relx = 0.6, rely = 0.7, anchor = CENTER)
    e5.place(relx = 0.65, rely = 0.65, anchor = CENTER)
    l5.place(relx = 0.53, rely = 0.65, anchor = CENTER)
    lname3.place(relx = 0.6, rely = 0.597, anchor = CENTER)
    lname3.config(font=labelFont1,padx=6,anchor="center",pady=3, bd=2, width=15)
    changeOnHover(b3,"#B20000", "#027FBE")
    
    return t


# Function for resetting the bill
def resetf():
    global selected_items
    global r
    selected_items.clear()
    r = random.randint(10000, 999999)


# Print/Show the bill
def get_bill(username):
    cost = 0
    items = []
    for i in selected_items:
        cost = cost+int(i[2])
        items.append(i[0])

    for i in range(len(selected_items)):
        cost=cost*selected_items[i][1]
                  
    tax = round(cost * 0.2, 2)
    service = round(cost/99, 2)
    total_cost = round(cost+tax+service)
   
    t = Toplevel()
    t.geometry("350x700")
    t.title("BILL")
    t.configure(bg="#212121")
    date = Label(t, text="DATE: " +
                 datetime.now().strftime("%d-%m-%Y"), fg="white", bg="#212121")
    time = Label(t, text="TIME: "+datetime.now().strftime("%H:%M"),
                 fg="white", bg="#212121")
    ref = Label(t, text="REF NO: "+str(r), fg="white", bg="#212121")
    emp = Label(t, text="EMPLOYEE ID: "+str(username),
                fg="white", bg="#212121")
    costl = Label(t, text="COST: "+str(cost), fg="white", bg="#212121")
    taxl = Label(t, text="TAX: "+str(tax), fg="white", bg="#212121")
    servicel = Label(t, text="SERVICE CHARGES: " +
                     str(service), fg="white", bg="#212121")
    total_costl = Label(t, text="TOTAL COST: " +
                        str(total_cost), fg="white", bg="#212121")
    date.pack()
    time.pack()
    ref.pack()
    emp.pack()
    costl.pack()
    taxl.pack()
    servicel.pack()
    total_costl.pack()
    Label(t, text="ITEMS:", fg="white", bg="#212121").pack()
    for it in range(len(selected_items)):
        Label(t, text=selected_items[it][0] + "( X "+str(
            selected_items[it][1])+" )", fg="white", bg="#212121").pack()
    if total_cost:
        store(datetime.now(), username, total_cost, r)
    return t


# Add items to the bill and diplay them
def add_item(item, itemno):
    cost = get_cost(item)
    selected_items.append((item, itemno, cost))
    tree.delete(*tree.get_children())
    for row in selected_items:
        tree.insert("", 0, text=row[0], values=(row[1], row[2]))
    return








#delete selected item from the bill
'''def delete1(tree):
    x=tree.selection()
    tree.delete(x) 
    print(x)
    for x in selected_items:
      selected_items.remove(x)'''
    
    
     

    

# Show the various items added to the bill when refresh is clicked
def two(tree):
    tree.delete(*tree.get_children())
    for row in selected_items:
        tree.insert('', 0, text=row[0], values=(row[1], row[2]))
        
        
        
        
# VIEW bills for employee
def show_items(tab_main, username):
    t = Frame(tab_main, background="#D9D7BE")
    tree = ttk.Treeview(t)
    labelFont1 = font.Font(family='Courier New bold', size=25)
    labelFont2 = font.Font(family='Courier New bold', size=20)
    data = get_user_details(int(username))
    buttonFont = font.Font(family='Verdana', size=10, weight='bold')
    b = Button(t, text="BILLS", command=lambda: sal_emp(
        tree,username), fg="white", bg="#1966ff")
    lname = Label(t, text="BILLS for "+data[1].capitalize(), fg="black", bg="#D9D7BE")
    lid = Label(t, text="ID: "+str(data[0]), fg="black", bg="#D9D7BE")
    tree["columns"] = ("one", "two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("one", text="EMPLOYEE ID")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    tree.column("three", anchor=CENTER)
    b.pack()
    tree.pack()
    lname.pack()
    lid.pack()
    
    b.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=2, width=6)
    lname.config(font=labelFont1,padx=6,anchor="center",pady=3, bd=2, width=20)
    lid.config(font=labelFont2,padx=6,anchor="center",pady=3, bd=2, width=20)
    b.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    tree.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    lname.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    lid.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    changeOnHover(b,"#004CAF", "#027FBE")
    
    return t


# Billing section
def bill(tab_main, username):
    
   
    buttonFont = font.Font(family='Verdana', size=10, weight='bold')
    labelFont = font.Font(family='Courier New bold', size=15)
    labelFont1 = font.Font(family='Verdana bold', size=11)
    t = Frame(tab_main, background="#D9D7BE")
    rows = get_items()
    
    options = []
    for i in rows:
        options.append(i[1])
    clicked = StringVar()
    if(len(options)):
        clicked.set(options[0])
        cl = IntVar()
        cl.set(1)
        drop = OptionMenu(t, clicked, *options)
        l = Label(t, text="SELECT ITEM:", fg="white", bg="#212121")
        q = OptionMenu(t, cl, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        l1 = Label(t, text="SELECT QUANTITY:", fg="white", bg="#212121")
        b = Button(t, text="ADD", command=lambda: add_item(
            clicked.get(), cl.get()), fg="white", bg="#00892F")
        reset = Button(t, text="RESET", command=lambda: resetf(),
                       fg="white", bg="blue")
        l.config(font=labelFont)
        l1.config(font=labelFont)
        drop.config(font=labelFont1,padx=30,anchor="center",pady=5, bd=5, width=10)
        q.config(font=labelFont1,padx=5,anchor="center",pady=3, bd=2, width=5)
        b.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=2, width=6)
        reset.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=2, width=6)
        drop.pack()
        l.pack()
        l1.pack()
        q.pack()
        b.pack()
        reset.pack()
        changeOnHover(b,"#00B63E", "#00892F")
        changeOnHover(reset,"#B20000", "blue")
        l.place(relx = 0.5, rely = 0.03, anchor = CENTER)
        drop.place(relx = 0.5, rely = 0.08, anchor = CENTER)
        l1.place(relx = 0.5, rely = 0.13, anchor = CENTER)
        q.place(relx = 0.5, rely = 0.18, anchor = CENTER)
        b.place(relx = 0.5, rely = 0.23, anchor = CENTER)
        reset.place(relx = 0.5, rely = 0.28, anchor = CENTER)
        
        #display selected items
        tree = ttk.Treeview(t)
        b1 = Button(t, text="REFRESH", command=lambda: two(
        tree), fg="white", bg="#027FBE")
        b2 = Button(t, text="SUBMIT", command=lambda: get_bill(
        username), fg="white", bg="#027FBE")
        clear = Button(t, text="CLEAR", command=lambda: resetf(),
                   fg="white", bg="#027FBE")
       # b_del = Button(t, text="DELETE", command=lambda: delete1(tree),
       #               fg="white", bg="#027FBE")
        tree["columns"] = ("one", "two")
        tree.heading("#0", text="ITEM NAME")
        tree.heading("one", text="QUANTITY")
        tree.heading("two", text="COST")
        tree.column("#0", anchor=CENTER)
        tree.column("one", anchor=CENTER)
        tree.column("two", anchor=CENTER)
        
        b1.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=4, width=6)
        b2.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=4, width=6)
        #b_del.config(font=labelFont,padx=6,anchor="center",pady=3, bd=4, width=6)
        clear.config(font=buttonFont,padx=6,anchor="center",pady=3, bd=4, width=6)
        
        changeOnHover(b1,"#004CAF", "#027FBE")
        changeOnHover(b2,"#004CAF", "#027FBE")
       # changeOnHover(b_del,"#004CAF", "#027FBE")
        changeOnHover(clear,"#B20000", "#027FBE")
        
        b1.pack()
        b2.pack()
        clear.pack()
        tree.pack()
        #b_del.pack()
        
        
        tree.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        b1.place(relx = 0.32, rely = 0.7, anchor = CENTER)
        b2.place(relx = 0.44, rely = 0.7, anchor = CENTER)
        clear.place(relx = 0.68, rely = 0.7, anchor = CENTER)
       # b_del.place(relx = 0.56, rely = 0.7, anchor = CENTER)
    return t


# Employee details
def user_details(tab_main, username):
    labelFont = font.Font(family='Courier New bold', size=35)
    t = Frame(tab_main, background="#D9D7BE")
    data = get_user_details(int(username))
    lname = Label(t, text="NAME: "+data[1], fg="black", bg="#D9D7BE")
    lid = Label(t, text="ID: "+str(data[0]), fg="black", bg="#D9D7BE")
    lphno = Label(t, text="PHNO: "+str(data[2]), fg="black", bg="#D9D7BE")
    lname.config(font=labelFont)
    lid.config(font=labelFont)
    lphno.config(font=labelFont)
    lname.pack()
    lid.pack()
    lphno.pack()
    img = ImageTk.PhotoImage(Image.open(r"D:\\Project code\\Proj code\\codes\\bill.jpg"))
    panel = Label(t, image=img)
    panel.photo = img
    panel.pack()
    return t


# Admin details
def admin_details(tab_main, username):
    labelFont = font.Font(family='Courier New bold', size=38)
    t = Frame(tab_main, background="#D9D7BE")
    data = get_admin_details(int(username))
    lname = Label(t, text="ADMIN NAME: "+data[1], fg="black", bg="#D9D7BE")
    lid = Label(t, text="ID: "+str(data[0]), fg="black", bg="#D9D7BE")
    lphno = Label(t, text="PHNO: "+str(data[2]), fg="black", bg="#D9D7BE")
    lname.config(font=labelFont)
    lid.config(font=labelFont)
    lphno.config(font=labelFont)
    lname.pack()
    lid.pack()
    lphno.pack()
    #img = ImageTk.PhotoImage(Image.open(r"billing system\img\admin.png"))
    panel = Label(t)
    #panel.photo = img
    panel.pack()
    return t


# POPUP for displaying errors
def popup(msg):
    pop = Toplevel()
    pop.geometry("200x60")
    MyLeftPos = (pop.winfo_screenwidth() - 200) / 2
    myTopPos = (pop.winfo_screenheight() - 60) / 2
    pop.geometry( "%dx%d+%d+%d" % (200, 60, MyLeftPos, myTopPos))
    pop.title("MESSAGE")
    pop.configure(bg="#212121")
    l = Label(pop, text=msg, fg="white", bg="#212121")
    exitb = Button(pop, text="OK", fg="white", bg="#1966ff",
                   command=lambda: pop.destroy())
    l.pack()
    exitb.pack()


# Employee dashboard
def ud(username):
    ud = Toplevel()
    tree = ttk.Treeview(ud)
    ul.destroy()
    root.iconify()
    ud.geometry("1000x800")
    MyLeftPos = (ud.winfo_screenwidth() - 1000) / 2
    myTopPos = (ud.winfo_screenheight() - 800) / 2
    ud.geometry( "%dx%d+%d+%d" % (1000, 800, MyLeftPos, myTopPos))
    data = get_user_details(int(username))
    ud.title("WELCOME "+ data[1].capitalize() +" -FAST FOOD CENTER")
    ud.configure(bg="#FFF")
    tab_main = ttk.Notebook(ud)
    t1 = user_details(tab_main, username)
    t2 = bill(tab_main, username)
    t3 = show_items(tab_main, username)
    t4 = remove_bill(tab_main, username)
    tab_main.add(t1, text="USER DETAILS")
    tab_main.add(t2, text="BILLING")
    tab_main.add(t3, text="VIEW BILL")
    tab_main.add(t4, text="REMOVE BILL")
    tab_main.pack(expand=1, fill='both')


# Admin dashboard
def ad(username):
    al.destroy()
    root.iconify()
    ad = Toplevel()
    MyLeftPos = (ad.winfo_screenwidth() - 1000) / 2
    myTopPos = (ad.winfo_screenheight() - 800) / 2
    ad.geometry( "%dx%d+%d+%d" % (1000, 800, MyLeftPos, myTopPos))
    data = get_admin_details(int(username))
    ad.title("ADMIN "+ data[1].capitalize() +" -FAST FOOD CENTER")
    ad.configure(bg="#212121")
    tab_main = ttk.Notebook(ad)
    t1 = admin_details(tab_main, username)
    t2 = list_emp(tab_main, username)
    t3 = sales(tab_main, username)
  
    t4 = list_items(tab_main, username)
    
    t5 = change_price_of_item(tab_main, username)
    
    t6 = deleted_bills(tab_main, username)
    
    tab_main.add(t1, text="ADMIN DETAILS")
    tab_main.add(t2, text="EMPLOYEE DETAILS")
    tab_main.add(t3, text="SALES")
    tab_main.add(t4, text="SHOW MENU")  
    tab_main.add(t5, text="CHANGE PRICE") 
    tab_main.add(t6, text="DELETED BILLS")
    tab_main.pack(expand=1, fill='both')


# Employee authentication
def user_auth(username, password):
    if username and password and username.isnumeric():
        if ck_details_emp(int(username), password):
            ud(username)
        else:
            popup("ERROR WRONG DETAILS")
    else:
        popup("ERROR WRONG DETAILS")


# Admin authentication
def admin_auth(username, password):
    
        if username and password and username.isnumeric():
             if ck_details_admin(int(username), password):
            
                 
                 ad(username)
             else:
                
               popup("ERROR WRONG DETAILS")   
        else:
            popup("ERROR WRONG DETAILS")      
                 
       
        
        
        


# Employee login
def user_login():
    global ul
    ul = Toplevel()
    MyLeftPos = (ul.winfo_screenwidth() - 250) / 2
    myTopPos = (ul.winfo_screenheight() - 100) / 2
    ul.geometry( "%dx%d+%d+%d" % (250, 100, MyLeftPos, myTopPos))
    ul.title("EMPLOYEE LOGIN")
    ul.configure(bg="#212121")
    l1 = Label(ul, text="ID: ", fg="white", bg="#212121")
    e1 = Entry(ul)
    l2 = Label(ul, text=" PASSWORD: ", fg="white", bg="#212121")
    e2 = Entry(ul, show="*")
    lb = Button(ul, text="LOGIN", fg="white", bg="#1500AB",
                command=lambda: user_auth(e1.get(), e2.get()))
   
    changeOnHover(lb,"#00B63E", "#1500AB")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    lb.grid(row=2, column=1)
    lb.place(relx = 0.5, rely = 0.6, anchor = CENTER)




# Admin login
def admin_login():
  
    global al
    al = Toplevel()
    MyLeftPos = (al.winfo_screenwidth() - 250) / 2
    myTopPos = (al.winfo_screenheight() - 100) / 2
    al.geometry( "%dx%d+%d+%d" % (250, 100, MyLeftPos, myTopPos))
    al.title("ADMIN LOGIN")
    al.configure(bg="#212121")
    l1 = Label(al, text="ID : ", fg="white", bg="#1500AB")
   
    e1 = Entry(al)
    l2 = Label(al, text="PASSWORD: ", fg="white", bg="#212121")
    e2 = Entry(al, show="*")
    lb = Button(al, text="LOGIN", fg="white", bg="#1500AB",
                command=lambda: admin_auth(e1.get(), e2.get()))
    changeOnHover(lb,"#00B63E", "#1500AB")
    
    l1.grid(row=1, column=0)
    e1.grid(row=1, column=1)
    l2.grid(row=2, column=0)
    e2.grid(row=2, column=1)
    lb.grid(row=3, column=1)
    lb.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    







#login page

root = Tk()
buttonFont = font.Font(family='Verdana', size=10, weight='bold')

MyLeftPos = (root.winfo_screenwidth() - 1000) / 2
myTopPos = (root.winfo_screenheight() -500) / 2
root.geometry( "%dx%d+%d+%d" % (1000, 500, MyLeftPos, myTopPos))
root.title("FAST FOOD BILLING SYSTEM")
root.configure(bg="#fff")


adminB = Button(root, text="ADMIN", fg="white", bg="#1500AB", padx=26,
                pady=8, bd=5, width=10, anchor="center", command=admin_login,font=buttonFont)
userB = Button(root, text="EMPLOYEE", fg="white", bg="#1500AB", padx=26,
               pady=8, bd=5, width=10, anchor="center",command=user_login,font=buttonFont)
adminB.grid(row=0, column=0)
changeOnHover(adminB,"blue", "#1500AB")
changeOnHover(userB,"blue", "#1500AB")
adminB.place(relx = 0.5, rely = 0.4, anchor = CENTER)
userB.grid(row=1, column=0)
userB.place(relx = 0.5, rely = 0.5, anchor = CENTER)
#img = ImageTk.PhotoImage(Image.open(r":\Users\LENOVO\Desktop\New folder (4)\img\ikm1.jpg"))

panel = Label(root)
#panel.photo = img
#panel.grid(row=2, column=0)
root.mainloop()
