import tkinter as tk
from tkinter import messagebox

def connect_to_vpn():
    server_address = entry_server.get()
    username = entry_username.get()
    password = entry_password.get()

    if server_address and username and password:
        messagebox.showinfo("Connected", "Connected to VPN Server")
    else:
        messagebox.showerror("Error", "Please fill in all the fields")

# Initialize the main window
root = tk.Tk()
root.title("VPN Connectivity")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Styling options
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Server Address
label_server = tk.Label(root, text="Server Address", font=label_font, bg="#f0f0f0")
label_server.pack(pady=5)
entry_server = tk.Entry(root, font=entry_font, width=30)
entry_server.pack(pady=5)

# Username
label_username = tk.Label(root, text="Username", font=label_font, bg="#f0f0f0")
label_username.pack(pady=5)
entry_username = tk.Entry(root, font=entry_font, width=30)
entry_username.pack(pady=5)

# Password
label_password = tk.Label(root, text="Password", font=label_font, bg="#f0f0f0")
label_password.pack(pady=5)
entry_password = tk.Entry(root, font=entry_font, show="*", width=30)
entry_password.pack(pady=5)


connect_button = tk.Button(root, text="Connect", font=button_font, bg="#4CAF50", fg="white", command=connect_to_vpn)
connect_button.pack(pady=15)


root.mainloop()
