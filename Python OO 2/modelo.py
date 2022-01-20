class TV_program:

    def __init__(self, program_name, program_year):
        self._program_name = program_name.title()
        self.program_year = program_year
        self._likes_quantity = 0

    @property
    def program_name(self):
        return self._program_name
    
    @property
    def likes_quantity(self):
        return self._likes_quantity
    
    def give_like(self):
        self._likes_quantity += 1

class Movie(TV_program):

    def __init__(self, movie_name, movie_year, movie_duration):
        super().__init__(movie_name, movie_year)
        self.movie_duration = movie_duration

class Series(TV_program):

    def __init__(self, series_name, series_year, series_season):
        super().__init__(series_name, series_year)
        self.series_duration = series_season


def test():

    movie1 = Movie("test Movie name", 1997, 165)
    series1 = Series("test series Name", 2000, 5)

    movie1.give_like()
    movie1.give_like()

    series1.give_like()
    series1.give_like()
    series1.give_like()

    print("Name: {} --- Year: {} --- Duration: {} --- Likes: {}".format(movie1.program_name, movie1.program_year, movie1.movie_duration, movie1.likes_quantity))
    print("Name: {} --- Year: {} --- Seasons: {} --- Likes: {}".format(series1.program_name, series1.program_year, series1.series_duration, series1.likes_quantity))

if( __name__ == "__main__"):
    test()
    
