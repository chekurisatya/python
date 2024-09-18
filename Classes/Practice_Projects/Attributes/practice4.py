'''
Check for Attributes with hasattr()
Write a class Book with attributes title and author. Use hasattr() to check if a particular
attribute (e.g., publisher) exists, and if it doesn't, add it using setattr().
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

B_1 = Book("The Fellowship of the Ring", "JRR Tolkien")
if not hasattr(B_1,'publisher'):
    setattr(B_1,'publisher','Harper Collins')

print(getattr(B_1,'publisher'))

