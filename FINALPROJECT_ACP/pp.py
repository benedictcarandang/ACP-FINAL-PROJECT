import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime


class ExpenseManager:
    def __init__(self, root): 
        self.root = root
        self.root.title("Expense Manager")
        self.root.geometry("800x900")
        self.root.resizable(False, False)

        self.frame1 = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)

        self.setup_database()
        self.set_background_image()

        self.create_screen1_widgets()
        self.create_screen2_widgets()

        self.frame1.pack(fill="both", expand=True)

        self.selected_expense_id = None  # Track the selected expense id for editing

    def setup_database(self):
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense TEXT,
                due_date DATE,
                price DECIMAL(10, 2),
                category VARCHAR(255),
                receipt_id INTEGER,
                FOREIGN KEY (receipt_id) REFERENCES receipts(receipt_id) ON DELETE SET NULL ON UPDATE CASCADE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS receipts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receipt_date DATE,
                amount DECIMAL(10, 2),
                category VARCHAR(255),
                description TEXT
            )
        """)
        conn.commit()
        conn.close()

    def set_background_image(self):
        try:
            bg_image = Image.open("bg.jpg")
            bg_image = bg_image.resize((800, 700), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(bg_image)
        except FileNotFoundError:
            self.bg_image = None

        self.bg_label1 = tk.Label(self.frame1, image=self.bg_image)
        self.bg_label1.place(relwidth=1, relheight=1)

        self.bg_label2 = tk.Label(self.frame2, image=self.bg_image)
        self.bg_label2.place(relwidth=1, relheight=1)

    def create_screen1_widgets(self):
        label_font = ("Arial", 12, "bold")

        self.expense_label = tk.Label(self.frame1, text="Expense Description:", font=label_font, bg="gray", anchor="w")
        self.expense_label.place(x=20, y=60, width=200, height=30)
        self.expense_entry = tk.Entry(self.frame1, font=("Arial", 12), bd=2)
        self.expense_entry.place(x=220, y=60, width=500, height=30)

        self.due_date_label = tk.Label(self.frame1, text="Due Date:", font=label_font, bg="gray", anchor="w")
        self.due_date_label.place(x=20, y=140, width=200, height=30)
        self.due_date_entry = DateEntry(self.frame1, width=20, background="gray", foreground="white", font=("Arial", 12))
        self.due_date_entry.place(x=220, y=140, width=250, height=30)

        self.price_label = tk.Label(self.frame1, text="Price (PHP):", font=label_font, bg="gray", anchor="w")
        self.price_label.place(x=20, y=220, width=200, height=30)
        self.price_entry = tk.Entry(self.frame1, font=("Arial", 12), bd=2)
        self.price_entry.place(x=220, y=220, width=250, height=30)

        self.category_label = tk.Label(self.frame1, text="Category:", font=label_font, bg="gray", anchor="w")
        self.category_label.place(x=20, y=300, width=200, height=30)
        self.category_var = tk.StringVar()
        self.category_var.set("Food")
        self.category_menu = tk.OptionMenu(self.frame1, self.category_var, "Food", "Utilities", "Entertainment", "Other")
        self.category_menu.config(font=label_font, bg="gray", fg="black")
        self.category_menu.place(x=220, y=300, width=250, height=30)

        self.save_button = tk.Button(self.frame1, text="Save", font=("Arial", 12, "bold"), bg="gray", fg="white", command=self.save_expense, relief="flat", height=2, width=5)
        self.save_button.place(x=20, y=400)

        self.edit_button = tk.Button(self.frame1, text="Edit", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.edit_expense, relief="flat", height=2, width=5)
        self.edit_button.place(x=100, y=400)

        self.delete_button = tk.Button(self.frame1, text="Delete", font=("Arial", 12, "bold"), bg="red", fg="white", command=self.delete_expense, relief="flat", height=2, width=5)
        self.delete_button.place(x=180, y=400)

        self.clear_all_button = tk.Button(self.frame1, text="Clear", font=("Arial", 12, "bold"), bg="darkred", fg="white", command=self.clear_all_expenses, relief="flat", height=2, width=5)
        self.clear_all_button.place(x=260, y=400)

        self.expense_listbox = tk.Listbox(self.frame1, font=("Courier", 12, "bold"), bd=2, relief="solid", selectbackground="gray")
        self.expense_listbox.place(x=20, y=470, width=760, height=200)

        self.switch_to_screen2_button = tk.Button(self.frame1, text="Reports", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.switch_to_screen2)
        self.switch_to_screen2_button.place(x=650, y=20)

        self.populate_expense_listbox()

    def create_screen2_widgets(self):
        self.category_summary_listbox = tk.Listbox(self.frame2, font=("Arial", 12), width=50, height=10)
        self.category_summary_listbox.pack(pady=10)

        self.calculate_button = tk.Button(self.frame2, text="Calculate", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.calculate_total_expenses, relief="flat", height=3, width=7)
        self.calculate_button.pack(pady=10)

        self.total_expenses_label = tk.Label(self.frame2, text="Total Expenses: PHP 0.00", font=("Arial", 12, "bold"), bg="gray", fg="white")
        self.total_expenses_label.pack(pady=10)

        self.generate_receipt_button = tk.Button(self.frame2, text="Generate", font=("Arial", 14, "bold"), bg="green", fg="white", command=self.generate_receipt, relief="flat", height=3, width=7)
        self.generate_receipt_button.pack(pady=10)

        self.switch_to_screen1_button = tk.Button(self.frame2, text="Back", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.switch_to_screen1)
        self.switch_to_screen1_button.place(x=650, y=20)

    def save_expense(self):
        expense = self.expense_entry.get()
        due_date = self.due_date_entry.get_date()
        price = self.price_entry.get()
        category = self.category_var.get()

        if not expense or not price:
            messagebox.showerror("Input Error", "Please fill in all fields")
            return

        try:
            price = float(price)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid price")
            return

        due_date_str = due_date.strftime('%Y-%m-%d')

        if self.selected_expense_id:
            conn = sqlite3.connect("expenses.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE expenses
                SET expense = ?, due_date = ?, price = ?, category = ?
                WHERE id = ?
            """, (expense, due_date_str, price, category, self.selected_expense_id))
            conn.commit()
            conn.close()
            self.selected_expense_id = None
        else:
            conn = sqlite3.connect("expenses.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO expenses (expense, due_date, price, category) VALUES (?, ?, ?, ?)",
                (expense, due_date_str, price, category)
            )
            conn.commit()
            conn.close()

        self.populate_expense_listbox()
        self.populate_category_summary_listbox()  # Update category summary when saving a new expense
        self.reset_input_fields()

    def edit_expense(self):
        selected_item = self.expense_listbox.curselection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an expense to edit.")
            return

        index = selected_item[0]
        selected_text = self.expense_listbox.get(index)
        expense_id = int(selected_text.split(" | ")[0])

        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        expense_data = cursor.fetchone()
        conn.close()

        if expense_data:
            self.selected_expense_id = expense_data[0]
            self.expense_entry.delete(0, tk.END)
            self.expense_entry.insert(0, expense_data[1])

            due_date = datetime.strptime(expense_data[2], "%Y-%m-%d").date()
            self.due_date_entry.set_date(due_date)

            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, expense_data[3])

            self.category_var.set(expense_data[4])

    def delete_expense(self):
        selected_item = self.expense_listbox.curselection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an expense to delete.")
            return

        index = selected_item[0]
        selected_text = self.expense_listbox.get(index)
        expense_id = int(selected_text.split(" | ")[0])

        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        conn.close()

        self.populate_expense_listbox()
        self.populate_category_summary_listbox()  # Update category summary after deleting an expense

    def clear_all_expenses(self):
        result = messagebox.askyesno("Clear All", "Are you sure you want to clear all expenses?")
        if result:
            conn = sqlite3.connect("expenses.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses")
            conn.commit()
            conn.close()
            self.populate_expense_listbox()
            self.populate_category_summary_listbox()  # Update category summary after clearing all

    def populate_expense_listbox(self):
        self.expense_listbox.delete(0, tk.END)

        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        conn.close()

        for expense in expenses:
            expense_str = f"{expense[0]} | {expense[1]} | {expense[2]} | {expense[3]} | {expense[4]}"
            self.expense_listbox.insert(tk.END, expense_str)

    def populate_category_summary_listbox(self):
        self.category_summary_listbox.delete(0, tk.END)

        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(price) FROM expenses GROUP BY category")
        category_summary = cursor.fetchall()
        conn.close()

        for category, total in category_summary:
            self.category_summary_listbox.insert(tk.END, f"{category}: PHP {total:.2f}")

    def calculate_total_expenses(self):
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(price) FROM expenses")
        total_expenses = cursor.fetchone()[0] or 0
        conn.close()

        self.total_expenses_label.config(text=f"Total Expenses: PHP {total_expenses:.2f}")

    def generate_receipt(self):
        # Retrieve all expenses from the database
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT expense, due_date, price, category FROM expenses")
        expenses = cursor.fetchall()
        conn.close()

        if not expenses:
            messagebox.showerror("Error", "No expenses available to generate a receipt.")
            return

        # Format the receipt content
        receipt_content = "Receipt\n\n"
        total_amount = 0.0
        for expense in expenses:
            expense_description = expense[0]
            due_date = expense[1]
            price = expense[2]
            category = expense[3]
            receipt_content += f"Description: {expense_description}\nDue Date: {due_date}\nPrice: PHP {price:.2f}\nCategory: {category}\n\n"
            total_amount += price

        receipt_content += f"Total Expenses: PHP {total_amount:.2f}"

        # Create a new popup window for the receipt
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Expense Receipt")
        receipt_window.geometry("400x500")
        
        # Display the receipt content
        receipt_label = tk.Label(receipt_window, text=receipt_content, font=("Arial", 12), justify="left")
        receipt_label.pack(padx=20, pady=20)
        
        # Button to close the popup
        close_button = tk.Button(receipt_window, text="Close", font=("Arial", 12), command=receipt_window.destroy)
        close_button.pack(pady=10)

    def switch_to_screen2(self):
        self.frame1.pack_forget()
        self.frame2.pack(fill="both", expand=True)
        self.populate_category_summary_listbox()

    def switch_to_screen1(self):
        self.frame2.pack_forget()
        self.frame1.pack(fill="both", expand=True)

    def reset_input_fields(self):
        self.expense_entry.delete(0, tk.END)
        self.due_date_entry.set_date(datetime.today().date())
        self.price_entry.delete(0, tk.END)
        self.category_var.set("Food")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseManager(root)
    root.mainloop()
