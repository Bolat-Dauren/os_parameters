# frontend.py

import tkinter as tk
from tkinter import ttk
from backend import OSParametersBackend, ParameterRetrievalError

class OSParametersApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("System Parameters")
        self.backend = OSParametersBackend()
        # Initialize the backend
        self.notebook = ttk.Notebook(self.root)
        # Create a notebook widget to hold tabs
        self.notebook.pack(padx=10, pady=10, fill='both', expand=True)
        # Pack the notebook to the window
        self.create_tabs()
        # Populate tabs with parameters

    def create_tabs(self):
        # Define the categories of parameters to be displayed in tabs
        categories = ["Operating System", "CPU", "Memory", "Disk", "Additional"]
        for category in categories:
            # Create a new tab for each category
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=category)
            # Add the tab to the notebook
            self.populate_tab(tab, category)
            # Populate the tab with parameters

    def populate_tab(self, tab, category):
        try:
            # Retrieve parameters for the given category from the backend
            parameters = self.backend.get_parameters(category)
            # Display each parameter in the tab
            for i, (key, value) in enumerate(parameters.items()):
                # Create labels for parameter key and value
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