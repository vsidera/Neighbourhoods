from django.test import TestCase
from .models import Post, Profile, Neighbourhood
from datetime import datetime
from django.contrib.auth.models import User



class ProfileTest(TestCase):
    ''' test class for Profile model'''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='vik')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()

    def test_profile_creation(self):
        ''' method to test profile instance is created only once for each user '''
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)
        

class TestPost(TestCase):
    ''' test class for image model '''
    def setUp(self):
        ''' method called before each test case'''
        self.test_user = User(username='vik', password='vik@123')
        self.test_user.save()
        self.test_profile = self.test_user.profile
        self.test_profile.save()

        self.test_post = Post(image='images/vik.jpg', title='vinstagram',description='Instagram Clone', profile=self.test_profile, live_link='https://vinsta.herokuapp.com/', created_on=datetime.now())

    def test_instance(self):
        ''' test method to ensure post instance creation '''
        self.assertTrue(isinstance(self.test_post, Post))

    def test_save_and_delete(self):
        ''' test method to save and delete post instance to db '''
        self.test_post.save_post()
        self.assertEqual(len(Post.objects.all()), 1)
        self.test_post.delete_post()
        self.assertEqual(len(Post.objects.all()), 0)

    def test_search_project(self):
        ''' test method to search projects by title '''
        self.test_post.save_post()
        res = Post.search_project('Vinstagram')
        self.assertIsNotNone(res)

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.test_user.delete() 
        Post.objects.all().delete()


class TestNeighbourhood(TestCase):
    ''' test class for Neighbourhood model '''
    def setUp(self):
        ''' method called before all tests '''
        self.test_user = User(username='vik', password='vik@123')
        self.test_user.save()
        self.test_profile = self.test_user.profile
        self.test_profile.save()
        self.test_post = Post(image='images/vik.jpg', title='Vinstagram',description='Instagram Clone', profile=self.test_profile, live_link='https://vinsta.herokuapp.com/', created_on=datetime.now())
        self.test_post.save()

        self.test_rate = Neighbourhood(interface=5, experience=6, content=5, user=self.test_profile, post=self.test_post)

    def tearDown(self):
        ''' method called after every test '''
        self.test_user.delete() 
        Post.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        ''' method to test instance creation '''
        self.assertIsInstance(self.test_rate, Neighbourhood)

    def test_save_and_delete_hood(self):
        ''' test method to save and delete hoods'''
        self.test_rate.save_hood()
        self.assertEqual(len(Neighbourhood.objects.all()), 1)
        self.test_rate.delete_hood()
        self.assertEqual(len(Neighbourhood.objects.all()), 0)
