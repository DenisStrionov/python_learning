class Movie:

    def __init__(self, title, genre,year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def show_info(self):
        print("Название", self.title)
        print("Жанр", self.genre)
        print("Год", self.year)
        print("Рейтинг", self.rating)

movie1 = Movie ("Бэтмэн", "Боевки", 2024, 8.0)
movie2 = Movie ("Интерстелар", "Фантастика", 2018, 9.0)

movie1.show_info()
movie2.show_info()

