class Bookstore:
    NoOfBooks = 0
    def __init__(self,book, author):
        self.Name = book
        self.Author = author
        Bookstore.NoOfBooks = Bookstore.NoOfBooks + 1

    def Display(self):
        print("Name of the Book:", self.Name)
        print("Name of the author:", self.Author)
        print("Number of books:", Bookstore.NoOfBooks)


def main():
    obj1 = Bookstore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = Bookstore("C Programming", "Dennis Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()