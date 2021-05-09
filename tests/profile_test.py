import unittest
from src.profile import *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)

        self.profile_1 = Profile("harrisonF", "myP@assword")

        

    # Test a Profile can add a favourite Movie
    def test_profile_add_movie(self):
        self.assertEqual(0, self.profile_1.favourites_lenght())
        self.profile_1.add_movie(self.movie_1)
        self.assertEqual(1, self.profile_1.favourites_lenght())
        
       
    # Test a Profile can remove a given Movie from favourites
    def test_profile_remove_movie(self):
        self.profile_1.add_movie(self.movie_1)
        self.profile_1.remove_movie(self.movie_1)
        self.assertEqual(True, self.movie_1 not in self.profile_1.favourites)


    # Test a Profile can return a list of Favourites
    def test_favourites_count(self):
        self.assertEqual(False, bool(len(self.profile_1.favourites)))

   
