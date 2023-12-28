
import tkinter as tk
import mysql.connector
import os


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="disha2003",
    database="collegedb"
)


def redirect_to_homepage():
    os.system("python homepage.py")


def verify_login():
    
    username = username_entry.get()
    password = password_entry.get()
    
    
    cursor = db.cursor()
    
   
    query = "SELECT * FROM studnt WHERE username=%s AND password=%s"
    values = (username, password)
    cursor.execute(query, values)
    
    
    result = cursor.fetchone()
    
    
    if result:
        success_label.config(text="Login successful!")
        register_label.pack_forget()
        success_label.pack()
        redirect_to_homepage()  
    else:
        register_label.config(text="Register first!")
        success_label.pack_forget()
        register_label.pack()


root = tk.Tk()
root.title("Login Page")

root.geometry("400x150")


username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()


password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


login_button = tk.Button(root, text="Login", command=verify_login)
login_button.pack()


success_label = tk.Label(root, text="")
success_label.pack()
success_label.config(fg="green", font=("Arial", 12))
success_label.pack_forget()


register_label = tk.Label(root, text="")
register_label.pack()
register_label.config(fg="red", font=("Arial", 12))
register_label.pack_forget()


root.mainloop()
