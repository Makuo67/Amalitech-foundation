class Student:

    def __init__(self, name, scores=None):
        self.name = name
        if scores is None:
            self.scores = []
        else:
            self.scores = scores

    def get_average(self):
        return sum(self.scores)/len(self.scores)

    def get_grade(self):
        avg = self.get_average()

        if avg >= 70:
            return 'A'
        elif avg >= 60 and avg < 70:
            return 'B'
        elif avg >= 50 and avg < 60:
            return 'C'
        else:
            return 'F'


class BankAccount:

    def __init__(self, name, balance=None):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited for {self.name}"

    def withdraw(self, amount):
        if self.balance < amount:
            return f"Insuficient balance"
        else:
            self.balance -= amount
            return f"{amount} withdrawn from {self.name}"

    def get_balance(self):
        return self.balance


# acc = BankAccount('Okeke')
# print(acc.deposit(100))
# print(acc.withdraw(130))
# print(acc.get_balance())


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def toggle_borrow(self):
        self.is_borrowed = not self.is_borrowed
        status = "borrowed" if self.is_borrowed else "returned"
        return f"{self.title} by {self.author} has been {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        return f"Added '{title}' by {author} to {self.name}"

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Removed '{title}' from {self.name}"
        return f"'{title}' not found in {self.name}"

    def search_by_title(self, title):
        found = [book for book in self.books if title.lower()
                 in book.title.lower()]
        if found:
            return [f"'{b.title}' by {b.author} (Borrowed: {b.is_borrowed})" for b in found]
        return [f"No books found matching '{title}'"]

    def lend_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                return book.toggle_borrow()
        return f"'{title}' not available (not found or already borrowed)"

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                return book.toggle_borrow()
        return f"'{title}' not borrowed"

    def list_books(self):
        if not self.books:
            return f"No books in {self.name}"
        result = [f"Books in {self.name}:"]
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            result.append(f"  - '{book.title}' by {book.author} [{status}]")
        return result


# Example usage / Demo
if __name__ == "__main__":
    lib = Library("Amalitech Library")

    print(lib.add_book("Python Crash Course", "Eric Matthes"))
    print(lib.add_book("Clean Code", "Robert C. Martin"))
    print(lib.add_book("The Pragmatic Programmer", "Andrew Hunt"))

    print("\nAll books:")
    for line in lib.list_books():
        print(line)

    print("\nSearch 'Python':")
    for line in lib.search_by_title("Python"):
        print(line)

    print("\nLend 'Clean Code':")
    print(lib.lend_book("Clean Code"))

    print("\nUpdated books:")
    for line in lib.list_books():
        print(line)

    print("\nReturn 'Clean Code':")
    print(lib.return_book("Clean Code"))

    print("\nTry to remove 'Python Crash Course':")
    print(lib.remove_book("Python Crash Course"))

    print("\nFinal books:")
    for line in lib.list_books():
        print(line)
