class Book:
    def __init__(self, autor, title, pages):
        self.autor = autor
        self.title = title
        self.pages = pages

    def show_info(self):
        print("Название:", self.title)
        print("Автор:", self.autor)
        print("Страниц:", self.pages)

book1 = Book ("Джоан Роулинг", "Гарри Поттер", 300)
book2 = Book ("Джон Толкиен", "Властелин колец", 500)
book3 = Book ("Михаил Булгаков", "Мастер и маргарита", 200)

book1.show_info()
book2.show_info()
book3.show_info()