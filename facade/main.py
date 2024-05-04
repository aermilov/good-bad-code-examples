class BookManager:
    """Управление книгами в библиотеке"""
    def __init__(self):
        self.available_books = {}
        self.lent_books = {}

    def add_book(self, title, author):
        if title in self.available_books:
            self.available_books[title]['quantity'] += 1
        else:
            self.available_books[title] = {'author': author, 'quantity': 1}
        print(f"Book '{title}' by {author} added to the library. Total copies: {self.available_books[title]['quantity']}.")

    def lend_book(self, title, user):
        if title in self.available_books and self.available_books[title]['quantity'] > 0:
            self.available_books[title]['quantity'] -= 1
            self.lent_books.setdefault(title, []).append(user)
            print(f"Book '{title}' lent to {user}. Remaining copies: {self.available_books[title]['quantity']}.")
        else:
            print(f"Book '{title}' is not available or out of stock.")

    def return_book(self, title, user):
        if title in self.lent_books and user in self.lent_books[title]:
            self.lent_books[title].remove(user)
            self.add_book(title, self.available_books[title]['author'])
            print(f"Book '{title}' returned by {user}.")
        else:
            print(f"Book '{title}' was not lent to {user} or already returned.")

class ReaderManager:
    """Управление читателями в библиотеке"""
    def __init__(self):
        self.readers = {}

    def register_reader(self, name, email):
        self.readers[email] = name
        print(f"Reader {name} registered with email {email}")

class LoanManager:
    """Управление задолженностями по возврату книг"""
    def check_loans(self, book_manager):
        overdue_books = []
        for book, users in book_manager.lent_books.items():
            if len(users) > 0:
                overdue_books.append(book)
        if overdue_books:
            print("Overdue books:", ", ".join(overdue_books))
        else:
            print("No overdue books.")

### Определение класса Фасада

class LibraryFacade:
    """Фасад для управления библиотекой"""
    def __init__(self, book_manager, reader_manager, loan_manager):
        self.book_manager = book_manager
        self.reader_manager = reader_manager
        self.loan_manager = loan_manager

    def register_new_reader(self, name, email):
        self.reader_manager.register_reader(name, email)

    def add_new_book(self, title, author):
        self.book_manager.add_book(title, author)

    def borrow_book(self, title, user):
        self.book_manager.lend_book(title, user)
        self.loan_manager.check_loans(self.book_manager)

    def return_book(self, title, user):
        self.book_manager.return_book(title, user)
        self.loan_manager.check_loans(self.book_manager)

if __name__ == "__main__":
    # Инициализация фасада библиотеки
    library = LibraryFacade(BookManager(), ReaderManager(), LoanManager())

    # Регистрация читателей
    readers = [
        ("Alice Johnson", "alice.johnson@example.com"),
        ("Bob Smith", "bob.smith@example.com"),
        ("Catherine Lee", "catherine.lee@example.com"),
        ("David Brown", "david.brown@example.com")
    ]

    for name, email in readers:
        library.register_new_reader(name, email)

    # Добавление книг
    books = [
        ("1984", "George Orwell"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("One Hundred Years of Solitude", "Gabriel Garcia Marquez"),
        ("Pride and Prejudice", "Jane Austen")
    ]

    for title, author in books:
        library.add_new_book(title, author)

    # Выдача книг
    loans = [
        ("1984", "alice.johnson@example.com"),
        ("The Great Gatsby", "bob.smith@example.com"),
        ("To Kill a Mockingbird", "alice.johnson@example.com"),
        ("Pride and Prejudice", "catherine.lee@example.com")
    ]

    for title, user in loans:
        library.borrow_book(title, user)

    # Возврат книг
    returns = [
        ("1984", "alice.johnson@example.com"),
        ("The Great Gatsby", "bob.smith@example.com")
    ]

    for title, user in returns:
        library.return_book(title, user)

    # Попытка повторной выдачи и возврата
    library.borrow_book("One Hundred Years of Solitude", "david.brown@example.com")
    library.return_book("One Hundred Years of Solitude", "david.brown@example.com")

    # Добавление и выдача новой книги
    library.add_new_book("Moby Dick", "Herman Melville")
    library.borrow_book("Moby Dick", "bob.smith@example.com")

    # Проверка задолженностей
    library.loan_manager.check_loans(library.book_manager)

    # Вывод всех доступных книг в библиотеке после операций
    print("\nAvailable books in the library:")
    for title, info in library.book_manager.available_books.items():
        print(f"Title: {title}, Author: {info['author']}, Quantity: {info['quantity']}")
