# Expense Manager Application

## I. Project Overview

The **Expense Manager Application** is a Python-based desktop application designed to help users manage and track their personal finances. The app enables users to:
- Add, edit, delete, and view expenses.
- Track due dates for each expense.
- Categorize expenses into categories such as Food, Utilities, Entertainment, and Others.
- View expense reports and summaries by category.
- Generate itemized receipts for recorded expenses.

The app uses an SQLite database to store expenses and receipts, providing a convenient way to track spending and make informed financial decisions.

## Key Features:
- Track expenses with descriptions, due dates, prices, and categories.
- Edit and delete recorded expenses.
- View expense summaries by category.
- Generate itemized receipts for expenses.
- Organize expenses into categories like Food, Utilities, Entertainment, and Others.
- SQLite database integration for storing and retrieving expenses.

The app aims to help users gain control over their spending, make informed decisions, and work toward financial stability.

---

## II. Explanation of How Python Concepts, Libraries, and Tools Were Applied

The **Expense Manager** uses several Python concepts and libraries to implement its functionality:

### 1. **Tkinter (GUI)**
- The user interface is built using **Tkinter**, Python’s standard GUI library. It is used to create all UI components, such as windows, buttons, labels, and input fields.
- Frames and widgets are used to structure the UI for easy navigation (e.g., between the main screen and reports screen).

### 2. **SQLite (Database Management)**
- **SQLite** is used for storing and managing expense data. The database contains two tables:
  - **expenses**: Stores expense details like description, price, due date, and category.
  - **receipts**: Stores optional receipt details, such as receipt date and description.

### 3. **tkcalendar**
- The **tkcalendar** library is used to allow users to select due dates for expenses via a DateEntry widget, providing an interactive calendar view and ensuring consistent date formats.

### 4. **Pillow (Python Imaging Library)**
- **Pillow** is used to handle images, such as setting a background image for the GUI to enhance visual appeal.

### 5. **Object-Oriented Programming (OOP)**
- The project follows **OOP** principles. The main functionality is encapsulated in the `ExpenseManager` class, which handles:
  - Expense management (adding, editing, deleting, and viewing).
  - UI rendering and database operations.
  - Report generation and receipt creation.

### 6. **Error Handling**
- Error handling is implemented to ensure user inputs are valid (e.g., ensuring price entries are numeric). Invalid data triggers appropriate error messages using `messagebox.showerror`.

### 7. **Datetime Library**
- The **datetime** library is used to handle date-related operations, such as setting due dates and formatting dates for receipts.

### 8. **Dynamic Data Population**
- Methods like `populate_expense_listbox()` and `populate_category_summary_listbox()` dynamically update the UI based on data in the SQLite database, ensuring the application is always up to date.

---

## III. Details of the Chosen SDG and Its Integration Into the Project

The **Expense Manager Application** aligns with the following **United Nations Sustainable Development Goals (SDGs)**:

### **SDG 12: Responsible Consumption and Production**
- **Promoting Sustainable Financial Management**: The app helps users track their expenses and make informed decisions, encouraging responsible consumption patterns. For example, users can reduce unnecessary spending to allocate more funds for essential or sustainable purchases.
- **Efficient Resource Management**: By categorizing expenses (e.g., Food, Utilities), the app promotes efficient use of resources, helping users prioritize their spending.

### **SDG 8: Decent Work and Economic Growth**
- **Supporting Financial Literacy**: The app helps users build financial literacy, an important skill for economic empowerment and growth. It provides insights into spending habits and promotes financial decision-making.
- **Economic Inclusion**: The app is designed to be simple and accessible, providing tools for financial management to individuals from various economic backgrounds.

---

## IV. Instructions for Running the Program

### Prerequisites:
- Python 3.x installed on your machine.
- Required libraries: Tkinter (usually included with Python), Pillow, tkcalendar, and SQLite (default with Python).

### Installation:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/expense-manager.git


**Install Dependencies:** If you don't have the required libraries installed, you can install them using pip:
```bash
pip install pillow tkcalendar
```
Run the Application: Navigate to the directory where the project is located and run:
```bash
python main.py
```
**Usage:**
- Upon launching the application, you can:
- Add new expenses by filling out the form with expense description, price, due date, and category.
- Edit or delete existing expenses from the list.
- View detailed reports and summaries on the Reports screen.
- Generate expense receipts that list all recorded expenses and their details.
- Clear all expenses if needed.
## File Structure:
```
 expense-manager/
 │
 ├── main.py                # Main program file
 ├── expenses.db            # SQLite database file
 ├── bg.jpg                 # Background image for the GUI (optional)
 ├── README.md              # Project documentation (this file)
 └── requirements.txt       # List of dependencies (optional)
```


## Video

[![Watch Video](https://img.shields.io/badge/Watch-Demonstration-blue?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/1nzbErVji5x33xw5zwNgSwGhRa2Tk7DyE/view?usp=sharing))

## Documentation
[ACP_FinalProject Papers.pdf](https://github.com/user-attachments/files/18055838/ACP_FinalProject.Papers.pdf)
