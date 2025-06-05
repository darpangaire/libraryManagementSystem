from library import LibraryManagementSystem

def main():
  system = LibraryManagementSystem()
  while True:
    print("\n📚 Library Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search by ID")
    print("4. Search by Title")
    print("5. Delete Book (Admin Only)")
    print("6. Exit")
    
    choices = int(input("Enter your choices"))
    
    if choices == 1:
      system.enter_book_list()
      
    elif choices == 2:
      system.book_List()
      
    elif choices == 3:
      id = input('Enter the ids of the books: ')
      system.search_id(id)
      
    elif choices == 4:
      title = input('Enter the title of the books: ')
      system.search_title(title)
      
    elif choices == 5:
      system.delete()
      
    elif choices == 6:
      print('👋 Goodbye!')
      break
    
    else:
      print('Wrong Input')
      
if __name__ == "__main__":
  main()
  
    