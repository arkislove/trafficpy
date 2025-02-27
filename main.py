import tkinter as tk
from tkinter import ttk, messagebox
import db_functions

def add_vehicle():
    vehicle_type = entry_vehicle_type.get()
    plate_number = entry_plate_number.get()
    location_id = entry_location_id.get()
    db_functions.add_vehicle(vehicle_type, plate_number, location_id)
    db_functions.refresh_vehicle_list(tree)

def delete_vehicle():
    selected_item = tree.selection()
    if selected_item:
        vehicle_id = tree.item(selected_item, "values")[0]
        db_functions.delete_vehicle(vehicle_id)
        db_functions.refresh_vehicle_list(tree)
    else:
        messagebox.showwarning("Selection Error", "Please select a vehicle to delete.")

def refresh_vehicle_list():
    db_functions.refresh_vehicle_list(tree)

window = tk.Tk()
window.title("TrafficPy")

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill='both')

frame1 = tk.Frame(notebook)
frame2 = tk.Frame(notebook)

notebook.add(frame1, text="Add/Delete Vehicle")
notebook.add(frame2, text="Vehicle List")

# Tab 1: Add/Delete Vehicle
tk.Label(frame1, text="Vehicle Type:").grid(row=0)
entry_vehicle_type = tk.Entry(frame1)
entry_vehicle_type.grid(row=0, column=1)

tk.Label(frame1, text="Plate Number:").grid(row=1)
entry_plate_number = tk.Entry(frame1)
entry_plate_number.grid(row=1, column=1)

tk.Label(frame1, text="Location ID:").grid(row=2)
entry_location_id = tk.Entry(frame1)
entry_location_id.grid(row=2, column=1)

button_add = tk.Button(frame1, text="Add Vehicle", command=add_vehicle)
button_add.grid(row=3, columnspan=2)

# Tab 2: Vehicle List
tree = ttk.Treeview(frame2, columns=("ID", "Type", "Model", "Color", "Image Path", "Created At", "Plate Number", "Location ID"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Type", text="Type")
tree.heading("Model", text="Model")
tree.heading("Color", text="Color")
tree.heading("Image Path", text="Image Path")
tree.heading("Created At", text="Created At")
tree.heading("Plate Number", text="Plate Number")
tree.heading("Location ID", text="Location ID")

tree.pack(expand=True, fill='both')

button_delete = tk.Button(frame2, text="Delete Vehicle", command=delete_vehicle)
button_delete.pack()

refresh_vehicle_list()

window.mainloop()
