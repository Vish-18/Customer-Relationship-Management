from Crm_oops import *
from tkinter import *
from tkinter import messagebox


def add_handler():
    add_frame = Toplevel(root)
    add_frame.geometry("500x450")
    add_frame.title("Add New Customer")

    Label(add_frame, text="Add New Customer", font=("Arial", 18)).pack(pady=20)

    Label(add_frame, text="Customer ID:", font=("Arial", 12)).pack(pady=5)
    Entry(add_frame, font=("Arial", 16), textvariable=var_id).pack()

    Label(add_frame, text="Customer Name:", font=("Arial", 12)).pack(pady=5)
    Entry(add_frame, font=("Arial", 16), textvariable=var_name).pack()

    Label(add_frame, text="Customer Age:", font=("Arial", 12)).pack(pady=5)
    Entry(add_frame, font=("Arial", 16), textvariable=var_age).pack()

    Label(add_frame, text="Customer Mobile:", font=("Arial", 12)).pack(pady=5)
    Entry(add_frame, font=("Arial", 16), textvariable=var_mob).pack()

    Button(add_frame, text="Save Customer", font=("Arial", 12), command=add_customer).pack(pady=20)


def add_customer():
    cus = Customer()
    cus.id = var_id.get()
    cus.name = var_name.get()
    cus.mob = var_mob.get()
    cus.age = var_age.get()
    cus.addCustomer()
    var_id.set("")
    var_name.set("")
    var_mob.set("")
    var_age.set("")
    messagebox.showinfo("CMS", "Customer Saved Successfully")


def search_handler():
    search_frame = Toplevel(root)
    search_frame.geometry("500x450")
    search_frame.title("Search Customer")
    Label(search_frame, text="Search Customer", font=("Arial", 18)).pack(pady=20)

    Label(search_frame, text="Customer ID:", font=("Arial", 12)).pack(pady=5)
    Entry(search_frame, font=("Arial", 16), textvariable=var_id).pack()

    Label(search_frame, text="Customer Name:", font=("Arial", 12)).pack(pady=5)
    Entry(search_frame, font=("Arial", 16), textvariable=var_name).pack()

    Label(search_frame, text="Customer Age:", font=("Arial", 12)).pack(pady=5)
    Entry(search_frame, font=("Arial", 16), textvariable=var_age).pack()

    Label(search_frame, text="Customer Mobile:", font=("Arial", 12)).pack(pady=5)
    Entry(search_frame, font=("Arial", 16), textvariable=var_mob).pack()

    Button(search_frame, text="Search Customer", font=("Arial", 12), command=search_operation).pack(pady=20)

def search_operation():
    cus = Customer()
    cus.id = var_id.get()
    cus.searchCustomer()  # Make sure this method sets cus.name, cus.age, and cus.mob based on cus.id
    var_name.set(cus.name)
    var_age.set(cus.age)
    var_mob.set(cus.mob)

def delete_handler():
    delete_frame = Toplevel(root)
    delete_frame.geometry("500x450")
    delete_frame.title("Delete  Customer")

    Label(delete_frame, text="Delete Customer", font=("Arial", 18)).pack(pady=20)

    Label(delete_frame, text="Customer ID:", font=("Arial", 12)).pack(pady=5)
    Entry(delete_frame, font=("Arial", 16), textvariable=var_id).pack()

    Button(delete_frame, text="delete Customer", font=("Arial", 12), command=delete_operation).pack(pady=20)
def delete_operation():
    cus = Customer()
    id_value = var_id.get()

    # Check if the value is empty or not a valid integer
    if not id_value:
        messagebox.showerror("CMS", "Customer ID cannot be empty")
        return

    try:
        cus.id = int(id_value)
        cus.deleteCustomer()
        messagebox.showinfo("CMS", "Customer Deleted Successfully")
        var_id.set("")
    except ValueError:
        messagebox.showerror("CMS", "Invalid Customer ID format")


def modify_handler():
    modify_frame = Toplevel(root)
    modify_frame.geometry("500x450")
    modify_frame.title("Modify New Customer")

    Label(modify_frame, text="Modify New Customer", font=("Arial", 18)).pack(pady=20)


    Label(modify_frame, text="Customer ID:", font=("Arial", 12)).pack(pady=5)
    Entry(modify_frame, font=("Arial", 16), textvariable=var_id).pack()


    Label(modify_frame, text="Customer Name:", font=("Arial", 12)).pack(pady=5)
    Entry(modify_frame, font=("Arial", 16), textvariable=var_name).pack()

    Label(modify_frame, text="Customer Age:", font=("Arial", 12)).pack(pady=5)
    Entry(modify_frame, font=("Arial", 16), textvariable=var_age).pack()

    Label(modify_frame, text="Customer Mobile:", font=("Arial", 12)).pack(pady=5)
    Entry(modify_frame, font=("Arial", 16), textvariable=var_mob).pack()

    Button(modify_frame, text="Modify Customer", font=("Arial", 12), command=modify_operation).pack(pady=20)

