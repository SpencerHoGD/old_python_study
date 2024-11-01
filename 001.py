class Book:
    def __init__(self, title, author, language):
        # Initialize book informations
        self.title = title
        self.author = author
        self.language = language
    def print_book_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Language: {self.language}')


book1 = Book(title='Harry Potter and the Sorcerer Stone', author='JK. Rowling', language='English')

book1.print_book_info()