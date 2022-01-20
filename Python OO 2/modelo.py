class Movie:

    def __init__(self, movie_name, movie_year, movie_duration):
        self.__movie_name = movie_name.title()
        self.movie_year = movie_year
        self.movie_duration = movie_duration
        self.__likes_quantity = 0
    
    @property
    def movie_name(self):
        return self.__movie_name
    
    @property
    def likes_quantity(self):
        return self.__likes_quantity
    
    def give_like(self):
        self.__likes_quantity += 1

class Series:

    def __init__(self, series_name, series_year, series_season):
        self.__series_name = series_name.title()
        self.series_year = series_year
        self.series_duration = series_season
        self.__likes_quantity = 0
    
    @property
    def series_name(self):
        return self.__series_name
    
    @property
    def likes_quantity(self):
        return self.__likes_quantity
    
    def give_like(self):
        self.__likes_quantity += 1

def test():

    movie1 = Movie("test Movie name", 1997, 165)
    series1 = Series("test series Name", 2000, 5)

    movie1.give_like()
    movie1.give_like()

    series1.give_like()
    series1.give_like()
    series1.give_like()

    print("Name: {} --- Year: {} --- Duration: {} --- Likes: {}".format(movie1.movie_name, movie1.movie_year, movie1.movie_duration, movie1.likes_quantity))
    print("Name: {} --- Year: {} --- Seasons: {} --- Likes: {}".format(series1.series_name, series1.series_year, series1.series_duration, series1.likes_quantity))

if( __name__ == "__main__"):
    test()
    
