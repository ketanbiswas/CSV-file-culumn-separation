import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def clean_file():
    input_path = filedialog.askopenfilename(title="Select input CSV file", filetypes=[("CSV Files", "*.csv")])
    if not input_path:
        return

    try:
        df = pd.read_csv(input_path, delimiter='\t')
        output_path = filedialog.asksaveasfilename(
            title="Save cleaned file as",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")]
        )
        if output_path:
            df.to_csv(output_path, index=False)
            messagebox.showinfo("Success", f"Cleaned file saved as: {os.path.basename(output_path)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Column Separator")

canvas = tk.Canvas(root, width=300, height=150)
canvas.pack()

btn_clean = tk.Button(root, text="Select and Clean File", command=clean_file)
canvas.create_window(150, 75, window=btn_clean)

root.mainloop()
