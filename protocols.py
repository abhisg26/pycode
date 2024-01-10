from typing import Protocol

class Printable(Protocol):
    pages: int

    def print(self):
        pass

    def recycle(self):
        pass

class Book:
    pages: int

    def __init__(self,title: str):
        self.title = title

    def print_item(self):
        print(f'Printing book: {self.title}')

    def recycle(self):
        print(f'Recycling: {self.title}')

def print_printable(printable: Printable):
    printable.print_item()

class Magazine:
    pages: int

    def __init__(self,title: str):
        self.title = title

    def print_item(self):
        print(f'Printing book: {self.title}')

    def recycle(self):
        print(f'Recycling: {self.title}')


book: Printable = Book('Python')
print_printable(book)



magazine: Printable = Magazine('Pythonistas')
print_printable(magazine)
