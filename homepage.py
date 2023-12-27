import tkinter as tk
import os

def open_login_page():
    os.system("start loginpage.exe")

def open_add_user_page():
    os.system("start add_data.py")
   

def open_add_product_page():
    os.system("start addproduct.exe")

def open_delete_product_page():
    os.system("start product_delete.exe")

def open_search_product_page():
    os.system("start search.exe")

def open_update_product_page():
    os.system("start updateproduct.exe")

root = tk.Tk()
root.title("Inventory Management Homepage")
root.geometry("400x300")

login_button = tk.Button(root, text="Login Page", command=open_login_page)
login_button.pack()

add_user_button = tk.Button(root, text="Add User", command=open_add_user_page)
add_user_button.pack()

add_product_button = tk.Button(root, text="Add Product", command=open_add_product_page)
add_product_button.pack()

delete_product_button = tk.Button(root, text="Delete Product", command=open_delete_product_page)
delete_product_button.pack()

search_product_button = tk.Button(root, text="Search Product", command=open_search_product_page)
search_product_button.pack()

update_product_button = tk.Button(root, text="Update Product", command=open_update_product_page)
update_product_button.pack()

root.mainloop()

