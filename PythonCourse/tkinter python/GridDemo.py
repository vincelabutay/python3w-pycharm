import tkinter as tk

main_windows = tk.Tk()
main_windows.geometry("800x600")

label1 = tk.Label(main_windows, text="Hello Python1", bg="Green", fg="white")
label1.grid(row=3, column=3, padx=10, pady=10)

label2 = tk.Label(main_windows, text="Hello Python1", bg="Green", fg="white")
label2.grid(row=0, column=1, padx=10, pady=10)

label3 = tk.Label(main_windows, text="Hello Python1", bg="Green", fg="white")
label3.grid(row=4, column=6, padx=10, pady=10)

main_windows.mainloop()