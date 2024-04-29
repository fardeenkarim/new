import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def create_folder(folder):
    os.makedirs(folder, exist_ok=True)

def generate_pdf(data):
    current_time = datetime.now().strftime("%H%M%S")
    folder = "files"
    create_folder(folder)
    pdf_filename = f"{folder}/invoice-{current_time}.pdf"
    c = canvas.Canvas(pdf_filename)
    c.drawString(72, 800, f"Invoice for: {data['customer']}")
    c.drawString(72, 780, f"Date: {data['date']}")
    c.drawString(72, 760, f"Amount Due: {data['amount']}")
    c.drawString(72, 740, f"Service: {data['service_description']}")
    c.save()
    os.system(f"open '{pdf_filename}'")

def submit():
    data = {
        'customer': customer_entry.get(),
        'date': date_entry.get_date().strftime('%Y-%m-%d'),
        'amount': amount_entry.get(),
        'service_description': service_description_entry.get()
    }
    generate_pdf(data)

root = tk.Tk()
root.title("Invoice Generator")

frame = ttk.Frame(root, padding="30")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

ttk.Label(frame, text="Customer Name:").grid(column=0, row=0, sticky=tk.W)
customer_entry = ttk.Entry(frame, width=25)
customer_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Date:").grid(column=0, row=1, sticky=tk.W)
date_entry = DateEntry(frame, width=23, borderwidth=2)
date_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Amount:").grid(column=0, row=2, sticky=tk.W)
amount_entry = ttk.Entry(frame, width=25)
amount_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Service Description:").grid(column=0, row=3, sticky=tk.W)
service_description_entry = ttk.Entry(frame, width=25)
service_description_entry.grid(column=1, row=3, sticky=(tk.W, tk.E))

submit_button = ttk.Button(frame, text="Generate Invoice", command=submit)
submit_button.grid(column=0, row=4, columnspan=2, sticky=(tk.W, tk.E))

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()