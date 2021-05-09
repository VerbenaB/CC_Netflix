class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def favourites_lenght(self):
        return len(self.favourites)
    
    def add_movie(self, movie):
        self.favourites.append(movie)

    def remove_movie(self, movie):
        self.favourites.remove(movie)