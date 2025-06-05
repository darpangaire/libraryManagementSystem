import json
from book import Books
from auth import Authentication
import os
from datetime import date


class LibraryManagementSystem:
  
  def __init__(self,filename="books.json"):
    self.filename = filename
    self.books = self.load_books()
    
  def load_books(self):
    if os.path.exists(self.filename):
      with open(self.filename,"r") as f:
        data = json.load(f)
        return [Books.from_dict(b) for b in data]
      
    return []
    
  def save_books(self):
    with open(self.filename,"w") as f:
      json.dump([book.to_dict() for book in self.books], f, indent=4)
    
  
    
  def enter_book_list(self):
    book_id = input("Enter the book id: ")
    book_title = input("Enter the title of the books: ")
    publish_date = input("Enter the publish date of the books(YYYY-MM-DD): ")
    author = input('Enter the name of the author: ')
    publisher = input('Enter the name of the publisher: ')
    book_price = input('Enter the price of the books: ')
    purchase_date = date.today()
    
    book = Books(book_id,book_title,publish_date,author,publisher,book_price,purchase_date)
    
    self.books.append(book)
    self.save_books()
    print("successfully added book Items.")
    
  def book_List(self):
    if not self.books:
      print('NO book items.')
      return
    else:
      for book in self.books:
        print(book)
    
  def search_id(self,book_id):
    for book in self.books:
      if book.book_id == book_id:
        print(book)
        return book.book_id
    return False
  
  def search_title(self,book_title):
    for book in self.books:
      if book.book_title == book_title:
        print("Book finded...")
        print(book)
        return book.book_title
        
    return False
  
  def delete(self):
    admin = input('Enter the admin: ')
    password = input("Enter the password: ")
    auth = Authentication.check_password(admin,password)
    if auth:
      book_id = input("enter book id: ")
      for book in self.books:
        if book.book_id == book_id:
          self.books.remove(book)
          self.save_books()
          print('delete successfully')
          return
        else:
          print('Book doesnot exists! ')
        
    else:
      print("access denied!!! Wrong Password")
      return
    

 
        
 
      
      
  

  
  
    
    
  