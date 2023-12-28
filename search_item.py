
import os
import tkinter as tk
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="disha2003",
    database="collegedb"
)
def redirect_to_homepage():
    os.system("python homepage.py")


def search_product():
    product = product_entry.get()
    price = price_entry.get()

    cursor = db.cursor()
    query = "SELECT * FROM stocks WHERE product=%s AND price=%s"
    values = (product, price)
    cursor.execute(query, values)

    result = cursor.fetchone()

    if result:
        search_result.config(text="Product found sucessfully",fg="green",font=("Arial", 12))  # Display the found product details
    else:
        search_result.config(text="Product not found",fg ="red",font=("Arial", 12))
    
root = tk.Tk()
root.title("Search Product")
root.geometry("400x200")


product_label = tk.Label(root, text="Product Name:")
product_label.pack()

product_entry = tk.Entry(root)
product_entry.pack()

price_label = tk.Label(root, text="Product Price:")
price_label.pack()

price_entry = tk.Entry(root)
price_entry.pack()


search_button = tk.Button(root, text="Search", command=search_product)
search_button.pack()


search_result = tk.Label(root, text="")

search_result.pack()

root.mainloop()
