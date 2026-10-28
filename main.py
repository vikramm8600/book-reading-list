"""A simple reading list that saves books in a local JSON file."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("books.json")


def load_books() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Could not read books.json; starting with an empty list.")
        return []


def save_books(books: list[dict]) -> None:
    DATA_FILE.write_text(
        json.dumps(books, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def show_books(books: list[dict]) -> None:
    if not books:
        print("Your reading list is empty.")
        return
    for index, book in enumerate(books, start=1):
        status = "Read" if book["read"] else "To read"
        print(f"{index}. {book['title']} — {book['author']} [{status}]")


def main() -> None:
    books = load_books()
    while True:
        print("\n=== Personal Book Reading List ===")
        print("1. View books")
        print("2. Add a book")
        print("3. Mark a book as read")
        print("4. Remove a book")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            show_books(books)
        elif choice == "2":
            title = input("Book title: ").strip()
            author = input("Author (optional): ").strip() or "Unknown author"
            if not title:
                print("Title cannot be empty.")
                continue
            books.append({"title": title, "author": author, "read": False})
            save_books(books)
            print("Book added.")
        elif choice == "3":
            show_books(books)
            try:
                index = int(input("Book number to mark as read: ")) - 1
                if 0 <= index < len(books):
                    books[index]["read"] = True
                    save_books(books)
                    print("Book marked as read.")
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            show_books(books)
            try:
                index = int(input("Book number to remove: ")) - 1
                if 0 <= index < len(books):
                    removed = books.pop(index)
                    save_books(books)
                    print(f"Removed: {removed['title']}")
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
