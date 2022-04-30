import tkinter as tk

main_window = tk.Tk()
label = tk.Label(main_window, text= "Hello Python", bg="grey", fg="blue",
                 padx=100, pady=200, font="comicsansms 10 bold", relief="sunken")
        #flat, groove, raised, ridge, solid, sunken
label.pack()

main_window.mainloop()