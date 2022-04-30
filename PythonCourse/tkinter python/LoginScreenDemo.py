import tkinter as tk

def get_value():
    print("Username :", username_entry.get() )
    print("Password :", password_entry.get() )

main_window = tk.Tk()
main_window.geometry("400x200")
main_window.title("Welcome to Python")

username_label=tk.Label(main_window, text="Username :")
password_label=tk.Label(main_window, text="Password :")
username_label.grid(row=0, column=0)
password_label.grid(row=1, column=0)

username=""
password=""

username_entry=tk.Entry(main_window, textvariable=username)
password_entry=tk.Entry(main_window, textvariable=password)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)


submit_button=tk.Button(main_window, text="Submit", command=get_value)
submit_button.grid(row=3, column=2)

main_window.mainloop()
