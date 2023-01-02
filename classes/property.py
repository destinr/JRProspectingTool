import csv
##########################################################################################
# Class: Property                                                                          #
# Attributes: Property ID (rid), address,             #
# Methods: Loads all movies from csv, checkoutMovie, checkinMovie                        #
##########################################################################################


class Movie:
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
        
        self.copies_available = int(self.copies_available)
            
    def checkoutMovie(self):
        self.copies_available -= 1
        
    def checkinMovie(self):
        self.copies_available += 1
            
    @classmethod
    def inputAllMovies(cls,file):
        movieList = []
        with open(file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                movieList.append(Movie(**row))
        
        return movieList