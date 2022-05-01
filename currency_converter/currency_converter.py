import tkinter as tk
import tkinter.ttk as ttk

def convert_pressed():
    amount = input_text.get()
    from_curr = source_value.get()
    to_curr = target_value.get()

main_window = tk.Tk()
main_window.title = ("Currency Converter")
main_window.geometry("450x200")

intro_label = tk.Label(main_window, text="Welcome to Live Currency Converter", fg="white", bg="blue",
                       borderwidth=3, relief=tk.RAISED)
intro_label.config(font=("Courier", 15, "bold"))
main_window.grid_columnconfigure(0, weight=1)
intro_label.grid(row=1)

input_text=tk.StringVar()
currency_field = tk.Entry(main_window, justify="right", textvariable=input_text)
currency_field.grid(row=2, padx=5, pady=5)

country_code = ["INR", "USD", "CAD", "CNY", "DDK", "PHP", "EUR"]
source_value=tk.StringVar()
source_value_selection = ttk.Combobox(main_window, values=country_code, textvariable=source_value)
source_value_selection.grid(row=3, padx=5, pady=5)

country_code = ["INR", "USD", "CAD", "CNY", "DDK", "PHP", "EUR"]
target_value=tk.StringVar()
target_value_selection = ttk.Combobox(main_window, values=country_code, textvariable=target_value)
target_value_selection.grid(row=4, padx=5, pady=5)

convert_button = tk.Button(main_window, text="Convert", height=1, width=7, command=lambda: convert_pressed())
convert_button.grid(row=5)

conversion_label = tk.Label(text="")
conversion_label.grid(row=6)

main_window.mainloop()