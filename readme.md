Personal Book Reading List 📚

Project Overview

The Personal Book Reading List is a simple command-line application developed using Python. It allows users to manage their personal reading lists by adding books, viewing saved books, marking books as read, and removing books.

The application stores book information in a local JSON file, allowing the reading list to persist between program executions.

Features

* View Books: Display all books in the reading list.
* Add Books: Add a new book by entering its title and author.
* Mark as Read: Update a book’s reading status when it has been completed.
* Remove Books: Delete a book from the reading list.
* Persistent Storage: Save book information in a JSON file.
* Input Validation: Prevent empty book titles and handle invalid menu choices and book numbers.
* Optional Author: Allow the author field to remain empty, defaulting to “Unknown author.”

Technologies Used

* Python
* JSON for data storage
* Pathlib for file path management

Requirements

* Python 3.9 or later
* No external libraries required

How to Run

1. Download or clone the project repository.
2. Open a terminal in the project folder.
3. Run the following command:

python main.py

    If necessary, use python3 main.py instead.
4. Choose an option from the menu.
5. Follow the instructions displayed in the terminal.

Application Menu

Option	Description
1	View all books
2	Add a new book
3	Mark a book as read
4	Remove a book
5	Exit the application

Data Storage

The application stores book information in a file named books.json, located in the same directory as main.py.

Each book is stored as a dictionary containing three fields:

* title: The title of the book.
* author: The author’s name.
* read: A Boolean value indicating whether the book has been read.

Example Data

[
  {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "read": false
  },
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "read": true
  }
]

The JSON file is created when a book is added and saved whenever a book is added, marked as read, or removed.

Project Structure

Personal-Book-Reading-List/
│
├── main.py
├── README.md
├── AUDIT.md
└── books.json

Note: books.json is generated when the application saves book data.

Limitations

* The application operates through a command-line interface.
* Duplicate books are allowed.
* Data validation for existing JSON entries is limited.
* Data is stored locally and is not synchronized across devices.
* File-writing errors are not explicitly handled.

Future Improvements

* Add duplicate book detection.
* Improve error handling for file operations.
* Validate book data when loading JSON.
* Add search and filtering functionality.
* Include categories, ratings, and reading progress.
* Develop a graphical user interface.

Author

Developed as a Python programming project to demonstrate basic programming concepts, functions, loops, conditional statements, exception handling, and JSON file operations.