def modify_operation():
    cus = Customer()  # 11000, cus.id=0,cus.name=0
    cus.id = var_id.get()       #20
    cus.name = var_name.get()   #Prashant
    cus.age = var_age.get()     #55
    cus.mob = var_mob.get()     #9999
    cus.modifyCustomer()
    messagebox.showinfo("CMS", "Customer Modified Successfully")
    var_id.set("")
    var_name.set("")
    var_age.set("")
    var_mob.set("")



def display_handler():
    root_all_cust = Tk()
    lbl_id_all = Label(root_all_cust, text="CUST ID", font=1, bg="Orange", width=20, height=2)
    lbl_id_all.grid(row=0, column=0)
    lbl_name_all = Label(root_all_cust, text="CUST NAME", font=1, bg="Orange", width=20, height=2)
    lbl_name_all.grid(row=0, column=1)
    lbl_age_all = Label(root_all_cust, text="CUST AGE", font=1, bg="Orange", width=20, height=2)
    lbl_age_all.grid(row=0, column=2)
    lbl_mob_all = Label(root_all_cust, text="CUST MOB", font=1, bg="Orange", width=20, height=2)
    lbl_mob_all.grid(row=0, column=3)
    i = 0
    for e in Customer.cus_list:  # e=1000, 2000
        i += 1  # i=1, i=2
        lbl_id_cust = Label(root_all_cust, text=e.id, font=1, bg="Yellow", width=20, height=2)
        lbl_id_cust.grid(row=i, column=0)
        lbl_name_cust = Label(root_all_cust, text=e.name, font=1, bg="Yellow", width=20, height=2)
        lbl_name_cust.grid(row=i, column=1)
        lbl_age_cust = Label(root_all_cust, text=e.age, font=1, bg="Yellow", width=20, height=2)
        lbl_age_cust.grid(row=i, column=2)
        lbl_mob_cust = Label(root_all_cust, text=e.mob, font=1, bg="Yellow", width=20, height=2)
        lbl_mob_cust.grid(row=i, column=3)

def save_handler():
    Customer.saveToPickle()
    messagebox.showinfo("CMS", "Data Saved Successfully")
def load_handler():
    Customer.loadFromPickle()
    messagebox.showinfo("CMS", "Data Loaded Successfully")
root = Tk()
root.geometry("750x725+100+50")
root.title("Customer Management Application")
root.configure(bg="#f0f0f0")

# Set heading
heading = Label(root, text="CUSTOMER MANAGEMENT APPLICATION", font=("Arial", 25, "bold"), bg="#ff7f50", fg="white", pady=20)
heading.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")

# Button configurations
btn_config = {
    "font": ("Arial", 14),
    "width": 20,
    "height": 2,
    "bg": "#9370DB",
    "fg": "white",
    "activebackground": "#8A2BE2",
    "activeforeground": "white"
}


def Menu():
    btn_add = Button(root, text="Insert Customer", **btn_config, command=add_handler)
    btn_add.grid(row=1, column=1, pady=10)

    btn_search = Button(root, text="Search Customer", **btn_config, command=search_handler)
    btn_search.grid(row=2, column=1, pady=10)

    btn_delete = Button(root, text="Delete Customer", **btn_config,command=delete_handler)
    btn_delete.grid(row=3, column=1, pady=10)

    btn_modify = Button(root, text="Modify Customer", **btn_config,command=modify_handler)
    btn_modify.grid(row=4, column=1, pady=10)

    btn_display_all = Button(root, text="Display All Customers", **btn_config,command=display_handler)
    btn_display_all.grid(row=5, column=1, pady=10)

    btn_save = Button(root, text="Save Data", **btn_config,command=save_handler)
    btn_save.grid(row=6, column=1, pady=10)

    btn_load = Button(root, text="Load Data", **btn_config,command=load_handler)
    btn_load.grid(row=7, column=1, pady=10)


var_id = IntVar()
var_name = StringVar()
var_age = IntVar()
var_mob = IntVar()

Menu()

root.mainloop()
