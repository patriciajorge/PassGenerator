import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle
from backend import generate_password  # Imports the generate_password function from the backend

def start_interface():
    def generate_password_frontend():
        try:
            length = int(entry_length.get())
            if length <= 0:
                raise ValueError

            # Gets the user's options and calls the generate_password function from the backend
            password = generate_password(
                length=length,
                use_uppercase=var_uppercase.get(),
                use_lowercase=var_lowercase.get(),
                use_numbers=var_numbers.get(),
                use_symbols=var_symbols.get()
            )

            if not password:
                messagebox.showwarning("Warning", "Please select at least one character type.")
                return

            # Displays the generated password
            entry_password.delete(0, tk.END)
            entry_password.insert(0, password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid length.")

    # Main window settings
    root = tk.Tk()
    root.title("Random Password Generator")
    root.geometry('350x400')

    # Apply the scidpink theme
    style = ThemedStyle(root)
    style.set_theme("scidpink")

    # Configure widget styles
    style.configure('TEntry', font=('Arial', 16))
    style.configure('TButton', font=('Arial', 16))
    style.configure('TCheckbutton', font=('Arial', 13))

    # Labels and entry fields
    frame_config = ttk.Frame(root)
    frame_config.pack(pady=20)

    label_title = ttk.Label(frame_config, text='Random Password Generator', font=('Arial', 18))
    label_title.grid(row=0, column=0, columnspan=2, pady=(0, 30))

    label_length = ttk.Label(frame_config, text="Password Length:", font=('Arial', 14))
    label_length.grid(row=1, column=0, sticky='e')

    global entry_length  
    entry_length = ttk.Entry(frame_config, width=5)
    entry_length.grid(row=1, column=1, padx=5)
    entry_length.insert(0, "")

    # Control variables for Checkbuttons
    global var_uppercase, var_lowercase, var_numbers, var_symbols
    var_uppercase = tk.BooleanVar(value=True)
    var_lowercase = tk.BooleanVar(value=True)
    var_numbers = tk.BooleanVar(value=True)
    var_symbols = tk.BooleanVar(value=True)

    # Checkbuttons for inclusion options
    frame_options = ttk.LabelFrame(root)
    frame_options.pack(pady=20)

    check_uppercase = ttk.Checkbutton(frame_options, text="Include Uppercase", variable=var_uppercase)
    check_uppercase.grid(row=0, column=0, sticky='w')

    check_lowercase = ttk.Checkbutton(frame_options, text="Include Lowercase", variable=var_lowercase)
    check_lowercase.grid(row=1, column=0, sticky='w')

    check_numbers = ttk.Checkbutton(frame_options, text="Include Numbers", variable=var_numbers)
    check_numbers.grid(row=0, column=1, sticky='w')

    check_symbols = ttk.Checkbutton(frame_options, text="Include Symbols", variable=var_symbols)
    check_symbols.grid(row=1, column=1, sticky='w')

    # Button to generate the password
    btn_generate = ttk.Button(root, text="Generate Password", command=generate_password_frontend)
    btn_generate.pack(pady=20)

    # Field to display the generated password
    global entry_password  # To be accessible within the generate_password_frontend function
    entry_password = ttk.Entry(root, width=40)
    entry_password.pack()

    # Start the application
    root.mainloop()

# Start the interface
start_interface()
