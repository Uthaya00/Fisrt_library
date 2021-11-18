class library:

    def __init__(self,books):
        self.books=books
    # list the books in library
    def list_books(self):
        print("avalaible books")
        for book in self.books:
            print(book.upper())
    # select and get a book from library
    def barrow_book(self,select_book):
        if select_book in self.books:
            print("get your "+ select_book +" book now")
            self.books.remove(select_book)
        else:
            print("book not avalaible")
     # return the book to library
    def receive_book(self,receive_book):
        print("you have returned the "+receive_book +" book")
        self.books.append(receive_book)
# list of books
books = ['java', 'python', 'c', 'c++', 'story','yoga']
# object created
obj=library(books)
option="""
     1.Display books
     2.which book do you want
     3.Return book

"""
while True:
        print(option)
        choice=int(input("Enter youe choice:"))
        if choice ==1:
            obj.list_books()
        elif choice==2:
            book=input("Enter the book you want: ")
            obj.barrow_book(book)
        elif choice==3:
            book=input("Enter the book you return: ")
            obj.receive_book(book)
        else:
            print("Thank You Come Again")
            quit()