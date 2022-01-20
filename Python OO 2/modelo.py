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

    def __str__(self):
        return "Name: {} --- Year: {} --- Likes: {}".format(self.program_name, self.program_year, self.likes_quantity)

class Movie(TV_program):

    def __init__(self, movie_name, movie_year, movie_duration):
        super().__init__(movie_name, movie_year)
        self.movie_duration = movie_duration

    def __str__(self):
        return "Name: {} --- Year: {} --- Duration: {} --- Likes: {}".format(self.program_name, self.program_year, self.movie_duration, self.likes_quantity)

class Series(TV_program):

    def __init__(self, series_name, series_year, series_season):
        super().__init__(series_name, series_year)
        self.series_duration = series_season

    def __str__(self):
        return "Name: {} --- Year: {} --- Seasons: {} --- Likes: {}".format(self.program_name, self.program_year, self.series_duration, self.likes_quantity)

def test():

    movie1 = Movie("test Movie name", 1997, 165)
    series1 = Series("test series Name", 2000, 5)

    movie1.give_like()
    movie1.give_like()

    series1.give_like()
    series1.give_like()
    series1.give_like()

    list_programs = [movie1, series1]

    for programs in list_programs:
        print(programs)

if( __name__ == "__main__"):
    test()
    
