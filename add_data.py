import tkinter as tk
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="disha2003",
    database="collegedb"
)


cursor = db.cursor()


def insert_data():
    
    username = username_entry.get()
    password = password_entry.get()
    contact = contact_entry.get()
    branch = branch_entry.get()
    

    sql = "INSERT INTO studnt (username, password, contact, branch) VALUES ( %s, %s, %s, %s)"
    values = (username, password, contact, branch)
    cursor.execute(sql, values)
    db.commit()
    
  
    
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
 
    message_label.config(text="Data successfully inserted!")

window = tk.Tk()
window.title("Insert data into SQL table")




username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(window)
password_entry.grid(row=2, column=1)

contact_label = tk.Label(window, text="Contact:")
contact_label.grid(row=3, column=0)
contact_entry = tk.Entry(window)
contact_entry.grid(row=3, column=1)

branch_label = tk.Label(window, text="Branch:")
branch_label.grid(row=4, column=0)
branch_entry = tk.Entry(window)
branch_entry.grid(row=4, column=1)


insert_button = tk.Button(window, text="Insert data", command=insert_data)
insert_button.grid(row=5, column=0)


message_label = tk.Label(window, text="")
message_label.grid(row=6, column=0)


window.mainloop()
