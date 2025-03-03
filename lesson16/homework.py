# Task1
import sqlite3

# Создавал табличку методом, поэтому закомментировал
# def create_tables(conn):
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS books (
#             id INTEGER PRIMARY KEY,
#             title TEXT,
#             author TEXT,
#             year INTEGER,
#             status TEXT
#         )
#     ''')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS readers (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             age INTEGER
#         )
#     ''')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS borrowed_books (
#             reader_id INTEGER,
#             book_id INTEGER,
#             borrow_date TEXT,
#             FOREIGN KEY(reader_id) REFERENCES readers(id),
#             FOREIGN KEY(book_id) REFERENCES books(id)
#         )
#     ''')
#     conn.commit()
#
#
# conn = sqlite3.connect('library.db')
# create_tables(conn)
# conn.close()

# Task2
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str

@dataclass
class Reader:
    id: int
    name: str
    age: int

# Task3
class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self) -> None:
        """Создает таблицы в базе данных, если они еще не существуют"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER,
                status TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS readers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowed_books (
                reader_id INTEGER,
                book_id INTEGER,
                borrow_date TEXT,
                FOREIGN KEY(reader_id) REFERENCES readers(id),
                FOREIGN KEY(book_id) REFERENCES books(id)
            )
        ''')
        self.conn.commit()

    def add_book(self, title, author, year) -> str:
        """Добавляет новую книгу в библиотеку"""
        result = self.cursor.execute('''
            INSERT INTO books (title, author, year, status)
            VALUES (?, ?, ?, ?)
        ''', (title, author, year, 'available'))
        self.conn.commit()
        return f"Успешно добавил книгу {title}"

    def add_reader(self, name, age) -> str:
        """Добавляет нового читателя"""
        result = self.cursor.execute('''
            INSERT INTO readers (name, age)
            VALUES (?, ?)
        ''', (name, age))
        self.conn.commit()
        return f"Успешно добавил читателя {name}"

    def borrow_book(self, reader_id, book_id) -> str:
        """Выдает книгу читателю, если она доступна"""
        self.cursor.execute('SELECT status FROM books WHERE id = ?', (book_id,))
        status = self.cursor.fetchone()[0]
        if status == 'available':
            self.cursor.execute('''
                UPDATE books SET status = ? WHERE id = ?
            ''', ('borrowed', book_id))
            self.cursor.execute('''
                INSERT INTO borrowed_books (reader_id, book_id, borrow_date)
                VALUES (?, ?, ?)
            ''', (reader_id, book_id, datetime.now().strftime('%Y-%m-%d')))
            self.conn.commit()
            return "Успешно выдана книга читателю"
        else:
            return "Книга недоступна для выдачи"

    def return_book(self, book_id) -> str:
        """Возвращает книгу в библиотеку"""
        self.cursor.execute('''
            UPDATE books SET status = ? WHERE id = ?
        ''', ('available', book_id))
        self.cursor.execute('''
            DELETE FROM borrowed_books WHERE book_id = ?
        ''', (book_id,))
        self.conn.commit()
        return "Книга успешно возвращена"

    def search_books(self, keyword) -> list:
        """Поиск книг по названию или автору"""
        self.cursor.execute('''
            SELECT * FROM books WHERE title LIKE ? OR author LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))
        return self.cursor.fetchall()

    def get_borrowed_books(self) -> list:
        """Выводит список всех выданных книг"""
        self.cursor.execute('''
            SELECT books.id, books.title, readers.name, borrowed_books.borrow_date
            FROM borrowed_books
            JOIN books ON borrowed_books.book_id = books.id
            JOIN readers ON borrowed_books.reader_id = readers.id
        ''')
        return self.cursor.fetchall()

    def get_statistics(self) -> tuple[int, int]:
        """Показывает количество доступных и занятых книг"""
        self.cursor.execute('SELECT COUNT(*) FROM books WHERE status = ?', ('available',))
        available = self.cursor.fetchone()[0]
        self.cursor.execute('SELECT COUNT(*) FROM books WHERE status = ?', ('borrowed',))
        borrowed = self.cursor.fetchone()[0]
        return available, borrowed

    def close(self):
        """Закрывает соединение с базой данных"""
        self.conn.close()

def interactive_menu():
    library = Library()
    while True:
        print("\n1. Добавить книгу")
        print("2. Добавить читателя")
        print("3. Выдать книгу")
        print("4. Вернуть книгу")
        print("5. Поиск книг")
        print("6. Список выданных книг")
        print("7. Статистика")
        print("8. Выход")
        choice = input("\nВыберите действие: ")
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            print(library.add_book(title, author, year))
        elif choice == '2':
            name = input("Введите имя читателя: ")
            age = int(input("Введите возраст читателя: "))
            print(library.add_reader(name, age))
        elif choice == '3':
            reader_id = int(input("Введите ID читателя: "))
            book_id = int(input("Введите ID книги: "))
            print(library.borrow_book(reader_id, book_id))
        elif choice == '4':
            book_id = int(input("Введите ID книги: "))
            print(library.return_book(book_id))
        elif choice == '5':
            keyword = input("Введите ключевое слово для поиска: ")
            books = library.search_books(keyword)
            for book in books:
                print(book)
        elif choice == '6':
            borrowed_books = library.get_borrowed_books()
            for book in borrowed_books:
                print(book)
        elif choice == '7':
            available, borrowed = library.get_statistics()
            print(f"Доступно книг: {available}, Выдано книг: {borrowed}")
        elif choice == '8':
            library.close()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

interactive_menu()