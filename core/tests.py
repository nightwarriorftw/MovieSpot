from django.test import TestCase

from .models import MovieSpotModel


class MovieSpotTestCase(TestCase):
    def setUp(self):
        MovieSpotModel.objects.create(
            title='American Pie',
            release_year='2011',
            location='Stanford',
            funfacts='This is awesome test',
            productionCompany='Testing Production',
            director='Adam Smith',
            writer='Haisley',
            actor1='test1',
            actor2='test2',
            actor3='test3'
        ).save()
        MovieSpotModel.objects.create(
            title='The Social Network',
            release_year='2012',
            location='Harvard',
            funfacts='This is awesome test',
            productionCompany='Mark Zukerberg Production',
            director='Adam Smith',
            writer='KSI',
            actor1='test1',
            actor2='test2',
            actor3='test3'
        ).save()

    def test_spotMovieLocation(self):
        location1 = MovieSpotModel.objects.get(
            location='Stanford', title='American Pie').location
        location2 = MovieSpotModel.objects.get(location='Harvard').location
        self.assertNotEqual(location1, 'Harvard')
        self.assertEqual(location2, 'Harvard')
