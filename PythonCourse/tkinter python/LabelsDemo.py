import tkinter as tk

main_window = tk.Tk()
label = tk.Label(main_window, text="Hello Python", bg="grey", fg="blue",
                 padx=100, pady=80, font="comic-sans-ms 10 bold", relief="flat")
# flat, groove, raised, ridge, solid, sunken
label.pack()


# adding photo to interface
photo = tk.PhotoImage(file="img.png")
label1 = tk.Label(image=photo)
label1.pack()

main_window.mainloop()
