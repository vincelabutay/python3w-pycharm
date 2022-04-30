import tkinter as tk

main_window = tk.Tk()
main_window.geometry("600x400")
main_window.maxsize(800, 600)

label1 = tk.Label(main_window, text="Hello Python 1", bg="blue", fg="white")
label1.pack(side=tk.LEFT, fill=tk.Y)

label2 = tk.Label(main_window, text="Hello Python 2", bg="red", fg="white")
label2.pack(side=tk.RIGHT, fill=tk.Y)

label3 = tk.Label(main_window, text="Hello Python 3", bg="grey", fg="white")
label3.pack(fill=tk.X)

label4 = tk.Label(main_window, text="Hello Python 4", bg="green", fg="white")
label4.pack(side=tk.BOTTOM, fill=tk.X)

main_window.mainloop()
