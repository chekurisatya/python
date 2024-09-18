'''
2. Class with Default Values
Write a class Book with attributes title, author, and pages. The default value for pages should be 100.
Create a few instances of Book and print the details of each book.
'''

class Book:

    def __init__(self, title, author, pages = 100):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}. Has {self.pages} pages"

B1 = Book("Hello","JRR Tolkien", 380 )
B2 = Book("Goodbye", "Satya")
print(B1)
print(B2)
