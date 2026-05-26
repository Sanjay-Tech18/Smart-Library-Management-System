from datetime import datetime, timedelta


class Library:
    def __init__(self):
        self.books = {
            "Python Basics": {"available": True},
            "Cyber Security": {"available": True},
            "Machine Learning": {"available": True},
            "Networking Fundamentals": {"available": True},
        }

        self.issued_books = {}

    def display_books(self):
        print("\n📚 ===== AVAILABLE BOOKS =====")

        for book, details in self.books.items():
            status = "✅ Available" if details["available"] else "❌ Issued"
            print(f"- {book} : {status}")

    def issue_book(self):
        self.display_books()

        book_name = input("\nEnter book name to issue: ").strip()

        if book_name not in self.books:
            print("❌ Book not found.")
            return

        if not self.books[book_name]["available"]:
            print("⚠️ Book is already issued.")
            return

        student_name = input("Enter student name: ").strip()

        try:
            duration = int(input("Enter duration (in days): "))
        except ValueError:
            print("❌ Invalid duration.")
            return

        issue_date = datetime.now()
        return_date = issue_date + timedelta(days=duration)

        self.books[book_name]["available"] = False

        self.issued_books[book_name] = {
            "student": student_name,
            "issue_date": issue_date,
            "return_date": return_date,
        }

        print("\n✅ Book Issued Successfully!")
        print(f"📖 Book: {book_name}")
        print(f"👤 Student: {student_name}")
        print(f"📅 Return By: {return_date.strftime('%d-%m-%Y')}")

    def calculate_fine(self, late_days):
        weeks_late = late_days // 7 + 1

        fine = 0

        for week in range(1, weeks_late + 1):
            fine += week * 20  # Progressive fine

        return fine

    def return_book(self):
        book_name = input("\nEnter book name to return: ").strip()

        if book_name not in self.issued_books:
            print("❌ This book was not issued.")
            return

        record = self.issued_books[book_name]

        today = datetime.now()
        due_date = record["return_date"]

        late_days = (today - due_date).days

        print("\n📘 ===== RETURN DETAILS =====")
        print(f"Book: {book_name}")
        print(f"Student: {record['student']}")

        if late_days > 0:
            fine = self.calculate_fine(late_days)

            print(f"⚠️ Late by {late_days} days")
            print(f"💰 Fine Amount: ₹{fine}")
        else:
            print("✅ Returned on time. No fine!")

        self.books[book_name]["available"] = True
        del self.issued_books[book_name]

        print("📚 Book returned successfully!")

    def menu(self):
        while True:
            print("\n")
            print("=" * 45)
            print("📚 SMART LIBRARY MANAGEMENT SYSTEM")
            print("=" * 45)
            print("1. View Books")
            print("2. Issue Book")
            print("3. Return Book")
            print("4. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.display_books()

            elif choice == "2":
                self.issue_book()

            elif choice == "3":
                self.return_book()

            elif choice == "4":
                print("\n👋 Thank you for using the Library System!")
                break

            else:
                print("❌ Invalid choice. Try again.")


library = Library()
library.menu()
