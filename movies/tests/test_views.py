from django.test import TestCase, Client
from movies.models import Movie



class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Example Movie', year=2000, imdb=7, genre='Fantastic')
        
        self.client = Client()
        
        

    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEqual(data[0]['name'], 'Example Movie')


   


class TestMovieSetSearch(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Search Movie', year=2000, imdb=7, genre='Fantastic')
        self.client = Client()


    def test_search(self):
        response = self.client.get('/movies/?search=Search')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        
        self.assertEqual(data[0]['name'], 'Search Movie')

    



class MovieOrderingTests(TestCase):

    def setUp(self):
        
        self.movies = [
            Movie.objects.create(name='Ordering Movie', year=2000, imdb=7, genre='Fantastic'),
            Movie.objects.create(name='Ordering Movie', year=2000, imdb=8, genre='Fantastic'),
            Movie.objects.create(name='Ordering Movie', year=2000, imdb=5, genre='Fantastic')
        ]

    def test_ordering_by_imdb(self):
        
        response = self.client.get('/movies/?ordering=imdb') 

        self.assertEqual(response.status_code, 200)

        ordered_movies = [movie['imdb'] for movie in response.data]
        
        self.assertEqual(ordered_movies, sorted(ordered_movies))