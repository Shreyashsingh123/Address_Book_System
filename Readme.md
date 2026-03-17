# 📘 Address Book Management System
#
# ## 📌 Introduction
# The Address Book Management System is a Python application for storing and managing contact information.
# It allows users to add, edit, delete, search, and sort contacts efficiently.
# The system supports file storage using JSON, CSV, and Text formats for easy data saving and loading.

# ---
  ## Features
# - Add, edit, and delete contacts
# - Add multiple contacts
# - Prevent duplicate entries
# - Search by city or state
# - Sort by name, city, state, or ZIP
# - Save data to (JSON / CSV / TXT)
# - load data from (JSON / CSV / TXT)

# ---
#
# ## 📁 Project Structure
# address_book_app/
# │
# ├── App/
# │   ├── Models/
# │   │   ├── Contact.py
# │   │   └── Address_Book.py
# │   │
# │   ├── Services/              # Business Logic
# │   │   └── Address_book_manager.py
# │   │
# │   └── Utils/                 # Helper Function
# │       ├── File_Handler.py
# │       ├── Searching.py
# │       └── Sorting.py
#
# ├── UserData/                  # Store User data
# │   ├── address_book1.json
# │   ├── address book.csv
#    
#
# ├── main.py                    # program starting point(Entry Point)
# └── README.md
#
# -----

# ## ▶️ How to Run
# python main.py
#
# ------
#
# ## 🛠️ Technologies Used
# - Python
# - JSON, CSV, Text files
#
# ------

# ## 📖 Conclusion
# This project demonstrates core OOP concepts, modular design, and file handling in Python.