Expense Manager Application

I. Project Overview
The Expense Manager Application is a Python-based desktop application designed to help users manage and track their personal finances. The app allows users to add, edit, delete, and view expenses, track due dates, and categorize expenses into categories such as Food, Utilities, Entertainment, and Others. The application provides reports on spending by category, displays total expenses, and allows users to generate receipts for their recorded expenses.

Key Features:

Track expenses with descriptions, due dates, prices, and categories.
Edit and delete recorded expenses.
View expense summaries by category.
Generate an itemized receipt for all expenses.
Organize expenses into categories such as Food, Utilities, Entertainment, and Others.
SQLite database integration to store and retrieve expenses.
The app aims to help users gain control over their spending, make informed decisions, and work toward financial stability.

II. Explanation of How Python Concepts, Libraries, and Tools Were Applied
The Expense Manager uses various Python concepts and libraries to achieve its functionality:

1. Tkinter (GUI):
The user interface is built using Tkinter, Python’s standard GUI library. Tkinter is used to create all the windows, buttons, labels, and other UI components.
Frames and widgets are used to structure the UI for ease of navigation between different sections (e.g., main screen and reports screen).
2. SQLite (Database Management):
SQLite is used to store and manage expenses and receipt data. The database is used to perform operations such as adding, deleting, and updating expenses.
Two tables are used:
expenses: To store expense details such as description, price, due date, and category.
receipts: To store details about receipts (optional), including receipt date and description.
3. tkcalendar:
The DateEntry widget from the tkcalendar library is used to enable users to select a date for the due date of their expenses.
It ensures that the date is entered in a consistent format and provides an interactive calendar view for date selection.
4. PIL (Python Imaging Library):
PIL (now maintained as Pillow) is used to handle images, specifically for setting a background image for the UI. This enhances the visual appeal of the application.
5. Object-Oriented Programming (OOP):
The project follows the principles of OOP. The entire functionality is encapsulated in the ExpenseManager class, which handles all aspects of expense management, UI rendering, and database operations.
Methods within this class implement the logic for saving, editing, deleting, and generating reports for expenses.
6. Error Handling:
Error handling is implemented to ensure the user inputs valid data. For example, a check is done to ensure the price entered is numeric. If incorrect data is entered, appropriate error messages are displayed using messagebox.showerror.
7. Datetime Library:
The datetime library is used to handle date-related operations, such as setting the due date for an expense and formatting it to store in the database.
It is also used when generating the receipt to present formatted dates.
8. Dynamic Data Population:
The populate_expense_listbox() and populate_category_summary_listbox() methods dynamically populate lists and reports based on the data in the SQLite database, ensuring the UI is always up to date.

III. Details of the Chosen SDG and Its Integration Into the Project
The Expense Manager Application contributes to the United Nations Sustainable Development Goal 12 (SDG 12): Responsible Consumption and Production, as well as SDG 8: Decent Work and Economic Growth. Here’s how the project aligns with these SDGs:

SDG 12: Responsible Consumption and Production
Promoting Sustainable Financial Management: By providing users with tools to track and manage their expenses, the app encourages responsible consumption patterns. Users can analyze their spending habits and identify areas where they may be overspending or consuming unsustainably (e.g., reducing non-essential entertainment costs to save for sustainable goods and services).
Efficient Resource Management: The app helps users identify how they allocate their financial resources across categories like food, utilities, and entertainment, helping them make more conscious decisions about where their money is being spent.
SDG 8: Decent Work and Economic Growth
Supporting Financial Literacy: The app aids in developing financial literacy, a crucial skill for economic empowerment. Users can make informed decisions about their finances, which can help in reducing financial instability and promoting long-term economic growth.
Economic Inclusion: The app is designed to be simple, accessible, and free (or low-cost), ensuring that individuals from diverse economic backgrounds have access to tools for managing their finances.
IV. Instructions for Running the Program
Follow the steps below to run the Expense Manager Application on your machine:

Prerequisites:
Make sure you have Python 3.x installed on your machine. You also need to install the required libraries:

Tkinter (usually comes with Python by default).
Pillow (for image handling).
tkcalendar (for date selection).
SQLite (comes with Python by default).
Installation:
Clone the Repository:
git clone https://github.com/yourusername/expense-manager.git
Install Dependencies: If you don't have the required libraries installed, you can install them using pip:
pip install pillow tkcalendar
Run the Application: Navigate to the directory where the project is located and run:
python main.py
Usage:
Upon launching the application, you can:
Add new expenses by filling out the form with expense description, price, due date, and category.
Edit or delete existing expenses from the list.
View detailed reports and summaries on the Reports screen.
Generate expense receipts that list all recorded expenses and their details.
Clear all expenses if needed.
File Structure:
expense-manager/
│
├── main.py                # Main program file
├── expenses.db            # SQLite database file
├── bg.jpg                 # Background image for the GUI (optional)
├── README.md              # Project documentation (this file)
└── requirements.txt       # List of dependencies (optional)
