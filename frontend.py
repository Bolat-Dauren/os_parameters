# frontend.py

import tkinter as tk
from tkinter import ttk
from backend import OSParametersBackend, ParameterRetrievalError

class OSParametersApp:
    def __init__(self, root):
        # Initialize the application window
        self.root = root
        self.root.title("System Parameters")
        self.backend = OSParametersBackend()  # Initialize the backend

        # Create a notebook to hold different parameter categories
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=10, pady=10, fill='both', expand=True)

        # Populate tabs for each parameter category
        self.create_tabs()

    def create_tabs(self):
        # Define the categories of parameters
        categories = ["Operating System", "CPU", "Memory", "Disk"]
        for category in categories:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=category)
            self.populate_tab(tab, category)

    def populate_tab(self, tab, category):
        try:
            # Retrieve parameters for the given category
            parameters = self.backend.get_parameters(category)
            for i, (key, value) in enumerate(parameters.items()):
                # Display each parameter in the tab
                ttk.Label(tab, text=key, foreground="blue").grid(row=i, column=0, padx=5, pady=5, sticky='w')
                ttk.Label(tab, text=value, foreground="green").grid(row=i, column=1, padx=5, pady=5, sticky='w')
        except ParameterRetrievalError as e:
            # Display error message if parameter retrieval fails
            ttk.Label(tab, text="Error:", foreground="red").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')
            ttk.Label(tab, text=str(e), foreground="red").grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = OSParametersApp(root)
    root.mainloop()
