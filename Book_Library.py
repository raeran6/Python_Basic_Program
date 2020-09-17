class Book_Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        print(f"We have following Books in Our Library:{self.name}")
        for book in self.booklist:
            print(book)

    def lend_book(self,user,book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book:user})
            print("Book DataBase Has been update.You can take book Now")
        else:
            print(f"Book is already in Use by{self.lend_dict[book]}")

    def add_book(self,book):
        self.booklist.append(book)
        print("Book Has been added Successfully")

    def return_book(self,book):
        self.booklist.remove(book)




if __name__ == '__main__':
    lib = Book_Library(['Python', 'C++', 'C#', 'Life Tips'],"CodeWithRajat")

    while (True):
        print(f"Welcome to {lib.name} Liabrary")
        print("Enter Your Choice")
        print("1 for display  books")
        print("2 for Lend the book")
        print("3 for add the book")
        print("4 for return the book")
        x = int(input())

        if x == 1:
            lib.display_books()
        elif x == 2:
            name = input("Enter Your Name")
            book = input("Enter Your Book Name")
            lib.lend_book(name,book)
        elif x == 3:
            book = input("Enter book Name")
            lib.add_book(book)
        elif x == 4:
            book = input("Enter Name of book")
            lib.return_book(book)
        else:
            print("Your Entered a wrong Choice")

        y = input("Press C to continue & E to Exit")
        while(y != "C" and y != "E"):
            if y == 'E':
                exit()
            elif y == 'C':
                continue
