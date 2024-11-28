import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
user_data = []
def calculate_bmi():
    try:
        name = entry_name.get()
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive values.")
            return
        bmi = weight / (height ** 2)
        category = cal_bmi(bmi)
        user_data.append({"name": name, "weight": weight, "height": height, "bmi": bmi})
        label_result.config(text=f"Hello {name}, your BMI is {bmi:.2f} ({category})")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
def cal_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    else:
        return "Overweight"
def view_data():
    if not user_data:
        messagebox.showinfo("No Data", "No user data available.")
        return
    data_window = tk.Toplevel(root)
    data_window.title("User Data")
    for idx, record in enumerate(user_data, start=1):
        tk.Label(data_window, text=f"{idx}. {record['name']} - BMI: {record['bmi']:.2f}").pack()
def plot_bmi():
    if not user_data:
        messagebox.showinfo("No Data", "No user data available to plot.")
        return
    names = [record["name"] for record in user_data]
    bmis = [record["bmi"] for record in user_data]
    plt.figure(figsize=(8, 5))
    plt.plot(names, bmis, marker="o")
    plt.title("BMI Trend Analysis")
    plt.xlabel("User")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.show()
root = tk.Tk()
root.title("BMI Calculator")
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)
tk.Label(root, text="Weight (kg):").grid(row=1, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1)
tk.Label(root, text="Height (m):").grid(row=2, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1)
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="View Data", command=view_data).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Plot BMI Trends", command=plot_bmi).grid(row=5, column=0, columnspan=2)
label_result = tk.Label(root, text="")
label_result.grid(row=6, column=0, columnspan=2)
root.mainloop()