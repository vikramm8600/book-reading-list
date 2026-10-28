Code Audit — Personal Book Reading List

1. Project Information

Project Name: Personal Book Reading List
Main File: main.py
Programming Language: Python
Data Storage: JSON
Application Type: Command-Line Application

2. Project Summary

The Personal Book Reading List is a Python application that allows users to maintain a collection of books and track their reading status.

The program provides options to view books, add new entries, mark books as read, and remove books. It uses a JSON file to store information locally between program executions.

The code is organized into functions for loading data, saving data, displaying books, and running the main application.

3. Code Structure

load_books()

* Checks whether books.json exists.
* Reads and decodes JSON data.
* Returns an empty list if the file does not exist.
* Handles JSON decoding and file-reading errors.

Observation: The function checks whether the loaded data is a list but does not validate individual book entries.

save_books(books)

* Converts the book list into JSON.
* Writes the data to books.json.
* Uses indentation to make the file readable.
* Uses UTF-8 encoding.

Observation: File-writing errors are not explicitly handled.

show_books(books)

* Displays all books with their authors.
* Shows whether each book has been read.
* Displays a message when the reading list is empty.

Observation: The function assumes every book contains valid title, author, and read fields.

main()

* Loads the existing reading list.
* Displays the application menu.
* Processes user selections.
* Adds, marks, and removes books.
* Saves changes to the JSON file.
* Exits when the user selects option 5.

4. Positive Findings

The application demonstrates several good programming practices:

* Uses separate functions for different responsibilities.
* Uses pathlib.Path to manage the data file location.
* Uses JSON for structured data storage.
* Preserves data between program executions.
* Validates empty book titles.
* Handles invalid numeric input when marking or removing books.
* Checks book indexes before modifying the list.
* Uses a main guard to prevent the application from running automatically when imported as a module.
* Uses UTF-8 encoding for file operations.

5. Issues Identified

Issue 1: Limited JSON Data Validation

Severity: Medium

The application checks whether the loaded JSON data is a list but does not validate the structure of each entry.

If the JSON file contains invalid entries or missing fields, the program may raise errors when displaying or modifying books.

Recommendation: Validate each entry and ensure that title and author are strings and read is a Boolean.

Issue 2: Potential Data Loss After Reading Errors

Severity: Medium

If books.json cannot be read or contains malformed JSON, load_books() returns an empty list.

If the user subsequently adds a book, the next save may overwrite the existing file, potentially destroying data that could otherwise be recovered.

Recommendation: Preserve a backup of the invalid file or stop the application and notify the user instead of silently continuing with an empty list.

Issue 3: File-Writing Errors Are Not Handled

Severity: Low

The save_books() function does not handle exceptions that may occur during writing.

Permission issues, storage problems, or other file-system errors could terminate the application.

Recommendation: Handle OSError and inform the user when changes cannot be saved.

Issue 4: Duplicate Books Are Allowed

Severity: Low

Users can add the same book multiple times.

Recommendation: Optionally check for duplicate titles before adding a new entry.

Issue 5: No Automated Tests

Severity: Low

The project does not include automated tests for its functions.

Recommendation: Add tests for adding books, removing books, updating reading status, loading invalid JSON, and handling incorrect user input.

6. Security and Privacy Review

* The application does not require user authentication.
* The program does not make network requests.
* No third-party dependencies are required.
* Book data is stored in a local JSON file.
* Anyone with access to the file can read or modify its contents.

Recommendation: Avoid storing sensitive information in the JSON file. Consider excluding personal reading data from a public repository if privacy is a concern.

7. Performance Review

The application is suitable for a small personal reading list.

Its basic operations are straightforward, and JSON storage is appropriate for a small dataset.

For a very large collection, a database could provide more efficient searching and more robust data management.

8. Recommended Improvements

The following improvements are recommended in priority order:

1. Validate JSON data before using it.
2. Prevent potential data loss when loading corrupted files.
3. Add error handling for saving operations.
4. Implement duplicate book detection.
5. Add automated tests.
6. Introduce search and filtering options.
7. Consider a graphical user interface as a future enhancement.

9. Conclusion

The Personal Book Reading List is a suitable beginner-level Python project that demonstrates functions, loops, conditional statements, exception handling, JSON operations, and file handling.

The current implementation provides the core functionality required to manage a personal reading list.

The most important improvements involve validating stored data and handling file errors more safely. Implementing these improvements would make the application more reliable and maintainable.

Audit Status: Static code review completed. Recommended improvements have been documented; they have not necessarily been implemented or tested.
